from django.db import models
from user.models import User

# Create your models here.

class Auth(models.Model):
    user_uid = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='user_uid.',
        help_text='char(1 -> 20).'
    )
    user_name = models.TextField(
        max_length=40,
        unique=True,
        verbose_name='user_name.',
        help_text='char(1->40).'
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='user_email',
        help_text='char(1 -> 100).'
    )
    password = models.TextField(
        max_length=100,
        verbose_name='password.',
        help_text='char(1 -> 100).'
    )
    on_session = models.BooleanField(
        default=False,
        verbose_name='on_session?',
    )
    is_verified = models.BooleanField(
        default=False,
        verbose_name='is_verified?',
    )
    is_reset = models.BooleanField(
        default=False,
        verbose_name='is_reset?'
    )
    secure_key = models.TextField(
        max_length=
    )

