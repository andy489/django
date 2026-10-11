from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from meetings.models import Meeting, Room


def detail(request, id):
  # meeting = Meeting.objects.get(pk=id)
  meeting = get_object_or_404(Meeting, pk=id)
  return render(request, "meetings/detail.html",
                {"meeting": meeting})


def room_list(request):
  return render(request, "meetings/room_list.html",
                {"rooms": Room.objects.all()})


MeetingForm = modelform_factory(Meeting, fields="__all__")


def new(request):
  if request.method == "POST":
    form = MeetingForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("welcome")
  else:
    form = MeetingForm()
  return render(request, "meetings/new.html",
                {"form": form})


def edit(request, id):
  meeting = get_object_or_404(Meeting, pk=id)
  if request.method == "POST":
    form = MeetingForm(request.POST, instance=meeting)
    if form.is_valid():
      form.save()
      return redirect("detail", id=id)
  else:
    form = MeetingForm(instance=meeting)
  return render(request, "meetings/edit.html",
                {"form": form})


def delete(request, id):
  meeting = get_object_or_404(Meeting, pk=id)
  if request.method == "POST":
    # Form is only shown to ask for confirmation
    # When we get a POST, we know we can go ahead and delete
    meeting.delete()
    return redirect("welcome")
  else:
    return render(request, "meetings/confirm_delete.html",
                  {"meeting": meeting})
