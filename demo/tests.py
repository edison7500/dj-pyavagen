from django.test import TestCase
from django.urls import reverse


class PyAvagenViewTestCase(TestCase):
    def setUp(self) -> None:
        pass

    def test_avatar_generate_view(self):
        url = reverse("pyavagen:generator", args=[300, "Trump"])

        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
