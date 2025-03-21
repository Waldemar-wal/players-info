from django.test import TestCase

from players.models import Race, Player, Equipment, EquipmentType


class TestModels(TestCase):

    def setUp(self):
        self.race = Race.objects.create(
            name="Elf",
        )

        self.player = Player.objects.create_user(
            username="john_doe",
            first_name="John",
            last_name="Doe",
            password="password123",
            level=70,
            power=10000,
            race=self.race,
        )

        self.equipment_type = EquipmentType.objects.create(
            type="weapon"
        )

        self.equipment = Equipment.objects.create(
            name="Axe",
            description="50dmg, 3kg",
            type=self.equipment_type,
        )

    def test_race_str(self):
        self.assertEqual(
            str(self.race),
            self.race.name,
        )

    def test_equipment_str(self):
        self.assertEqual(
            str(self.equipment),
            f"{self.equipment.name}({self.equipment.type.type}): "
            f"{self.equipment.description}"
        )

    def test_equipment_type_str(self):
        self.assertEqual(
            str(self.equipment_type),
            self.equipment_type.type

        )

    def test_player_str(self):
        self.assertEqual(
            str(self.player),
            (f"Player: {self.player.username}, race:{self.player.race.name}, "
             f"level: {self.player.level}, power: {self.player.power}")
        )
