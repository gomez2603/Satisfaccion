from __future__ import unicode_literals, absolute_import
from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from cuestionario.models import *
from users.models import User


class EncuestaView(admin.ModelAdmin):
    list_display = ('p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10', 'ob1', 'ob2', 'answered_date')

admin.site.register(encuesta, EncuestaView)


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = AuthUserAdmin.fieldsets + (
        ('Extended Field', {'fields': ('is_answered',
                                       )}),
    )
    list_display = ('username','first_name','last_name','email' , 'is_superuser','is_answered')
    search_fields = ['username']