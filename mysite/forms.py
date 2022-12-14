from django import forms
from django.contrib.auth import get_user_model
from .models import User
from .models import Profile


class UserCreationForm(forms.ModelForm[User]):
    password = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ("email",)

    def clean_password(self):
        password = self.cleaned_data.get("password")
        return password

    def save(self, commit=True) -> User:
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm[Profile]):
    class Meta:
        model = Profile
        fields = (
            "username",
            "zipcode",
            "prefecture",
            "city",
            "address",
        )
