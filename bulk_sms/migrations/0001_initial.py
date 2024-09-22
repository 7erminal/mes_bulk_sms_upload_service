# Generated by Django 3.1.6 on 2024-09-19 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type', models.IntegerField(blank=True, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('username', models.CharField(blank=True, max_length=40, null=True)),
                ('image_path', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateTimeField()),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('id_type', models.CharField(blank=True, max_length=5, null=True)),
                ('id_number', models.CharField(blank=True, max_length=100, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=20, null=True)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('is_verified', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserTypes',
            fields=[
                ('user_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_type_name', models.CharField(max_length=255)),
                ('user_type_description', models.CharField(max_length=255)),
                ('active', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('date_modified', models.DateTimeField(blank=True, null=True)),
                ('created_by', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Campaigns',
            fields=[
                ('campaignId', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=200, null=True)),
                ('scheduledTime', models.CharField(blank=True, max_length=200, null=True)),
                ('recipient_file', models.FileField(blank=True, null=True, upload_to='recipients')),
                ('recipient_number', models.CharField(blank=True, max_length=200, null=True)),
                ('recipient_email', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.IntegerField(default=0)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_setup_by', to='bulk_sms.users')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_authorized_by', to='bulk_sms.users')),
            ],
        ),
    ]
