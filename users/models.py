from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator, MinLengthValidator
from sorl.thumbnail import ImageField

# from order.models import Order


class MyUserManager(BaseUserManager):
    """Create custom user manager for our custom User"""
    def create_user(self, username, password=None, first_name='', last_name='', **kwargs):
        """
        Creates and saves a User with the given username and password.
        """
        if not username:
            raise ValueError(_('Users must have an username, email or phone'))
	# This block process any optional arguement when creating new user
        additionalArguements = dict()
        if kwargs:
            for k, v in kwargs.items():
                if k in dir(User):
                    additionalArguements.update({k: v})
        user = self.model(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **additionalArguements
        )
        user.set_password(password)
        user.user_db_backend = 'regular'
        user.save(using=self._db)
        return user

    # def create_superuser(self, username, password=None, name=None, **kwargs):
    def create_superuser(self, username, password=None, first_name='', last_name='', **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.user_db_backend = 'regular'
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model represents any user signup in the application."""
    USER_DB_BACKEND_CHOICES = [
        ('regular', 'regular'),     # 'regular' means django authentication default backend
        ('api', 'api'),             # 'api' means DRF authentication backend
        ('social', 'social'),       # 'social' means social backend
    ]
    username = models.CharField(max_length=40,
                                unique=True,
                                verbose_name=_('username'),
                                validators=[MaxLengthValidator(33, _('username is too long')),
                                            MinLengthValidator(3, _('username is too short'))],
                                )
    email = models.EmailField(unique=False, verbose_name=_('email'), blank=True)
    phone = models.CharField(verbose_name=_('phone'),
                             max_length=15,
                             blank=True,
                             validators=[MaxLengthValidator(13, _('phone cannot be longer than 13 chars')),
                                         MinLengthValidator(11, _('phone cannot be shorter than 11 chars'))])
    first_name = models.CharField(verbose_name=_('first name'),
                                  max_length=50,
                                  blank=True,
                                 )
    last_name = models.CharField(verbose_name=_('last name'),
                                 max_length=50,
                                 blank=True,
                                 )
    picture = ImageField(verbose_name=_('user picture'), blank=True)
    gender = models.CharField(verbose_name=_('gender'), max_length=6, blank=True, null=True, choices=[('M', 'M'), ('F', 'F')])
    marketing = models.BooleanField(verbose_name=_('marketing'), default=False)
    personal = models.BooleanField(verbose_name=_('personal'), default=False)
    address = models.TextField(verbose_name=_('address'), blank=True)
    score = models.IntegerField(verbose_name=_('user score'), default=0)
    score_lifetime = models.IntegerField(verbose_name=_('user score'), default=0)
    discount_value = models.DecimalField(verbose_name=_('user discount(value)'), default=0, max_digits=9,
                                         decimal_places=0)
    discount_percent = models.DecimalField(verbose_name=_('user discount(percent)'), default=0, max_digits=5,
                                           decimal_places=2,
                                           validators=[
                                               MaxValueValidator(100, _('percent could not be more than 100')),
                                               MinValueValidator(0, _('percent could not be less than 0'))
                                           ])
    is_active = models.BooleanField(default=True, verbose_name=_('is active'))
    is_staff = models.BooleanField(default=False, verbose_name=_('is staff'))
    is_admin = models.BooleanField(default=False, verbose_name=_('is admin'))
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'))
    objects = MyUserManager()

    # Field used to knowldege user signup with social_login or any other backend
    is_social_login = models.BooleanField(verbose_name=_('is social login'), default=False)
    user_db_backend = models.CharField(verbose_name=_('user db backend'),
                                       max_length=100,
                                       blank=True,
                                       choices=USER_DB_BACKEND_CHOICES)
    
    USERNAME_FIELD = 'username'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'

    def __str__(self) -> str:
        return self.username
