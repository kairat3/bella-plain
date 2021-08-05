from rest_framework import serializers
from .models import Product, Category,  Favorite, Bag, Color, Size, Additional


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.children.exists():
            representation['children'] = CategorySerializer(instance=instance.children.all(), many=True).data
        return representation


class AdditionalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Additional
        fields = ('key', 'value', )


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ('id', 'color', )


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('id', 'size', )


class ProductSerializer(serializers.ModelSerializer):
    additional = AdditionalSerializer(many=True)
    color = ColorSerializer(many=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'preview', 'additional', 'color', )


class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = ('id', 'favorite', 'user', )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        review = Favorite.objects.create(user=user, **validated_data)
        return review

    def to_representation(self, instance):
        representation = super(FavoriteSerializer, self).to_representation(instance)
        representation['user'] = instance.user.email
        return representation


class BagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = ('id', 'in_bag', 'quantity', 'product')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        bag = Bag.objects.create(user=user, **validated_data)
        return bag

    def to_representation(self, instance):
        representation = super(BagSerializer, self).to_representation(instance)
        representation['user'] = instance.user.phone_number
        return representation


class BagCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bag
        fields = ('quantity', 'product', )

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        bag = Bag.objects.create(user=user, **validated_data)
        return bag

    def validate(self, attrs):
        return attrs
