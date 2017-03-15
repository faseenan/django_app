from django.conf.urls import url
from telefun import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]