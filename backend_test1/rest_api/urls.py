# rest_api/urls.py 

from django.urls import path, include 
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView

from . import views

urlpatterns = {
    path('auth/', include('rest_framework.urls',
                            namespace = 'rest_framework')),
    path('servants/', views.CreateView.as_view(), name = 'summon'),
    path('servants/<int:pk>', views.DetailsView.as_view(), name = 'stats')
}

urlpatterns = format_suffix_patterns(urlpatterns)