from django.shortcuts import render
from django.views import generic
from .models import Note
from django.urls import reverse


def HomeView(request):
    note_list = Note.objects.all()
    context = {'notes': note_list}

    return render(request, 'notes/home.html', context)


class NoteDetailView(generic.DetailView):
    model = Note
    template_name = 'notes/note_detail.html'


class NoteCreateView(generic.CreateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'notes/note_create.html'

    def get_success_url(self):
        return reverse('home')


class NoteUpdateView(generic.UpdateView):
    model = Note
    fields = ['title', 'text']
    template_name = 'notes/note_update.html'


class NoteDeleteView(generic.DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'

    def get_success_url(self):
        return reverse('home')
