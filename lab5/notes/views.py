from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note
import os
from .serializers import (
    CreateNoteResponseSerializer,
    NoteTextResponseSerializer,
    NoteInfoResponseSerializer,
    NoteListResponseSerializer
)

TOKENS_FILE = os.path.join(os.path.dirname(__file__), "tokens.txt")


def check_token(token):
    with open(TOKENS_FILE, "r") as file:
        tokens = {line.strip() for line in file}
    if token not in tokens:
        return False
    return True


class CreateNoteView(APIView):
    def post(self, request):
        token = request.query_params.get('token')
        if not check_token(token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_403_FORBIDDEN)

        text = request.data.get("text", "")
        note = Note.objects.create(text=text)
        serializer = CreateNoteResponseSerializer(note)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class NoteDetailView(APIView):
    def get(self, request, note_id):
        token = request.query_params.get('token')
        if not check_token(token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_403_FORBIDDEN)

        try:
            note = Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteTextResponseSerializer(note)
        return Response(serializer.data)

    def patch(self, request, note_id):
        token = request.query_params.get('token')
        if not check_token(token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_403_FORBIDDEN)

        try:
            note = Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        note.text = request.data.get("text", note.text)
        note.save()
        serializer = NoteTextResponseSerializer(note)
        return Response(serializer.data)

    def delete(self, request, note_id):
        token = request.query_params.get('token')
        if not check_token(token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_403_FORBIDDEN)

        try:
            note = Note.objects.get(id=note_id)
            note.delete()
            return Response({"detail": "Note deleted"}, status=status.HTTP_200_OK)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)


class NoteInfoView(APIView):
    def get(self, request, note_id):
        token = request.query_params.get('token')
        if not check_token(token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_403_FORBIDDEN)

        try:
            note = Note.objects.get(id=note_id)
        except Note.DoesNotExist:
            return Response({"detail": "Note not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = NoteInfoResponseSerializer(note)
        return Response(serializer.data)


class ListNotesView(APIView):
    def get(self, request):
        token = request.query_params.get('token')
        if not check_token(token):
            return Response({"detail": "Invalid token"}, status=status.HTTP_403_FORBIDDEN)

        notes = Note.objects.values_list('id', flat=True)
        note_dict = {i: note_id for i, note_id in enumerate(notes)}
        serializer = NoteListResponseSerializer({"notes": note_dict})
        return Response(serializer.data)
