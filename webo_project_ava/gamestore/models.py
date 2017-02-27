from django.db import models
from django.contrib.auth.models import User
from time import time
import datetime

# Tiedostojen lahetyksen funktio maarittelee polun ja tiedostojen nimen,
# jottei samannimisia tiedostoja yriteta luoda. (aikaan perustuva)
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Laajentaa djangon tarjoamaa valmista User-mallia
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	activation_key = models.CharField(max_length=40, blank=True)
	key_expires = models.DateTimeField(default=datetime.date.today())
	is_a_developer = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name_plural=u'User profiles'

class Game(models.Model):
	name = models.CharField(max_length=255)
	owner = models.ForeignKey(User, null=True, editable=False)
	url = models.URLField(max_length=255, unique=True)
	image = models.FileField(upload_to=get_upload_file_name)
	highscores = models.TextField(null=True)

# Pelin tallennus, joka identifioidaan pelin ja käyttäjän perusteella
class Savedata(models.Model):
	user = models.ForeignKey(User)
	game = models.ForeignKey(Game)
	data = models.TextField(null=True)
	score = models.IntegerField(default=0)
