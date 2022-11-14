from django.shortcuts import render
from django.http import JsonResponse
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers 

# Create your views here.

@api_view(['GET', 'POST'])
def artiste_list(request, format=None):

    if request.method == 'GET':
        artistes = Artiste.objects.all()
        serializer = ArtisteSerializer(artistes, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ArtisteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['GET', 'POST'])
def song_list(request, format=None):

    if request.method == 'GET':
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def lyric_list(request, format=None):

    if request.method == 'GET':
        lyrics = Lyric.objects.all()
        serializer = LyricSerializer(lyrics, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = LyricSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'Put', 'DELETE'])
def song_detail(request, id, format=None):

    try:
        songs = Song.objects.get(pk=id)
    except Song.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SongSerializer(songs)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SongSerializer(songs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        songs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)