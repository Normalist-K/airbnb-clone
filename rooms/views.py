from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import Http404
from . import models

# Create your views here.


class HomeView(ListView):  # 11.7

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "price"
    context_object_name = "rooms"


class RoomDetail(DetailView):  # 12.4

    """ RoomDetail Definition """

    model = models.Room


"""

Function Based View

def room_detail(request, pk):  # 12.0
    try:  # 12.2
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
        # raise Http404() # 12. 3

"""
