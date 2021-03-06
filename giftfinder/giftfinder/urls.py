from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from apps.api.views import ItemViewSet, TagViewSet, CategoryViewSet, RecipientViewSet, \
        OccasionViewSet, StoreViewSet, LikeViewSet, find_gift, tester, backup

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'recipients', RecipientViewSet)
router.register(r'occasions', OccasionViewSet)
router.register(r'stores', StoreViewSet)
router.register(r'likes', LikeViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'presentpicker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/1.0/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/find_gift/$', find_gift),
    url(r'^yedekle/$', backup),

    url(r'^runtests/$', tester),

    # custom
    url(r'^accounts/', include('apps.profiles.urls')),

    # static
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
)
