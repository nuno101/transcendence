from django.db import models

# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=12, unique=True, null=False)
	fullname = models.CharField(max_length=60, null=False)
	avatar = models.BinaryField(max_length=900000, null=False)
	password_hash = models.CharField(max_length=255, null=False) 
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Session(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Friend(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dummy")
	friend = models.ForeignKey(User, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)

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


class Match(models.Model):
	class MatchStatus(models.TextChoices):
			CREATED = "created"
			ONGOING = "ongoing"
			DONE = "done"
			CANCELLED = "cancelled"
	tournament_id = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	player_id = models.ForeignKey(User, on_delete=models.CASCADE)
	player2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visitor")
	status = models.CharField(
        max_length=36,
        choices=MatchStatus.choices,
        default=MatchStatus.CREATED,
	)
	score = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

