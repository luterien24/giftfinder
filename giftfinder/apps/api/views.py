import os

from django.shortcuts import render
from django.conf import settings

from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from apps.items.models import Item, Tag, Category, Recipient, Occasion, Store, Like
from apps.items.serializers import ItemSerializer, TagSerializer, CategorySerializer, RecipientSerializer, OccasionSerializer, \
                StoreSerializer, LikeSerializer

from apps.items.gift_finder import GiftManager

## TEST_MODE

def backup(request):
    import requests
    import json
    import datetime

    r = requests.get("http://dunyayidegistir.com/api/1.0/")

    dx = json.loads(r.content)

    nw = datetime.datetime.now()
    date_key = nw.day + nw.month + nw.year + nw.hour + nw.minute + nw.second

    for k, v in dx.items():

        r = requests.get(v)

        key = k + "." + str(date_key)
        
        file_path = os.path.join(settings.PROJECT_DIR + key)

        f = open(file_path, "w")
        f.write(r.content)
        f.close()

    tmp = """Backup created = {{ date_key }}"""

    ctx = {
        "date_key" : date_key
    }

    return render(request, tmp, ctx)



@api_view(['GET', 'POST'])
def find_gift(request):
    """ gift finder """
    if request.method == "POST":
        try:
            data = request.POST
            interests = data.getlist("interests", [])
            categories = data.getlist("categories", [])
            recipients = data.getlist("recipients", [])
            min_age, max_age = tuple(data.get("age", "-").split("-"))
            sex = data.get("sex", "both")
            items = Item.objects.filter(tags__name__in=interests)

            item_serializer = ItemSerializer(items, many=True, context={"request":request})

            return Response(item_serializer.data)
        except Exception as e:
            print "ERROR !!! - ", str(e)
    elif request.method == "GET":
        try:
            data = request.GET
            print "request.GET : ", request.GET
            print "interests : ", data.getlist("interests", [])
            interests = data.getlist("interests", [])
            categories = data.getlist("categories", [])
            recipients = data.getlist("recipients", [])
            min_age, max_age = tuple(data.get("age", "-").split("-"))
            sex = data.get("sex", "both")


            items = Item.objects.filter(sex=sex)

            if interests:
                items = items.filter(tags__name__in=interests)

            if categories:
                item = items.filter(category__name__in=categories)

            if recipients:
                item = items.filter(recipients__name__in=recipients)

            if min_age and max_age:
                items = items.filter(min_age__lte=min_age, max_age__gte=max_age)


            item_serializer = ItemSerializer(items, many=True, context={"request":request})

            return Response(item_serializer.data)
        except Exception as e:
            print "ERROR !!! - ", str(e)
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
    url = "http://127.0.0.1:8000/api/find_gift/?recipients=arkadas&interests=Futbol&interests=Internet&interests=Yemek&categories=Yiyecek"
    data = {
        "recipients" : ["arkadas",],
        "categories" : ["Yetiskinler icin", "Yiyecek"],
        "interests" : ["Futbol", "Internet", "Bilgisayar", "Yemek"]
    }

    r = requests.get(url)

    raise Exception(r.content)



