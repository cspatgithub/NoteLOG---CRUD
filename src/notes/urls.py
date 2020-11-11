from django.urls import path
from .views import HomeView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('', HomeView, name='home'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note-detail'),
    path('note/create', NoteCreateView.as_view(), name='note-create'),
    path('note/<int:pk>/update', NoteUpdateView.as_view(), name='note-update'),
    path('note/<int:pk>/delete', NoteDeleteView.as_view(), name='note-delete'),
]