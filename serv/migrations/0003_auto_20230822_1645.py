# Generated by Django 3.2.5 on 2023-08-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0002_auto_20230811_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='provider',
            field=models.CharField(default=None, max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='categories',
            field=models.CharField(choices=[('Pembelian', 'Purchasing'), ('Service', 'Service'), ('Perbaikan', 'Repairment'), ('Kunjungan', 'Visit')], default='Pembelian', max_length=25),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='location',
            field=models.CharField(choices=[('Nanggroe Aceh Darussalam', 'Nanggroe Aceh Darussalam'), ('Sumatera Utara', 'Sumatera Utara'), ('Sumatera Selatan', 'Sumatera Selatan'), ('Sumatera Barat', 'Sumatera Barat'), ('Bengkulu', 'Bengkulu'), ('Riau', 'Riau'), ('Kepulauan Riau', 'Kepulauan Riau'), ('Jambi', 'Jambi'), ('Lampung', 'Lampung'), ('Bangka Belitung', 'Bangka Belitung'), ('Kalimantan Barat', 'Kalimantan Barat'), ('Kalimantan Timur', 'Kalimantan Timur'), ('Kalimantan Selatan', 'Kalimantan Selatan'), ('Kalimantan Tengah', 'Kalimantan Tengah'), ('Kalimantan Utara', 'Kalimantan Utara'), ('Banten', 'Banten'), ('Jakarta', 'Jakarta'), ('Jawa Barat', 'Jawa Barat'), ('Jawa Tengah', 'Jawa Tengah'), ('Yogyakarta', 'Yogyakarta'), ('Jawa Timur', 'Jawa Timur'), ('Bali', 'Bali'), ('Nusa Tenggara Timur', 'Nusa Tenggara Timur'), ('Nusa Tenggara Barat', 'Nusa Tenggara Barat'), ('Gorontalo', 'Gorontalo'), ('Sulawesi Barat', 'Sulawesi Barat'), ('Sulawesi Tengah', 'Sulawesi Tengah'), ('Sulawesi Utara', 'Sulawesi Utara'), ('Sulawesi Tenggara', 'Sulawesi Tenggara'), ('Sulawesi Selatan', 'Sulawesi Selatan'), ('Maluku Utara', 'Maluku Utara'), ('Maluku', 'Maluku'), ('Papua Barat', 'Papua Barat'), ('Papua', 'Papua'), ('Papua Tengah', 'Papua Tengah'), ('Papua Pengungan', 'Papua Pegunungan'), ('Papua Selatan', 'Papua Selatan'), ('Papua Barat Daya', 'Papua Barat Daya')], default='Jakarta', max_length=25),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('In Progress', 'In Progress'), ('In Review', 'In Review'), ('Done', 'Done')], default='Todo', max_length=25),
        ),
    ]
