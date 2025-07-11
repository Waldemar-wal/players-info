from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from players.models import Player, EquipmentType, Equipment, Race


@admin.register(Player)
class PlayerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("level", "race", "power",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("level", "race", "power",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "level",
                        "race",
                        "power",
                    )
                },
            ),
        )
    )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ["name", "type", "description",]
    search_fields = ("name",)
    list_filter = ("type",)

admin.site.register(Race)
admin.site.register(EquipmentType)
