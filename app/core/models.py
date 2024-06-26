from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    """ Manager: User model """

    def create_user(self, email, **extra_fields):
        """ Create and save a new user """

        user = self.model(email=email.lower(), **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name):
        """ Create and save a new superuser """

        user = self.create_user(
            email=email,
            first_name=name)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    """ Model: User """

    # Field declarations
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    dnd_start_time = models.DateTimeField()
    dnd_end_time = models.DateTimeField()
    preferred_timezone = models.CharField(max_length=50)

    # Reference custom manager
    objects = UserManager()

    # Unique identifier field - email instead if username
    USERNAME_FIELD = 'email'
    # Fields for superuser creation
    REQUIRED_FIELDS = ['name']

    # String representation of model
    def __str__(self):
        return self.email

class Meeting(models.Model):
    class MeetingType(models.TextChoices):
        ONLINE = 'ONLINE'
        OFFLINE = 'OFFLINE'

    user = models.ForeignKey(User, 
        on_delete=models.CASCADE,
        related_name='meetings_user',
        related_query_name='meeting_user'
    )
    meeting_type = models.CharField(max_length=7, choices=MeetingType.choices)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    timezone = models.CharField(max_length=50, default="UTC")
    notification_interval = models.CharField(max_length=50)