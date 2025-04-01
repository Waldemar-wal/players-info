from django.urls import path

from .views import (
    home_page,
    EquipmentListView,
    EquipmentDetailView,
    EquipmentCreateView,
    EquipmentUpdateView,
    EquipmentDeleteView,
    PlayerListView,
    PlayerDetailView,
    PlayerCreateView,
    PlayerDeleteView,
    PlayerPowerAndLevelUpdateView,
    EquipmentTypeListView,
    EquipmentTypeCreateView,
    EquipmentTypeUpdateView,
    EquipmentTypeDeleteView,
    RaceDeleteView,
    RaceUpdateView,
    RaceCreateView,
    RaceListView,
    # toggle_assign_to_equipment,
    AssignToEquipment,
)




urlpatterns = [
    path("", home_page, name="home_page"),
    path(
        "races/",
        RaceListView.as_view(),
        name="race-list",
    ),
    path(
        "races/create/",
        RaceCreateView.as_view(),
        name="race-create",
    ),
    path(
        "races/<int:pk>/update/",
        RaceUpdateView.as_view(),
        name="race-update",
    ),
    path(
        "races/<int:pk>/delete/",
        RaceDeleteView.as_view(),
        name="race-delete",
    ),
    path(
        "equipment-types/",
        EquipmentTypeListView.as_view(),
        name="equipment-type-list",
    ),
    path(
        "equipment-types/create/",
        EquipmentTypeCreateView.as_view(),
        name="equipment-type-create",
    ),
    path(
        "equipment-types/<int:pk>/update/",
        EquipmentTypeUpdateView.as_view(),
        name="equipment-type-update",
    ),
    path(
        "equipment-types/<int:pk>/delete/",
        EquipmentTypeDeleteView.as_view(),
        name="equipment-type-delete",
    ),
    path("equipments/", EquipmentListView.as_view(), name="equipment-list"),
    path(
        "equipments/<int:pk>/toggle-assign/",
        AssignToEquipment.as_view(),
        name="toggle-assign-to-equipment",
    ),
    path(
        "equipments/<int:pk>/",
        EquipmentDetailView.as_view(),
        name="equipment-detail"
    ),
    path(
        "equipments/create/",
        EquipmentCreateView.as_view(),
        name="equipment-create"
    ),
    path(
        "equipments/<int:pk>/update/",
        EquipmentUpdateView.as_view(),
        name="equipment-update"
    ),
    path(
        "equipments/<int:pk>/delete/",
        EquipmentDeleteView.as_view(),
        name="equipment-delete"
    ),
    path("players/", PlayerListView.as_view(), name="player-list"),
    path(
        "players/<int:pk>/", PlayerDetailView.as_view(), name="player-detail"
    ),
    path("players/", PlayerListView.as_view(), name="player-list"),
    path(
        "players/<int:pk>/", PlayerDetailView.as_view(), name="player-detail"
    ),
    path(
        "players/create/", PlayerCreateView.as_view(), name="player-create"
    ),
    path(
        "players/<int:pk>/update/",
        PlayerPowerAndLevelUpdateView.as_view(),
        name="player-update",
    ),
    path(
        "players/<int:pk>/delete/",
        PlayerDeleteView.as_view(),
        name="player-delete",
    ),
]

app_name = "players"
