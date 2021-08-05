from rest_framework import serializers
from info.models import About, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('title', 'image', )


class AboutUsSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ('logo', 'desc', 'desc2', 'images', )