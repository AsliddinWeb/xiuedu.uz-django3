from django.db import models
from apps.core.models import BaseModel


class GalleryImage(BaseModel):
    """Galereya rasmi"""
    title = models.CharField(max_length=255, blank=True, verbose_name="Sarlavha")
    image = models.ImageField(upload_to='gallery/', verbose_name="Rasm")
    image_large = models.ImageField(upload_to='gallery/large/', blank=True, null=True, verbose_name="Katta rasm (lightbox)")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")
    is_featured = models.BooleanField(default=False, verbose_name="Bosh sahifada ko'rsatish")

    class Meta:
        verbose_name = "Galereya rasmi"
        verbose_name_plural = "Galereya rasmlari"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title or f"Rasm #{self.pk}"

    def get_large_url(self):
        if self.image_large:
            return self.image_large.url
        return self.image.url