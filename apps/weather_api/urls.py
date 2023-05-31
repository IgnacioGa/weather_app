from django.urls import path

from . import views


app_name = "weather"

urlpatterns = [
    path("", views.Weather.as_view(), name="index"),
    path("clear_session", views.clear_session, name="clear_session"),
    path("api_get", views.WeatherApi.as_view(), name="api_get"),
    path("api_get_detail/<str:city>", views.WeatherDetailApi.as_view(), name="api_get_detail"),
    path("city_information", views.WeatherCity.as_view(), name="city_information"),
]
