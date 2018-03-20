# Generated by Django 2.0.3 on 2018-03-17 17:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', model_utils.fields.StatusField(choices=[('waiting', 'waiting'), ('rejected', 'rejected'), ('refunded', 'refunded'), ('completed', 'completed'), ('error', 'error')], default='waiting', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('provider', model_utils.fields.StatusField(choices=[('waiting', 'waiting'), ('rejected', 'rejected'), ('refunded', 'refunded'), ('completed', 'completed'), ('error', 'error')], default='waiting', max_length=100, no_check_for_status=True, verbose_name='payment provider')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('currency', models.CharField(max_length=10, verbose_name='currency')),
                ('amount', models.DecimalField(decimal_places=2, default='0.0', max_digits=9, verbose_name='amount')),
                ('tax', models.DecimalField(decimal_places=2, default='0.0', max_digits=9, verbose_name='tax')),
                ('billing_first_name', models.CharField(blank=True, max_length=256, verbose_name='billing first name')),
                ('billing_last_name', models.CharField(blank=True, max_length=256, verbose_name='billing last name')),
                ('billing_address_1', models.CharField(blank=True, max_length=256, verbose_name='billing address 1')),
                ('billing_address_2', models.CharField(blank=True, max_length=256, verbose_name='billing address 2')),
                ('billing_city', models.CharField(blank=True, max_length=256, verbose_name='billing city')),
                ('billing_country_code', models.CharField(blank=True, max_length=2, verbose_name='billing country code')),
                ('billing_postcode', models.CharField(blank=True, max_length=256, verbose_name='billing postcode')),
                ('billing_country_area', models.CharField(blank=True, max_length=256, verbose_name='billing country area')),
                ('billing_email', models.EmailField(blank=True, max_length=254, verbose_name='billing email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StripePayment',
            fields=[
                ('payment_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='payments.Payment')),
                ('transaction_id', models.CharField(blank=True, help_text='Id of the transaction, if applicable', max_length=255, verbose_name='transaction id')),
            ],
            options={
                'abstract': False,
            },
            bases=('payments.payment',),
        ),
        migrations.AddField(
            model_name='payment',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_payments.payment_set+', to='contenttypes.ContentType'),
        ),
    ]