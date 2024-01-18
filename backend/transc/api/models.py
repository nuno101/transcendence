from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	username = models.CharField(max_length=12, unique=True, null=False)
	#avatar = models.ImageField(upload_to='avatars/', null=True, blank=True) # TODO
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	avatar = models.BinaryField(max_length=900000, null=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def serialize(self):
		return {
			'id': self.id,
			'username': self.username,
			'created_at': self.created_at,
			'updated_at': self.updated_at,
		}

class Friend(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="dummy")
	friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def serialize(self):
		return {
			'user_id': self.user.id,
			'friend_id': self.friend.id,
			'created_at': self.created_at,
		}

class Tournament(models.Model):
	class TournamentStatus(models.TextChoices):
			CREATED = "created"
			REG_OPEN = "registration_open"
			REG_CLOSED = "registration_closed"
			ONGOING = "ongoing"
			DONE = "done"
			CANCELLED = "cancelled"

	title = models.CharField(max_length=150)
	description = models.CharField(max_length=900)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(
        max_length=36,
        choices=TournamentStatus.choices,
        default=TournamentStatus.CREATED,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
	
	def serialize(self):
		return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'creator_id': self.creator_id,
        'status': self.status,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
    }

class Game(models.Model):
	class MatchStatus(models.TextChoices):
			CREATED = "created"
			ONGOING = "ongoing"
			DONE = "done"
			CANCELLED = "cancelled"
	tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	player_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	player2_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="visitor")
	status = models.CharField(
        max_length=36,
        choices=MatchStatus.choices,
        default=MatchStatus.CREATED,
	)
	score = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def serialize(self):
		return {
        'id': self.id,
        'tournament_id': self.tournament_id.id,
        'player_id': self.player_id.id,
        'player2_id': self.player2_id.id,
        'status': self.status,
        'score': self.score,
        'created_at': self.created_at,
        'updated_at': self.updated_at,
    }
