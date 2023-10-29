from django.db import migrations


def backup_data(apps, schema_editor):
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('oc_lettings_site', '0002_auto_20231029_1449'),
    ]

    operations = [
        migrations.RunPython(backup_data),
        # Supprimez les anciennes tables en utilisant migrations.DeleteModel
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='Letting',
        ),
    ]

