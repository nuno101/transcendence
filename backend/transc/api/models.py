from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.validators import MinLengthValidator
import os

# cCONF: Avatar file path config
AVATAR_PATH = 'avatars/'
DEFAULT_AVATAR_NAME = os.getenv('DEFAULT_AVATAR_NAME', 'default.png')

class User(AbstractUser):
	def get_avatar_path(instance, filename):
		# Get file extension
		ext = filename.split('.')[-1]
		return f'{AVATAR_PATH}{instance.id}.{ext}'

	username = models.CharField(max_length=12, unique=True, null=False,validators=[
            MinLengthValidator(3, 'Username too short, must contain at least 3 characters')
            ])
	nickname = models.CharField(max_length=12, unique=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	avatar = models.ImageField(upload_to=get_avatar_path, null=True, blank=True)
	tournaments = models.ManyToManyField('Tournament', related_name='participants', blank=True)

	class States(models.TextChoices):
			OFFLINE = "offline"
			ONLINE = "online"
	status = models.CharField(
				max_length=36,
				choices=States.choices,
				default=States.OFFLINE,
	)

	# User relationships
	friends = models.ManyToManyField('self', blank=True)
	blocked = models.ManyToManyField("self", blank=True, symmetrical=False)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['nickname']

	def __str__(self):
		return self.username

	def get_avatar_url(self):
		if not self.avatar:
			return settings.MEDIA_URL + f'{AVATAR_PATH}{DEFAULT_AVATAR_NAME}'
		return self.avatar.url

	def serialize(self, private=False):
		tournaments_data = [tournament.serialize() for tournament in self.tournaments.all()]

		return {
			'id': self.id,
			'username': self.username,
			'nickname': self.nickname,
			'created_at': str(self.created_at.strftime("%Y-%m-%d %H:%M:%S")),
			'updated_at': str(self.updated_at.strftime("%Y-%m-%d %H:%M:%S")),
			'status': self.status if private else None,
			'tournaments': tournaments_data
		}

class FriendRequest(models.Model):
	to_user = models.ForeignKey(User, on_delete=models.CASCADE)
	from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dummy")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'
	
	def serialize(self):
		return {
			'id': self.id,
			'from_user': self.from_user.serialize(),
			'to_user': self.to_user.serialize(),
			'created_at': str(self.created_at),
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
	creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tournaments')
	status = models.CharField(
        max_length=36,
        choices=TournamentStatus.choices,
        default=TournamentStatus.CREATED,
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	players = models.ManyToManyField(User, related_name='joined_tournaments', blank=True)
	ranking = models.JSONField(null=True, blank=True)

	def __str__(self):
		return self.title

	def serialize(self):
		return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'creator': {
					'id' : self.creator.id,
					'username': self.creator.username,
					'nickname': self.creator.nickname
				},
        'status': self.status,
        'created_at': str(self.created_at.strftime("%Y-%m-%d %H:%M:%S")),
        'updated_at': str(self.updated_at.strftime("%Y-%m-%d %H:%M:%S")),
		'players': [{'id': player.id, 'username': player.username, 'nickname': player.nickname} for player in self.players.all()],
		'ranking': self.ranking
    }

class Game(models.Model):
	class MatchStatus(models.TextChoices):
			CREATED = "created"
			ONGOING = "ongoing"
			DONE = "done"
			CANCELLED = "cancelled"
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, blank=True, null=True, related_name="matches")
	player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="player1")
	player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="player2")
	status = models.CharField(
		max_length=36,
		choices=MatchStatus.choices,
		default=MatchStatus.CREATED,
	)
	player1_score = models.IntegerField(
		default=0,
		validators=[
        MaxValueValidator(11),
        MinValueValidator(0)
      ]
	)
	player2_score = models.IntegerField(
		default=0,
		validators=[
        MaxValueValidator(11),
        MinValueValidator(0)
      ]
	)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.player1} vs {self.player2}'

	def serialize(self):
		return {
			'id': self.id,
			'tournament':  self.tournament.serialize() if self.tournament else None,
			'player1': self.player1.serialize(),
			'player2': self.player2.serialize(),
			'status': self.status,
			'player1_score': self.player1_score,
			'player2_score': self.player2_score,
			'created_at': str(self.created_at.strftime("%Y-%m-%d %H:%M:%S")),
			'updated_at': str(self.updated_at.strftime("%Y-%m-%d %H:%M:%S")),
		}

class Notification(models.Model):
	type = models.CharField(max_length=36)
	content = models.CharField(max_length=250)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.content

	def serialize(self):
		return {
			'id': self.id,
			'type': self.type,
			'content': self.content,
			'user_id': self.user.id,
			'created_at': str(self.created_at),
		}

class Channel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(User, related_name="channels")

    def __str__(self):
        return str(self.id)

    def serialize(self):
      return {
          'id': self.id,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at),
          'members': [m.serialize() for m in self.members.all()]
      }

class Message(models.Model):
    content = models.TextField(max_length=2500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def serialize(self):
      return {
          'id': self.id,
          'content': self.content,
          'author': self.author.serialize(),
          'channel_id': self.channel.id,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }
