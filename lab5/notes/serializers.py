from rest_framework import serializers
from .models import Note


class CreateNoteResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id']


class NoteTextResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'text']


class NoteInfoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['created_at', 'updated_at']


class NoteListResponseSerializer(serializers.Serializer):
    notes = serializers.DictField(child=serializers.IntegerField())
