from dataclasses import field
from rest_framework import serializers
from .models import Article,Art,Img,Related

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model= Article
        fields = [
            'article_id',
            'article_order',
            'content',
            'img_url',
            'related_art'
        ]

class ArtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Art
        fields=[
            'title',
            'cover',
            'content',
            'art_id'
        ]

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model=Img
        fields=[
            'url',
            'art_id'
        ]

class RelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model= Related
        fields=[
            'url',
            'art_id'
        ]