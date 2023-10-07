# Generated by Django 3.2.5 on 2023-08-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0003_auto_20230822_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('contact', models.IntegerField(max_length=13)),
                ('location', models.CharField(choices=[('Nanggroe Aceh Darussalam', 'Nanggroe Aceh Darussalam'), ('Sumatera Utara', 'Sumatera Utara'), ('Sumatera Selatan', 'Sumatera Selatan'), ('Sumatera Barat', 'Sumatera Barat'), ('Bengkulu', 'Bengkulu'), ('Riau', 'Riau'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Jambi', 'Jambi'), ('Lampung', 'Lampung'), ('Bangka Belitung', 'Bangka Belitung'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Banten', 'Banten'), ('Jakarta', 'Jakarta'), ('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('Yogyakarta', 'Yogyakarta'), ('Jawa Timur', 'Jawa Timur'), ('Bali', 'Bali'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Gorontalo', 'Gorontalo'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Sulawesi Tenggara', 'Sulawesi Tenggara'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Maluku Utara', 'Maluku Utara'), ('Maluku', 'Maluku'), ('Papua Barat', 'Papua Barat'), ('Papua', 'Papua'), ('Papua Tengah', 'Papua Tengah'), ('Papua Pengungan', 'Papua Pegunungan'), ('Papua Selatan', 'Papua Selatan'), ('Papua Barat Daya', 'Papua Barat Daya')], default='Jakarta', max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='ContactRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=25)),
                ('contact', models.IntegerField(max_length=13)),
                ('address', models.TextField()),
                ('maps', models.URLField(blank=True)),
                ('id_customer', models.CharField(max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
            ],
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='provider',
        ),
    ]
