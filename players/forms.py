from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from players.models import Player, Equipment, Race


class EquipmentForm(forms.ModelForm):
    players = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Equipment
        fields = "__all__"


class PlayerCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Player
        fields = UserCreationForm.Meta.fields + (
            "race",
            "level",
            "power",
        )

    def clean_race_level_power(self):
        return validate_race_level_power(
            self.cleaned_data["race"],
            self.cleaned_data["level"],
            self.cleaned_data["power"],
        )


class PlayerPowerAndLevelUpdateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["race", "level", "power"]

    def clean_race_level_power(self):
        return validate_race_level_power(
            self.cleaned_data["race"],
            self.cleaned_data["level"],
            self.cleaned_data["power"],
        )


def validate_race_level_power(
    race,
    level,
    power,
):
    if level < 1:
        raise ValidationError("Level must be greater than 0")
    if power < 1:
        raise ValidationError("Power must be greater than 0")
    if race not in Race:
        raise ValidationError("Choose a valid race")

    return race, level, power


class EquipmentNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class RaceNameSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class EquipmentTypeNameSearchForm(forms.Form):
    type = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by type"})
    )


class PlayerUsernameSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )
