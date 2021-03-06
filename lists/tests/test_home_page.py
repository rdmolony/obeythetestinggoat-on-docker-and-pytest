from django.test.client import Client
from django.urls import resolve

import pytest
from pytest_django.asserts import assertTemplateUsed

from lists.models import Item
from lists.views import home_page


@pytest.mark.django_db
def test_returns_correct_html(client: Client) -> None:
    response = client.get("/")

    html = response.content.decode("utf8")
    assert html.startswith("<html>")
    assert "<title>To-Do lists</title>" in html
    assert html.endswith("</html>")


@pytest.mark.django_db
def test_uses_home_template(client: Client) -> None:
    response = client.get("/")
    assertTemplateUsed(response, "home.html")
