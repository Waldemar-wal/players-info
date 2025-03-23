from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import (
    PlayerCreationForm,
    PlayerPowerAndLevelUpdateForm,
    EquipmentForm,
    EquipmentNameSearchForm,
    PlayerUsernameSearchForm,
    RaceNameSearchForm,
    EquipmentTypeNameSearchForm
)
from .models import Player, Equipment, EquipmentType, Race


@login_required
def home_page(request):
    """View function for the home page of the site."""

    num_players = Player.objects.count()
    num_races = Race.objects.count()
    num_equipments = Equipment.objects.count()
    num_equipment_types = EquipmentType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_players": num_players,
        "num_races": num_races,
        "num_equipments": num_equipments,
        "num_equipment_types": num_equipment_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "players/home_page.html", context=context)


class EquipmentTypeListView(LoginRequiredMixin, generic.ListView):
    model = EquipmentType
    context_object_name = "equipment_type_list"
    template_name = "players/equipment_type_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EquipmentTypeListView, self).get_context_data(**kwargs)

        context["search_form"] = EquipmentTypeNameSearchForm()
        type = self.request.GET.get("type", "")

        context["search_form"] = EquipmentTypeNameSearchForm(initial={"type": type})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        type = self.request.GET.get("type", "")

        if type:
            queryset = queryset.filter(type__icontains=type)

        return queryset


class EquipmentTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = EquipmentType
    fields = "__all__"
    success_url = reverse_lazy("players:equipment-type-list")
    template_name = "players/equipment_type_form.html"


class EquipmentTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = EquipmentType
    fields = "__all__"
    success_url = reverse_lazy("players:equipment-type-list")
    template_name = "players/equipment_type_form.html"


class EquipmentTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = EquipmentType
    success_url = reverse_lazy("players:equipment-type-list")
    template_name = "players/equipment_type_confirm_delete.html"


class RaceListView(LoginRequiredMixin, generic.ListView):
    model = Race
    context_object_name = "race_list"
    template_name = "players/race_list.html"
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RaceListView, self).get_context_data(**kwargs)

        context["search_form"] = RaceNameSearchForm()
        name = self.request.GET.get("name", "")

        context["search_form"] = RaceNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name", "")

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class RaceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Race
    fields = "__all__"
    success_url = reverse_lazy("players:race-list")


class RaceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Race
    fields = "__all__"
    success_url = reverse_lazy("players:race-list")


class RaceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Race
    success_url = reverse_lazy("players:race-list")


class EquipmentListView(LoginRequiredMixin, generic.ListView):
    model = Equipment
    paginate_by = 5
    queryset = Equipment.objects.select_related("type")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EquipmentListView, self).get_context_data(**kwargs)

        context["search_form"] = EquipmentNameSearchForm()
        name = self.request.GET.get("name", "")

        context["search_form"] = EquipmentNameSearchForm(initial={"name": name})
        return context

    def get_queryset(self):
        queryset = Equipment.objects.select_related("type")
        name= self.request.GET.get("name", "")

        if name:
            queryset = queryset.filter(name__icontains=name)

        queryset = queryset.order_by("name")

        return queryset



class EquipmentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Equipment


class EquipmentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Equipment
    form_class = EquipmentForm
    success_url = reverse_lazy("players:equipment-list")


class EquipmentUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Equipment
    form_class = EquipmentForm
    success_url = reverse_lazy("players:equipment-list")


class EquipmentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Equipment
    success_url = reverse_lazy("players:equipment-list")


class PlayerListView(LoginRequiredMixin, generic.ListView):
    model = Player
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PlayerListView, self).get_context_data(**kwargs)

        context["search_form"] = PlayerUsernameSearchForm()
        username = self.request.GET.get("Username", "")

        context["search_form"] = PlayerUsernameSearchForm(initial={"username": username})
        return context

    def get_queryset(self):
        queryset = Player.objects.select_related("race")
        username= self.request.GET.get("username", "")

        if username:
            queryset = queryset.filter(username__icontains=username)

        queryset = queryset.order_by("username")

        return queryset


class PlayerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Player
    queryset = Player.objects.all().prefetch_related("equipments__type")


class PlayerCreateView(generic.CreateView):
    model = Player
    form_class = PlayerCreationForm


class PlayerPowerAndLevelUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Player
    form_class = PlayerPowerAndLevelUpdateForm
    success_url = reverse_lazy("players:player-list")


class PlayerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Player
    success_url = reverse_lazy("")


@login_required
def toggle_assign_to_equipment(request, pk):
    player = Player.objects.get(id=request.user.id)
    if (
        Equipment.objects.get(id=pk) in player.equipments.all()
    ):  # probably could check if car exists
        player.equipments.remove(pk)
    else:
        player.equipments.add(pk)
    return HttpResponseRedirect(reverse_lazy("players:equipment-detail", args=[pk]))
