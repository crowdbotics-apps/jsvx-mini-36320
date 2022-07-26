# Generated by Django 2.2.26 on 2022-07-20 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company2', '0001_initial'),
        ('company1', '0001_initial'),
        ('company3', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firm_companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company1', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firm_companies_company1', to='company1.Company1')),
                ('company2', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firm_companies_company2', to='company2.Company2')),
                ('company3', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='firm_companies_company3', to='company3.Company3')),
            ],
        ),
    ]
