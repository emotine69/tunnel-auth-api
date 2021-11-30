from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# length style guide:
# id:   32,
# name: 40,
# email: 100,
# password: 100,
# other: 50,


class User(models.Model):
    user_uid = models.CharField(
        max_length=32,
        unique=True,
        verbose_name='user_uid',
        help_text='char(1 -> 28).',
        primary_key=True
    )
    user_name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='user_name',
        help_text='char(1 -> 40).',
    )
    user_email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name='user_email',
        help_text='char(1 -> 100).'
    )
    user_full_name = models.CharField(
        max_length=50,
        verbose_name='user_full_name',
        help_text='char(1 -> 50).'
    )
    province = models.CharField(
        # Attributes.
        max_length=50,
        # Details.
        verbose_name="province.",
        help_text="char(1 -> 50).",
    )
    district = models.CharField(
        # Attributes.
        max_length=50,
        # Details.
        verbose_name="district.",
        help_text="char(1 -> 50).",
    )
    ward = models.CharField(
        max_length=50,
        verbose_name="ward.",
        help_text="char(1 -> 50).",
    )
    detail_adr = models.TextField(
        max_length=50,
        verbose_name='detail_adr.',
        help_text='char(1 -> 50).'
    )
    phone_number = PhoneNumberField()

    class Meta:
        verbose_name = 'user_uid.'
        verbose_name_plural = 'user_uids.'

    def __str__(self):
        return str(self.user_uid)
