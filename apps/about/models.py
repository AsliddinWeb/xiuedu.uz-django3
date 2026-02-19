from django.db import models
from apps.core.models import BaseModel, ImageModel


# 1. Breadcrumb
class AboutBreadcrumb(BaseModel):
    """About sahifa breadcrumb"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    parent_title = models.CharField(max_length=100, default="Bosh sahifa", verbose_name="Ota sahifa nomi")
    parent_link = models.CharField(max_length=255, default="/", verbose_name="Ota sahifa havolasi")
    background_image = models.ImageField(upload_to='about/breadcrumb/', verbose_name="Fon rasmi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "1. Breadcrumb"
        verbose_name_plural = "1. Breadcrumb"

    def __str__(self):
        return "About breadcrumb"

    def save(self, *args, **kwargs):
        if self.is_active:
            AboutBreadcrumb.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


# 2. Universitet haqida
class AboutUniversity(BaseModel, ImageModel):
    """Universitet haqida asosiy section"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")

    # Asosiy rasm (ImageModel dan keladi)

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "2. Universitet haqida"
        verbose_name_plural = "2. Universitet haqida"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            AboutUniversity.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class AboutStatistic(BaseModel):
    """Universitet haqida — o'ng tarafdagi statistika"""
    value = models.CharField(max_length=50, verbose_name="Qiymat (5 000+, 350+)")
    description = models.CharField(max_length=255, verbose_name="Tavsif")
    icon = models.FileField(upload_to='about/icons/', blank=True, null=True, verbose_name="Icon (SVG)")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "2. Statistika"
        verbose_name_plural = "2. Statistikalar"
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.description[:30]}"


# 3. Tarix
class AboutHistory(BaseModel, ImageModel):
    """Universitet tarixi section"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    content = models.TextField(verbose_name="Matn")
    content_2 = models.TextField(blank=True, verbose_name="Matn 2 (ikkinchi paragraf)")

    # Rasm ImageModel dan

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "3. Tarix"
        verbose_name_plural = "3. Tarix"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            AboutHistory.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


# 4. Funfact (statistika banneri)
class AboutFunfact(BaseModel):
    """Funfact elementi (95%, Top 10, №1)"""
    value = models.CharField(max_length=50, verbose_name="Qiymat")
    description = models.CharField(max_length=255, verbose_name="Tavsif")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "4. Funfact"
        verbose_name_plural = "4. Funfactlar"
        ordering = ['order']

    def __str__(self):
        return f"{self.value} - {self.description[:30]}"


# 5. Missiya va Qadriyatlar
class AboutMission(BaseModel):
    """Missiya section statik matnlari"""
    title = models.CharField(max_length=255, default="Missiya va Qadriyatlar", verbose_name="Sarlavha")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "5. Missiya sarlavhasi"
        verbose_name_plural = "5. Missiya sarlavhasi"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            AboutMission.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class AboutMissionItem(BaseModel, ImageModel):
    """Missiya elementi"""

    class Side(models.TextChoices):
        LEFT = 'left', "Chap"
        RIGHT = 'right', "O'ng"

    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    side = models.CharField(max_length=10, choices=Side.choices, default=Side.LEFT, verbose_name="Joylashuv")

    # Rasm ImageModel dan

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "5. Missiya elementi"
        verbose_name_plural = "5. Missiya elementlari"
        ordering = ['order']

    def __str__(self):
        return self.title


# 6. Kampus sayohati
class AboutCampusTour(BaseModel):
    """Kampus sayohati section"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    video_url = models.URLField(verbose_name="Video havolasi (YouTube)")
    video_thumbnail = models.ImageField(upload_to='about/campus/', verbose_name="Video poster rasmi")
    button_text = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, blank=True, verbose_name="Tugma havolasi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "6. Kampus sayohati"
        verbose_name_plural = "6. Kampus sayohati"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            AboutCampusTour.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


# 7. Rahbariyat
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
        verbose_name = "7. Rahbar"
        verbose_name_plural = "7. Rahbariyat"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} - {self.position}"