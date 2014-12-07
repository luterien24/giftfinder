from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.items.models import Item, Tag, Category, Recipient, Occasion, Store, Like
from apps.items.serializers import ItemSerializer, TagSerializer, CategorySerializer, RecipientSerializer, OccasionSerializer, \
                StoreSerializer, LikeSerializer

from apps.items.gift_finder import GiftManager

@api_view(['GET', 'POST'])
def find_gift(request):
    """ gift finder """
    if request.method == "POST":

        interests = request.POST.get("interests", [])
        categories = request.POST.get("categories", [])
        recipients = request.POST.get("recipients", [])
        min_age, max_age = tuple(request.POST.get("age", "-").split("-"))
        sex = request.POST.get("sex", "both")

        items = Item.objects.filter(tags__name__in=interests, category__name__in=categories, 
            recipients__name__in=recipients)

        return Response(items)
    elif request.method == "GET":
        return Response({'hey':'hey'})
    else:
        return Response("No such method.")


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_fields = ("id",)



class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ("id",)



class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_fields = ("id",)



class RecipientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    filter_fields = ("id",)



class OccasionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializer
    filter_fields = ("id",)



class StoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    filter_fields = ("id",)


class LikeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filter_fields = ("id",)


def tester(request):
    """
        test code
    """
    import requests
    url = "http://127.0.0.1:8000/api/find_gift/"
    data = {
        "recipients" : ["arkadas",],
        "categories" : ["Yetiskinler icin"],
        "interests" : ["Futbol", "Internet", "Bilgisayar"]
    }

    r = requests.post(url, data=data)

    raise Exception(r.content)



