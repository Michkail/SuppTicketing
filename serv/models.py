from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class TicketStatus(models.TextChoices):
    TODO = 'Todo'
    IN_PROGRESS = 'In Progress'
    IN_REVIEW = 'In Review'
    DONE = 'Done'


class LocationChoices(models.TextChoices):
    NANGGROE_ACEH_DARUSSALAM = 'Nanggroe Aceh Darussalam'
    SUMATERA_UTARA = 'Sumatera Utara'
    SUMATERA_SELATAN = 'Sumatera Selatan'
    SUMATERA_BARAT = 'Sumatera Barat'
    BENGKULU = 'Bengkulu'
    RIAU = 'Riau'
    KEPULAUAN_RIAU = 'Kepulauan Riau'
    JAMBI = 'Jambi'
    LAMPUNG = 'Lampung'
    BANGKA_BELITUNG = 'Bangka Belitung'
    KALIMANTAN_BARAT = 'Kalimantan Barat'
    KALIMANTAN_TIMUR = 'Kalimantan Timur'
    KALIMANTAN_SELATAN = 'Kalimantan Selatan'
    KALIMANTAN_TENGAH = 'Kalimantan Tengah'
    KALIMANTAN_UTARA = 'Kalimantan Utara'
    BANTEN = 'Banten'
    JAKARTA = 'Jakarta'
    JAWA_BARAT = 'Jawa Barat'
    JAWA_TENGAH = 'Jawa Tengah'
    YOGYAKARTA = 'Yogyakarta'
    JAWA_TIMUR = 'Jawa Timur'
    BALI = 'Bali'
    NUSA_TENGGARA_TIMUR = 'Nusa Tenggara Timur'
    NUSA_TENGGARA_BARAT = 'Nusa Tenggara Barat'
    GORONTALO = 'Gorontalo'
    SULAWESI_BARAT = 'Sulawesi Barat'
    SULAWESI_TENGAH = 'Sulawesi Tengah'
    SULAWESI_UTARA = 'Sulawesi Utara'
    SULAWESI_TENGGARA = 'Sulawesi Tenggara'
    SULAWESI_SELATAN = 'Sulawesi Selatan'
    MALUKU_UTARA = 'Maluku Utara'
    MALUKU = 'Maluku'
    PAPUA_BARAT = 'Papua Barat'
    PAPUA = 'Papua'
    PAPUA_TENGAH = 'Papua Tengah'
    PAPUA_PEGUNUNGAN = 'Papua Pengungan'
    PAPUA_SELATAN = 'Papua Selatan'
    PAPUA_BARAT_DAYA = 'Papua Barat Daya'


class CategoryType(models.TextChoices):
    PURCHASING = 'Pembelian'
    SERVICE = 'Service'
    REPAIRMENT = 'Perbaikan'
    VISIT = 'Kunjungan'


class Ticket(models.Model):
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TODO)
    description = models.TextField()
    media = models.FileField(upload_to="media/", default=None, null=True)
    location = models.CharField(max_length=25, choices=LocationChoices.choices, default=LocationChoices.JAKARTA)
    categories = models.CharField(max_length=25, choices=CategoryType.choices, default=CategoryType.PURCHASING)
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)
