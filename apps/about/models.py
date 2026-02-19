from django.db import models
from apps.core.models import BaseModel, ImageModel


class Leader(BaseModel, ImageModel):
    """Universitet rahbariyati a'zosi"""
    full_name = models.CharField(max_length=255, verbose_name="F.I.O")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    position = models.CharField(max_length=255, verbose_name="Lavozim")
    degree = models.CharField(max_length=255, blank=True, verbose_name="Ilmiy daraja")

    short_bio = models.TextField(verbose_name="Qisqa ma'lumot")
    biography = models.TextField(blank=True, verbose_name="Biografiya")
    education = models.TextField(blank=True, verbose_name="Ma'lumoti")
    expertise = models.TextField(blank=True, verbose_name="Mutaxassislik sohalari")
    courses = models.TextField(blank=True, verbose_name="Darslar")
    publications = models.TextField(blank=True, verbose_name="Ilmiy nashrlari")

    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="Email")
    reception_days = models.CharField(max_length=255, blank=True, verbose_name="Qabul kunlari")

    facebook_link = models.URLField(blank=True, verbose_name="Facebook")
    linkedin_link = models.URLField(blank=True, verbose_name="LinkedIn")
    telegram_link = models.URLField(blank=True, verbose_name="Telegram")
    youtube_link = models.URLField(blank=True, verbose_name="YouTube")
    instagram_link = models.URLField(blank=True, verbose_name="Instagram")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Rahbar"
        verbose_name_plural = "Rahbariyat"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} - {self.position}"