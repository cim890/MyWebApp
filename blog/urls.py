from django.conf.urls import url
from django.views.generic import RedirectView
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    #Regular Expression r'regularExprsHere'
    # /blog/
    url(r'^$', views.index, name='index'),
    # /blog/[IDBlog]/
    url(r'^(?P<idpost>[0-9]+)/$', views.blogdetail, name='blogdetail'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/admin/img/favicon.ico')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)