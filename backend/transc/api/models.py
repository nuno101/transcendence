from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
# import uuid # TODO: Use UUIDs?

class User(AbstractUser):
	username = models.CharField(max_length=12, unique=True, null=False)
	nickname = models.CharField(max_length=12, unique=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	avatar = models.BinaryField(max_length=900000, null=False)

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
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username
	
	def save(self, *args, **kwargs):
		# On first save, create stats
		if self._state.adding:
			super().save(*args, **kwargs)
			UserStats.objects.create(user=self)
		else:
			super().save(*args, **kwargs)

	def serialize(self, private=False):
		return {
			'id': self.id,
			'username': self.username,
			'nickname': self.nickname,
			'created_at': str(self.created_at),
			'updated_at': str(self.updated_at),
			'status': self.status if private else None,
		}

class UserStats(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name="stats")
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.user.username}\'s stats'

	def serialize(self):
		return {
			'user_id': self.user.id,
			'wins': self.wins,
			'losses': self.losses,
			'created_at': str(self.created_at),
			'updated_at': str(self.updated_at),
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
        'creator_id': self.creator.id,
        'status': self.status,
        'created_at': str(self.created_at),
        'updated_at': str(self.updated_at),
    }

class Game(models.Model):
	class MatchStatus(models.TextChoices):
			CREATED = "created"
			ONGOING = "ongoing"
			DONE = "done"
			CANCELLED = "cancelled"
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	player1 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	player2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="visitor")
	status = models.CharField(
		max_length=36,
		choices=MatchStatus.choices,
		default=MatchStatus.CREATED,
	)
	player1_score = models.IntegerField(default=0)
	player2_score = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f'{self.player1} vs {self.player2}'
	
	def save(self, *args, **kwargs): # TODO: Find better way to update user stats in a nice way. This is ugly and won't work reliably.
		super().save(*args, **kwargs)

		# Update user stats
		if self.status == Game.MatchStatus.DONE:
			if self.player1_score > self.player2_score:
				self.player1.stats.wins += 1
				self.player2.stats.losses += 1
			elif self.player1_score < self.player2_score:
				self.player1.stats.losses += 1
				self.player2.stats.wins += 1
			self.player1.stats.save()
			self.player2.stats.save()

	def serialize(self):
		return {
			'id': self.id,
			'tournament_id': self.tournament.id,
			'player1_id': self.player1.id,
			'player2_id': self.player2.id,
			'status': self.status,
			'player1_score': self.player1_score,
			'player2_score': self.player2_score,
			'created_at': str(self.created_at),
			'updated_at': str(self.updated_at),
		}

class Channel(models.Model):
    # TODO: Use UUIDs?
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    members = models.ManyToManyField(User, related_name="channels")

    def __str__(self):
        return self.name

    def serialize(self):
      return {
          'id': self.id,
          'name': self.name,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at),
          'members': [m.serialize() for m in self.members.all()]
      }

class Message(models.Model):
    # TODO: Use UUIDs?
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
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
          'author_id': self.author.id,
          'channel_id': self.channel.id,
          'created_at': str(self.created_at),
          'updated_at': str(self.updated_at)
      }