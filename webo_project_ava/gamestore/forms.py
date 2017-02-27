from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from gamestore.models import Game, UserProfile

#rekisteroinnin lomake: asetetaan tarvittavat kentat
class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'E-mail address'}))
	first_name = forms.TextInput()
	last_name = forms.TextInput()
	is_a_developer = forms.BooleanField(initial=False, required=False)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name',
			'is_a_developer', 'password1', 'password2')

#siivotaan email kentta ja tarkastetaan onko syotetty email kaytossa
	def clean_email(self):
		email = self.cleaned_data["email"]
		try:
			User._default_manager.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('This email is already in use!')

#talletetaan tiedot user modeliin, mutta asetetaan tili inaktiiviseksi
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']

		if commit:
			user.is_active = False
			user.save()
		return user

#uuden pelin syottamiseen tarkoitettu lomake: pelin nimi, url ja bannerkuva
class Gameform(forms.ModelForm):

	class Meta:
		model = Game
		fields = ('name', 'url', 'image')

class DeleteGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = []

#Profiilin rajallinen muokkaus lomake: voi mukauttaa vain nimet, silla tama ei
#ollut pakollinen toiminnallisuus, ja emailin ja kayttajanimen muuttamiseen
#pitaisi tehda lisatoita tarkastuksia varten
class UpdateProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

#pelin muokkauksen lomake. Bannerin muuttamista ei toteutettu
class UpdateGame(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'url']
