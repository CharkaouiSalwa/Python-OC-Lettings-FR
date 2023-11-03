from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

def copy_data(apps, schema_editor):
    OldProfile = apps.get_model("oc_lettings_site", "Profile")
    Profile = apps.get_model("profiles", "Profile")
    for old_profile in OldProfile.objects.all():
        new_profile = Profile(
            user=old_profile.user,
            favorite_city=old_profile.favorite_city,
        )
        new_profile.save()



class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favorite_city', models.CharField(blank=True, max_length=64)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(copy_data),

    ]

