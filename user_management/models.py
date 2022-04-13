from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class CustomAccountManager(BaseUserManager):
    """Custom Account Manager class.
    Parameters
    ----------
    BaseUserManager : django.contrib.auth.models
    """

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        """Create django super user.
        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        password : str
        Returns
        -------
        django.contrib.auth.models import User
        Raises
        ------
        ValueError
            raise "Superuser must be assigned to is_staff=True." if user has not staff role
        ValueError
            raise "Superuser must be assigned to is_superuser=True." if user has not superuser role
        """
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if other_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, first_name, last_name, password, **other_fields)

    def create_user(self, email, first_name, last_name, password, **other_fields):
        """Create django super user.
        Parameters
        ----------
        email : str
        first_name : str
        last_name : str
        password : str
        Returns
        -------
        django.contrib.auth.models.User
        Raises
        ------
        ValueError
            raise "You must provide an email address" if email address is not given
        """
        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Django core user class.
    Parameters
    ----------
    AbstractBaseUser : django.contrib.auth.models
    PermissionsMixin : django.contrib.auth.models
    Returns
    -------
    django.contrib.auth.models.User
    """

    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(
        _("image"), upload_to=upload_to,null=True,blank=True)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    objects = CustomAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "phone_number"]


    def __str__(self):
        """Str representation of user model.
        Returns
        -------
        str
            returns the string containing the first name and last name
        """
        return f"{self.first_name} {self.last_name}"



class Profile(models.Model):
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    image = models.ImageField(
        _("image"), upload_to=upload_to,null=True,blank=True)
    bio = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

