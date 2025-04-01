from django.contrib.admin import site
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from players.models import Player


class PlayerAdminTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user who can log in to the admin panel
        cls.user = get_user_model().objects.create_superuser(
            username="admin", password="password"
        )

        # Create a player instance
        cls.player = Player.objects.create_user(
            username="john_doe",
            first_name="John",
            last_name="Doe",
            password="password123",
            level=70,
            power=10000,
        )

    def setUp(self):
        # Log in as the admin user
        self.client.login(username="admin", password="password")

    def test_player_level_race_power_in_list_display(self):
        response = self.client.get(reverse("admin:players_player_changelist"))

        self.assertContains(response, "level")
        self.assertContains(response, "race")
        self.assertContains(response, "power")


    def test_player_level_race_power_in_edit_page(self):
        response = self.client.get(
            reverse("admin:players_player_change", args=[self.player.pk])
        )

        self.assertContains(response, "level")
        self.assertContains(response, "race")
        self.assertContains(response, "power")

    def test_player_level_race_power_in_add_page(self):
        response = self.client.get(reverse("admin:players_player_add"))

        self.assertContains(response, "level")
        self.assertContains(response, "race")
        self.assertContains(response, "power")

    def test_player_admin_class_registers_correctly(self):
        player_admin = site._registry.get(Player)
        self.assertIsNotNone(player_admin)

        expected_fields = (
            "username",
            "level",
            "race",
            "power",
        )
        for field in expected_fields:
            self.assertIn(field, player_admin.list_display)

        found_in_fieldsets = any(
            "level" or "race" or "power" in section[1]["fields"]
            for section in player_admin.fieldsets
        )
        self.assertTrue(
            found_in_fieldsets,
            "Field 'level' or 'race' or 'power' not found in fieldsets."
        )

        found_in_add_fieldsets = any(
            "level" or "race" or "power" in section[1]["fields"]
            for section in player_admin.add_fieldsets
        )
        self.assertTrue(
            found_in_add_fieldsets,
            "Field 'level' or 'race' or 'power' not found in add_fieldsets."
        )
