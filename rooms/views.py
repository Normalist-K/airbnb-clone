# from mate import ceil
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView
from . import models

# Create your views here.


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "price"
    context_object_name = "rooms"


# Using paginator
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")


# Manual Coding
# def all_rooms(request):
# page = int(request.GET.get("page", 1))
# page_size = 10
# limit = page_size * page
# offset = limit - page_size
# all_rooms = models.Room.objects.all()[offset:limit]
# page_count = ceil(models.Room.objects.count() / page_size)
# page_range = range(1, page_count + 1)
# return render(
#     request,
#     "rooms/home.html",
#     {
#         "rooms": all_rooms,
#         "page": page,
#         "page_count": page_count,
#         "page_range": page_range,
#     },
# )
