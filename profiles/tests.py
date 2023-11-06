from django.test import TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth.models import User


class ProfilesViewTestCase(TestCase):
    def setUp(self):
        # Créez des données de test pour vos profils
        self.user1 = User.objects.create(username="user1", email="user1@example.com")
        self.profile1 = Profile.objects.create(user=self.user1, favorite_city="City One")

        self.user2 = User.objects.create(username="user2", email="user2@example.com")
        self.profile2 = Profile.objects.create(user=self.user2, favorite_city="City Two")

    def test_index_view(self):
        # Testez la vue 'index'
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        expected_profiles = ['<Profile: user1>', '<Profile: user2>']
        actual_profiles = list(response.context['profiles_list'].order_by('user__username'))
        self.assertQuerysetEqual(actual_profiles, expected_profiles)

    def test_profile_view(self):
        # Testez la vue 'profile' pour un utilisateur existant (User 1)
        response = self.client.get(reverse('profiles:profile', args=[self.user1.username]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['profile'], self.profile1)
