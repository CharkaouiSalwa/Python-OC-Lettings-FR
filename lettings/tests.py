from django.test import TestCase
from lettings.models import Address, Letting
from django.urls import reverse

class LettingsTestCase(TestCase):
    def setUp(self):
        # Créez des objets Address et Letting pour les tests
        self.Address = Address.objects.create(
            number=123,
            street="Main St",
            city="Lyon",
            state="EX",
            zip_code=12345,
            country_iso_code="EXM"
        )
        self.Letting = Letting.objects.create(
            title="Example Letting",
            address=self.address
        )

    def test_letting_view(self):
        # Testez la vue  letting en utilisant l'URL correspondante
        url = reverse('lettings:letting', args=(self.letting.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting.title)
        self.assertContains(response, str(self.address))

    def test_index_view(self):
        # Testez la vue index
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.letting.title)
