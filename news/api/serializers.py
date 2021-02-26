from rest_framework import serializers
from news.model import Article

class ArticleSerializer(serializers.Serializer):
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_data = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, validated_data):
        print(validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.title = validated_data.get('author', instance.title)
        instance.description = validated_data.get('author', instance.description)
        instance.body = validated_data.get('author', instance.body)
        instance.location = validated_data.get('author', instance.location)
        instance.published_data = validated_data.get('author', instance.publication_data)
        instance.description = validated_data.get('author', instance.description)
        instance.active = validated_data.get('author', instance.active)

        instance.save()
        return instance