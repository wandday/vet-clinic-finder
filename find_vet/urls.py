from django.contrib import admin
from django.urls import path, include
from find_vet.views import FindView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', FindView.as_view(), name='find_api'),
    path('index', views.index, name='index'),
    path('find', views.find, name='find'),
    ]