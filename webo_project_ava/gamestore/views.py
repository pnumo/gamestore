from django.shortcuts import render, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib import auth
from gamestore.models import UserProfile, Game, Savedata
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from gamestore.forms import *
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.mail import send_mail
import hashlib, datetime, random, operator, json
from django.utils import timezone


def starting_site(request):
	return render(request,"index.html",{'games':Game.objects.order_by('?')[:8]})

#register_user funktio luo käyttäjän profiilin ennalta, tallettaa siihen
#tarvittavat tiedot, mutta ei aseta profiilia aktiiviseksi
#activation_key muodostetaan random merkkijonosta ja emailista luodusta hashista
def register_user(request):
	args = {}
	args.update(csrf(request)) #csrf huomioitu

	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		args['form'] = form

		if form.is_valid():
			form.save()

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			is_a_developer=form.cleaned_data['is_a_developer']
			random_string = str(random.random()).encode('utf8')
			salt = hashlib.sha1(random_string).hexdigest()[:5]
			salted = (salt+email).encode('utf8')
			activation_key = hashlib.sha1(salted).hexdigest()
			key_expires = datetime.datetime.today() + datetime.timedelta(2)
			user = User.objects.get(username=username)

			profile = UserProfile(user=user, activation_key=activation_key,
									key_expires=key_expires,
									is_a_developer=is_a_developer)
			profile.save()

			email_subject ='Account verification'
			email_body = "Hello %s, thanks for registering. To activate your profile, click the following link: http://127.0.0.1:8000/confirm/%s" % (username, activation_key)

			#lahetetaan email kohdeosoitteeseen.
			send_mail(email_subject, email_body, 'myemail@domain.com',
						[email], fail_silently = False)

			return HttpResponseRedirect('/register_confirmation')

	else:
		args['form'] = RegistrationForm()

	return render_to_response('register.html', args,
								context_instance=RequestContext(request))

#tama funktio toteuttaa rekisteroinnin viimeistelyn varmentamalla, etta
#linkin sisaltama aktivointiavoin vastaa UserProfileen talletettua avainta
def register_confirm(request, activation_key):

	if request.user.is_authenticated():
		HttpResponseRedirect('/')

#mikali ei vastaavutta, renderoidaan 404
	user_profile =get_object_or_404(UserProfile, activation_key=activation_key)

#mikali ei rekisteroity 48h sisalla, renderoidaan virhesivu
	if user_profile.key_expires < timezone.now():
		return render_to_response('confirmation_expired.html')

#mikali kaikki ok, muutetaan kayttaja aktiiviseksi ja login onnistuu
	user = user_profile.user
	user.is_active =True
	user.save()
	return render_to_response('register_success.html')

def register_success(request):
	return render_to_response('register_success.html')

def confirm_required(request):
	return render_to_response('confirmation_required.html')

#sisaankirjautumisen lomakkeen funktio, csrf huomioitu
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

#autentikoinnin toteutus, tarkastetaan vastaako syotetyt tiedot db:a
def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/loggedin')
	else:
		return HttpResponseRedirect('/invalid')

#sisaankirjautumisen onnistumisen palautesivu
@login_required
def loggedin(request):
	return render_to_response('loggedin.html',
							{ 'full_name': request.user.username})

#sisaankirjautuminen ei onnistunut
def invalid_login(request):
	return render_to_response('invalid_login.html')

#uloskirjaus djangon auth toiminnallisuuden avulla.
def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

#valitetaan games.html:lle kaikki peliobjektit
def games(request):
	return render(request, 'games.html', {'games': Game.objects.all() })

# Globaalien ja käyttäjän highscojen sekä itse pelin haku
@login_required
def game(request, game_id=1):
	def globalscores(request, game_id):
		try:
			game = Game.objects.get(id=game_id)
			scores_json = game.highscores
		except Game.DoesNotExist:
			raise Http404("Game doesn't exist")
		scores = []
		my_best_score = 0

		if scores_json is not None:
			scores_obj = json.loads(scores_json)
			for score_obj in scores_obj["scores"]:
				scores.append(score_obj)
				if request.user.username == score_obj["player"] and int(score_obj["score"]) > my_best_score:
					my_best_score = int(score_obj["score"])
			scores.sort(key=lambda x: int(x["score"]), reverse=True)
		return scores, my_best_score

	scores, my_best_score = globalscores(request, game_id)
	return render(request, "game.html",
		{ 'onegame': Game.objects.get(id=game_id), 'globalscores': scores,
		'my_best_score': my_best_score })

