from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

#     Step 1: Define Custom Permissions in Models
# Add custom permissions to one of your existing models (or a new model if preferable) to control actions such as viewing, creating, editing, or deleting instances of that model.

# Model Permissions to Add:
# Create permissions such as can_view, can_create, can_edit, and can_delete within your chosen model.

    class Meta:
        permissions = [
            ("can_view", "Can view books"),
            ("can_create", "Can create books"),
            ("can_edit", "Can edit books"),
            ("can_delete", "Can delete books"),
        ]


    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"
    
    
# Implement a custom user manager that handles user creation and queries, ensuring it can manage the added fields effectively.

# Custom Manager Functions to Implement:
# create_user: Ensure it handles the new fields correctly.
# create_superuser: Ensure administrative users can still be created with the required fields.

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be staff")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser must have superuser set to true")
        
        return self.create_user(username, email, password, **extra_fields)


# Create a custom user model by extending AbstractUser, adding custom fields that are relevant to your application’s needs.

# Fields to Add:

# date_of_birth: A date field.
# profile_photo: An image field.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customer_user_permissions",
        blank=True,
    )

    objects = CustomUserManager()

    def __str__(self):
        return self.username
