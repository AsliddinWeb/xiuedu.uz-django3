from django.db import models
from django.conf import settings
from apps.core.models import BaseModel, ImageModel


class NewsCategory(BaseModel):
    """Yangilik kategoriyasi"""
    name = models.CharField(max_length=255, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class NewsTag(BaseModel):
    """Yangilik tegi"""
    name = models.CharField(max_length=100, verbose_name="Nomi")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Teg"
        verbose_name_plural = "Teglar"
        ordering = ['name']

    def __str__(self):
        return self.name


class News(BaseModel, ImageModel):
    """Yangilik"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    category = models.ForeignKey(NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='news', verbose_name="Kategoriya")
    tags = models.ManyToManyField(NewsTag, blank=True, related_name='news', verbose_name="Teglar")

    image = models.ImageField(upload_to='news/', verbose_name="Asosiy rasm")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Qisqa tavsif")
    content = models.TextField(verbose_name="Kontent")

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='news', verbose_name="Muallif")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Nashr sanasi")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")
    is_featured = models.BooleanField(default=False, verbose_name="Tanlangan")

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])


class NewsImage(BaseModel):
    """Yangilik qo'shimcha rasmi"""
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='images', verbose_name="Yangilik")
    image = models.ImageField(upload_to='news/images/', verbose_name="Rasm")
    alt_text = models.CharField(max_length=255, blank=True, verbose_name="Alt matn")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")

    class Meta:
        verbose_name = "Yangilik rasmi"
        verbose_name_plural = "Yangilik rasmlari"
        ordering = ['order']

    def __str__(self):
        return self.alt_text or f"Rasm #{self.pk}"


class NewsComment(BaseModel):
    """Yangilikka izoh"""

    class Status(models.TextChoices):
        PENDING = 'pending', "Kutilmoqda"
        APPROVED = 'approved', "Tasdiqlangan"
        REJECTED = 'rejected', "Rad etilgan"

    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments', verbose_name="Yangilik")
    name = models.CharField(max_length=255, verbose_name="Ism")
    phone = models.CharField(max_length=50, verbose_name="Telefon raqami")
    subject = models.CharField(max_length=255, blank=True, verbose_name="Mavzu")
    message = models.TextField(verbose_name="Xabar")

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING, verbose_name="Holati")

    class Meta:
        verbose_name = "Izoh"
        verbose_name_plural = "Izohlar"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.news.title[:30]}"