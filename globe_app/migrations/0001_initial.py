# Generated by Django 3.2.5 on 2022-07-22 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locationName', models.TextField(unique=True)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='ForumPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TravelNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('travelPics', models.ImageField(blank=True, upload_to='travelPics')),
                ('destination', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='globe_app.destination')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('middle_name', models.CharField(blank=True, max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('age', models.IntegerField()),
                ('description', models.TextField(blank=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non Binary'), ('PNTD', 'Prefer not to say')], max_length=4)),
                ('picture', models.ImageField(blank=True, upload_to='profilePics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UpcomingTravel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateStart', models.DateField()),
                ('dateEnd', models.DateField()),
                ('budgetStart', models.DecimalField(decimal_places=2, max_digits=6)),
                ('budgetEnd', models.DecimalField(decimal_places=2, max_digits=6)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globe_app.destination')),
                ('owner', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='globe_app.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='TravelWishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globe_app.destination')),
                ('travelNotes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globe_app.travelnote')),
            ],
        ),
        migrations.CreateModel(
            name='TravelHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelPics', models.ImageField(blank=True, upload_to='travelPics')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globe_app.destination')),
                ('travelNotes', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='globe_app.travelnote')),
            ],
            options={
                'verbose_name_plural': 'TravelHistories',
            },
        ),
        migrations.CreateModel(
            name='PostReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globe_app.forumpost')),
            ],
            options={
                'verbose_name_plural': 'PostReplies',
            },
        ),
    ]