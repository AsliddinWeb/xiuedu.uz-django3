from django.db import models


class BaseModel(models.Model):
    """Barcha modellar uchun asosiy abstract model"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqt")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgartirilgan vaqt")

    class Meta:
        abstract = True
        ordering = ['-created_at']


class SlugModel(models.Model):
    """Slug uchun abstract model"""
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")

    class Meta:
        abstract = True


class PublishedModel(models.Model):
    """Nashr qilish uchun abstract model"""
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")
    published_at = models.DateTimeField(null=True, blank=True, verbose_name="Nashr qilingan vaqt")

    class Meta:
        abstract = True


class ImageModel(models.Model):
    """Rasm uchun abstract model"""
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name="Rasm", blank=True, null=True)
    image_alt_uz = models.CharField(max_length=255, verbose_name="Rasm alt (O'zbekcha)", blank=True)
    image_alt_ru = models.CharField(max_length=255, verbose_name="Rasm alt (Ruscha)", blank=True)
    image_alt_en = models.CharField(max_length=255, verbose_name="Rasm alt (Inglizcha)", blank=True)

    class Meta:
        abstract = True

    def get_image_alt(self, lang='uz'):
        """Til bo'yicha rasm alt qaytarish"""
        return getattr(self, f'image_alt_{lang}', '')


class ViewCountModel(models.Model):
    """Ko'rishlar soni uchun abstract model"""
    view_count = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")

    class Meta:
        abstract = True

    def increment_view_count(self):
        """Ko'rishlar sonini oshirish"""
        self.view_count += 1
        self.save(update_fields=['view_count'])


class OrderModel(models.Model):
    """Tartib raqami uchun abstract model"""
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        abstract = True
        ordering = ['order', '-created_at']