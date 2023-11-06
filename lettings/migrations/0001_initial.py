import django.core.validators
from django.db import migrations, models
import django.db.models.deletion

def copy_data(apps, schema_editor):
    # Copiez les données de l'ancienne base de données vers la nouvelle
    #OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldAddress = apps.get_model("lettings", "Address")
    Address = apps.get_model("lettings", "Address")
    for old_address in OldAddress.objects.all():
        new_address = Address(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        new_address.save()

    #OldLetting = apps.get_model("oc_lettings_site", "Letting")
    OldLetting = apps.get_model("lettings", "Letting")
    Letting = apps.get_model("lettings", "Letting")
    for old_letting in OldLetting.objects.all():
        new_letting = Letting(
            title=old_letting.title,
            address=Address.objects.get(id=old_letting.address.id),
        )
        new_letting.save()



class Migration(migrations.Migration):
    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
                ('street', models.CharField(max_length=64)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=2, validators=[django.core.validators.MinLengthValidator(2)])),
                ('zip_code', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('country_iso_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.CreateModel(
            name='Letting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lettings.Address')),
            ],
        ),
        migrations.RunPython(copy_data),
    ]
