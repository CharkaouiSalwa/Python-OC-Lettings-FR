from django.test import TestCase
from django.urls import reverse
from .models import Profile


class ProfilesViewTestCase(TestCase):
    def setUp(self):
        # Créez des données de test pour vos profils
        self.profile1 = Profile.objects.create(user__username="user1",
                                               name="User One", email="user1@example.com")
        self.profile2 = Profile.objects.create(user__username="user2",
                                               name="User Two", email="user2@example.com")

    def test_index_view(self):
        # Testez la vue 'index'
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['profiles_list'],
                                 ['<Profile: User One>', '<Profile: User Two>'])

    def test_profile_view(self):
        # Testez la vue 'profile' pour un utilisateur existant
        response = self.client.get(reverse('profiles:profile', args=[self.profile1.user.username]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['profile'], self.profile1)

    def test_profile_view_nonexistent_user(self):
        # Testez la vue 'profile' pour un utilisateur inexistant
        response = self.client.get(reverse('profiles:profile', args=['nonexistentuser']))
        self.assertEqual(response.status_code, 404)
