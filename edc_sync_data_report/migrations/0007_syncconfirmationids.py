# Generated by Django 3.2.11 on 2022-04-17 17:55

import _socket
from django.db import migrations, models
import django.db.models.deletion
import django_revision.revision_field
import edc_base.model_fields.hostname_modification_field
import edc_base.model_fields.userfield
import edc_base.model_fields.uuid_auto_field
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('edc_sync_data_report', '0006_syncsite_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncConfirmationIds',
            fields=[
                ('created', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('modified', models.DateTimeField(blank=True, default=edc_base.utils.get_utcnow)),
                ('user_created', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model_fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', edc_base.model_fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('primary_key', models.CharField(max_length=100, unique=True, verbose_name='Model object id')),
                ('app_label', models.CharField(max_length=100, verbose_name='App label')),
                ('model_name', models.CharField(max_length=200, verbose_name='Model Name')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Ceated date')),
                ('data_collection_date', models.DateField(blank=True, null=True, verbose_name='Data collection date')),
                ('is_synced', models.BooleanField(blank=True, null=True)),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='sites.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
