from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class LettingsTestCase(TestCase):
    def setUp(self):
        # Créez des objets Address et Letting pour les tests
        self.address = Address.objects.create(
            number=123,
            street="Main St",
            city="Lyon",
            state="EX",
            zip_code=12345,
            country_iso_code="EXM"
        )
        self.letting = Letting.objects.create(
            title="Example Letting",
            address=self.address
        )

    def test_index_view(self):
        url = reverse('lettings:index')
        response = self.client.get(url)
        # Vérifiez que la page renvoie un code de statut HTTP 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting.title)

    def test_letting_view(self):
        url = reverse('lettings:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        # Vérifiez que le contenu de la réponse contient le titre de la location
        self.assertContains(response, self.letting.title)
