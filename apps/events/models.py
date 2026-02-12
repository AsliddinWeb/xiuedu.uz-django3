from django.db import models
from apps.core.models import BaseModel, ImageModel


class Event(BaseModel, ImageModel):
    """Tadbir"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Tavsif")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Qisqa tavsif")

    # Sana va vaqt
    event_date = models.DateField(verbose_name="Tadbir sanasi")
    event_time = models.TimeField(blank=True, null=True, verbose_name="Boshlanish vaqti")
    end_time = models.TimeField(blank=True, null=True, verbose_name="Tugash vaqti")

    # Narx va o'rinlar
    cost = models.DecimalField(max_digits=12, decimal_places=0, default=0, verbose_name="Narxi (so'm)")
    is_free = models.BooleanField(default=False, verbose_name="Bepulmi?")
    total_slots = models.PositiveIntegerField(default=0, verbose_name="Jami o'rinlar soni")
    booked_slots = models.PositiveIntegerField(default=0, verbose_name="Band qilingan o'rinlar")

    # Tugma
    button_text = models.CharField(max_length=100, default="Ro'yxatdan o'tish", verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, blank=True, verbose_name="Tugma havolasi")

    # Joy ma'lumotlari
    venue_name = models.CharField(max_length=255, blank=True, verbose_name="Joy nomi")
    venue_address = models.TextField(blank=True, verbose_name="Manzil")
    venue_phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon raqami")
    venue_website = models.URLField(blank=True, verbose_name="Veb-sayt")
    venue_map_embed = models.TextField(blank=True, verbose_name="Google Maps iframe kodi")

    # Ijtimoiy tarmoqlar
    facebook_link = models.URLField(blank=True, verbose_name="Facebook")
    instagram_link = models.URLField(blank=True, verbose_name="Instagram")
    linkedin_link = models.URLField(blank=True, verbose_name="LinkedIn")
    telegram_link = models.URLField(blank=True, verbose_name="Telegram")
    youtube_link = models.URLField(blank=True, verbose_name="YouTube")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")
    is_featured = models.BooleanField(default=False, verbose_name="Tanlangan")

    class Meta:
        verbose_name = "Tadbir"
        verbose_name_plural = "Tadbirlar"
        ordering = ['-event_date', '-created_at']

    def __str__(self):
        return self.title

    def get_formatted_cost(self):
        if self.is_free:
            return "Bepul"
        if self.cost:
            return f"{self.cost:,.0f} so'm".replace(',', ' ')
        return "Belgilanmagan"

    def available_slots(self):
        if self.total_slots:
            return self.total_slots - self.booked_slots
        return 0

    @property
    def is_fully_booked(self):
        return self.total_slots > 0 and self.booked_slots >= self.total_slots


class EventFeature(BaseModel):
    """Tadbir xususiyati (Interactive Workshops, Networking va h.k.)"""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='features', verbose_name="Tadbir")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Tadbir xususiyati"
        verbose_name_plural = "Tadbir xususiyatlari"
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.event.title} - {self.title}"