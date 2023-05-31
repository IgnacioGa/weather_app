from django.views.generic import TemplateView, DeleteView
from django.shortcuts import render
from django.http import JsonResponse
from .constants import WEATHER_GIFS, ERRORS

from django.conf import settings

from django.views.decorators.http import require_http_methods

import requests
import json


class TemplateMixin(TemplateView):
    def setup(self, request, *args, **kwargs):
        """
        Setup if the request is htmx
        """
        super().setup(request, *args, **kwargs)
        self.is_htmx = request.headers.get("HX-Request") == "true"

    def trigger_error_response(self, message):
        """
        Send error response
        """
        return JsonResponse({"message": message}, status=400)


class Weather(TemplateMixin):
    template_name = "weather/index.html"


class WeatherApi(TemplateMixin):
    template_name = "weather/city.html"

    def get(self, *args, **kwargs):
        if self.is_htmx:
            city_name = self.request.GET.get("q")

            if "cities" not in self.request.session.keys():
                self.request.session["cities"] = []

            if city_name in self.request.session["cities"]:
                return self.trigger_error_response("The city is already in the list")

            response = requests.get(
                f"{settings.WEATHER_API_BASE_URL}?access_key={settings.WEATHER_API_ACCESS_KEY}&query={city_name}"
            )
            response_json = response.json()

            if "error" in response_json.keys():
                error_code = response_json.get("error").get("code")
                error_message = ERRORS[error_code]
                return self.trigger_error_response(error_message)

            self.request.session["cities"].append(city_name)
            self.request.session.save()

            context = {
                "response": json.dumps(response_json),
                "city": city_name,
                "id": city_name.replace(" ", "_").replace(",", "_"),
            }
            return render(self.request, "weather/city.html", context)
        return super().get(*args, **kwargs)


class WeatherDetailApi(DeleteView):
    def delete(self, request, *args, **kwargs):
        self.request.session["cities"].remove(kwargs.get("city"))
        self.request.session.save()
        return JsonResponse({}, status=204)


class WeatherCity(TemplateMixin):
    template_name = "weather/information.html"

    def get(self, *args, **kwargs):
        if self.is_htmx:
            city_info = json.loads(self.request.GET.get("city_info"))
            try:
                city_info["gif"] = WEATHER_GIFS[city_info.get("current").get("weather_descriptions")[0]]
            except KeyError:
                city_info["gif"] = "sunny.svg"

            context = {"response": city_info}
            return render(self.request, "weather/information.html", context)
        return super().get(*args, **kwargs)


@require_http_methods(["POST"])
def clear_session(request):
    if "cities" in request.session.keys():
        del request.session["cities"]
        request.session.save()
    return JsonResponse({}, status=204)
