from django.shortcuts import render, get_object_or_404, redirect
from trips.models import Trip, Destination, Comment
from django.forms import modelform_factory


def landing_page(request):
    posts = Trip.objects.all()
    destinations = Destination.objects.values_list("country", flat=True).distinct()
    return render(
        request, "landing_page.html", {"posts": posts, "destinations": destinations}
    )


CommentForm = modelform_factory(Comment, fields=["name", "text"])


def detail_page(request, pk: int):
    post = get_object_or_404(Trip, pk=pk)
    destinations = Destination.objects.values_list("country", flat=True).distinct()
    return render(
        request,
        "detail.html",
        {
            "post": post,
            "destinations": destinations,
            "comment_form": CommentForm(),
        },
    )


def comment(request, pk: int):
    trip = get_object_or_404(Trip, pk=pk)
    if request.method == "POST":
        form = CommentForm(data=request.POST, initial={"trip_id": trip.id})
        if form.is_valid():
            form.instance.trip = trip
            form.save()
    return redirect("trip_detail", pk=pk)
