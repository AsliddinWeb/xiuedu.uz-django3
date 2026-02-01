from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom User model"""
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Telefon")
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', blank=True, null=True, verbose_name="Avatar")
    birth_date = models.DateField(blank=True, null=True, verbose_name="Tug'ilgan sana")
    address = models.TextField(blank=True, null=True, verbose_name="Manzil")
    
    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['-date_joined']
    
    def __str__(self):
        return self.get_full_name() or self.username