#pelin lisaamisen lomekkeen kasittelija, csrf huomioitu
@login_required
def addgame(request):
	if request.POST:
		form = Gameform(request.POST, request.FILES)

		if form.is_valid():
			addgame = form.save(commit=False)
			addgame.owner=request.user
			addgame.save()
			return HttpResponseRedirect('/games/')

	else:
		form= Gameform()

	args = {}
	args.update(csrf(request))

	args['form'] = form
	return render(request, 'addgame.html', args)

#pelin poistamisessa testataan vastaako id pelia tietokannassa vai annetaanko
#404, tarkistetaan seuraavaksi onko poistettavaksi halutun pelin omistaja
#sama kuin poistaja, mikali ei renderoidaan 403
@login_required
def delete_game(request, game_id):
    game_to_delete = get_object_or_404(Game, id=game_id)

    if game_to_delete.owner != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game_to_delete)

        if form.is_valid():
            game_to_delete.delete()
            return HttpResponseRedirect("/")

    else:
        form = DeleteGameForm(instance=game_to_delete)

    template_vars = {'form': form}
    return render(request, '/game.html', template_vars)

@login_required
def profile(request):
	return render(request, 'profile.html')

#Profiilin paivitys, luodaan lomake nimenomaan kyseisesta kayttajaa vastaa-
#vasta modelista
@login_required
def update_profile(request, template_name="update_profile.html"):
	
    if request.method == "POST":
        form = UpdateProfile(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return HttpResponseRedirect('/update_success')
    else:
        form = UpdateProfile(instance=request.user)
    page_title = ('Edit user names')

    return render_to_response(template_name, locals(),
        context_instance=RequestContext(request))

def update_success(request):
	return render_to_response('update_success.html')

@login_required
def update_game(request, game_id=None):
    instance = get_object_or_404(Game, id=game_id)
    form = UpdateGame(request.POST or None, instance=instance)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return HttpResponseRedirect('/games')

    context = {
        "name": instance.name,
        "instance": instance,
        "form": form,
    }
    return render(request, "update_game.html", context)

# Highscoren tallennus kantaan JSON-formaatissa.
@csrf_exempt
def submit_highscore(request, template_name="game.html"):
	if request.method == "POST":
		gamename = request.POST["game"]
		score = request.POST["score"]
		user = request.POST["user"]

		game = Game.objects.get(name=gamename)
		if game.highscores == None:
			score_obj = {"scores": [{"player": user, "score": score}]}
		else:
			new_score = {"player": user, "score": score}

			score_obj_json = game.highscores
			score_obj = json.loads(score_obj_json)
			score_obj["scores"].append(new_score)
		game.highscores = json.dumps(score_obj)
		game.save()

		return HttpResponse("SUCCESS!")

	return HttpResponse("FAILURE!")

# Pelin tilan tallennus kantaan korvaten edellinen vastaava tila
# ja jos sellaista ei ole, luodaan uusi.
# Yhtä käyttäjä-peli -yhdistelmää vastaa maksimissaan yksi tila.
@csrf_exempt
def save_state(request, template_name="game.html"):
	if request.method == "POST":
		gamename = request.POST["game"]
		savedata = request.POST["savedata"]
		score = request.POST["score"]
		username = request.user.username

		game = Game.objects.get(name=gamename)
		user = User.objects.get(username=username)

		save, created = Savedata.objects.get_or_create(user=user, game=game)
		save.data = savedata
		save.score = score;
		save.save()

		return HttpResponse("SUCCESS!")

	return HttpResponse("FAILURE!")

# Pelin tilan haku käyttäjän ja pelin perusteella.
def load_state(request, template_name="game.html"):
	if request.method == "GET":
		gamename = request.GET["game"]
		username = request.user.username

		game = Game.objects.get(name=gamename)
		user = User.objects.get(username=username)

		save = Savedata.objects.get(user=user, game=game)
		result = {}
		result["messageType"] = "LOAD"
		result["gameState"] = {"playerItems": save.data, "score": save.score}
		#data = {"messageType":"LOAD", "gameState":{"playerItems":json.loads(save.data),
		#"score": save.score}}
		result = json.dumps(result)

		return HttpResponse(result)
	return HttpResponse("FAILURE!")
