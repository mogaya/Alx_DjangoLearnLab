from django.contrib import admin
from .models import Author, Book, Library, Librarian, CustomUser

from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('date_of_birth', 'profile_photo')}),
#     )
#     add_fieldsets = UserAdmin.add_fieldsets + (
#         (None, {'fields': ('date_of_birth', 'profile_photo')})
#     )

# admin.site.register(CustomUser, CustomUserAdmin)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)