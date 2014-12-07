from rest_framework import serializers

from apps.items.models import Item, Tag, Category, Recipient, Occasion, Store, Like

class GiftFinderSerializer(serializers.Serializer):

    pass




class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category

class RecipientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipient

class OccasionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Occasion

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Store

class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Like

