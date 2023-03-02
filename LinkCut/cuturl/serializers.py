from rest_framework import serializers

from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["id", "full_url", "cut_url"]
        read_only_fields = ("id",)


class CreateUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["id", "full_url"]
        read_only_fields = ("id",)

    def create(self, validated_data):
        return Url.objects.create(**validated_data)
