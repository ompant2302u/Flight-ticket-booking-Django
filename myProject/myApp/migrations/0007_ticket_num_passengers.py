# Generated migration

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_flight_flight_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='num_passengers',
            field=models.IntegerField(default=1),
        ),
    ]
