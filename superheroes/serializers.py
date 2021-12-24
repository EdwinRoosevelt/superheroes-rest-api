from rest_framework import serializers


class SuperHeroesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
