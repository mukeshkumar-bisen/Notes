# views.py
from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteRetrieveUpdate(generics.RetrieveUpdateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# views.py (continued)
from rest_framework import generics
from django.db.models import Q

class QueryNoteByTitle(generics.ListAPIView):
    serializer_class = NoteSerializer

    def get_queryset(self):
        title_substring = self.request.query_params.get('title', '')
        return Note.objects.filter(title__icontains=title_substring)
