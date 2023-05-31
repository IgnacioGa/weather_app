from django.test import TestCase
from django.urls import reverse
import re


# Create your tests here.
class TestWeatherApi(TestCase):
    def setUp(self):
        self.headers = {"HTTP_HX-Request": "true"}

    def test_get_info_correct(self):
        """Test the function to get the information from the weather api"""
        response = self.client.get(reverse("weather:api_get"), {"q": "new york"}, **self.headers)
        html_container = re.findall('class="city"', str(response.content))
        assert response.status_code == 200
        assert len(html_container) == 1
        assert "response" in response.context
        assert "city" in response.context
        assert "id" in response.context
        assert "new_york" in response.context.get("id")
        # Check if the city is in the session
        assert "new york" in self.client.session.get("cities")

    def test_delete_city(self):
        """Test delete a city in the session"""
        self.client.get(reverse("weather:api_get"), {"q": "new york"}, **self.headers)
        self.client.delete(reverse("weather:api_get_detail", kwargs={"city": "new york"}), **self.headers)
        assert "new york" not in self.client.session.get("cities")

    def test_clear_session(self):
        """Test clear session on reload"""
        self.client.get(reverse("weather:api_get"), {"q": "new york"}, **self.headers)
        assert "cities" in self.client.session
        self.client.post(reverse("weather:clear_session"))
        assert "cities" not in self.client.session
