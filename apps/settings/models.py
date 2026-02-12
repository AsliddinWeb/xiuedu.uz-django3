from django.db import models
from apps.core.models import BaseModel


class SiteSettings(BaseModel):
    """Sayt asosiy sozlamalari"""
    site_name = models.CharField(max_length=255, verbose_name="Sayt nomi")
    site_description = models.TextField(verbose_name="Sayt tavsifi")
    site_keywords = models.TextField(blank=True, verbose_name="Kalit so'zlar")

    # Logolar
    logo = models.FileField(upload_to='logos/', verbose_name="Asosiy logo")
    logo_white = models.FileField(upload_to='logos/', verbose_name="Oq logo", blank=True, null=True)
    logo_dark = models.FileField(upload_to='logos/', blank=True, null=True, verbose_name="Qora logo")
    favicon = models.FileField(upload_to='logos/', verbose_name="Favicon")

    # Aloqa ma'lumotlari
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    phone_2 = models.CharField(max_length=20, blank=True, verbose_name="Telefon 2")
    email = models.EmailField(verbose_name="Email")
    email_2 = models.EmailField(blank=True, verbose_name="Email 2")

    address = models.TextField(verbose_name="Manzil")
    work_time = models.CharField(max_length=255, blank=True, verbose_name="Ish vaqti")

    # Xarita
    map_iframe = models.TextField(blank=True, verbose_name="Google Maps iframe")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Kenglik")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Uzunlik")

    # Copyright
    copyright_text = models.CharField(max_length=255, blank=True, verbose_name="Copyright matni")

    # SEO
    google_analytics = models.TextField(blank=True, verbose_name="Google Analytics kodi")
    yandex_metrika = models.TextField(blank=True, verbose_name="Yandex Metrika kodi")
    facebook_pixel = models.TextField(blank=True, verbose_name="Facebook Pixel kodi")

    # Faol holat
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Sayt sozlamasi"
        verbose_name_plural = "Sayt sozlamalari"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        if self.is_active:
            SiteSettings.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        """Faol sozlamani qaytarish"""
        return cls.objects.filter(is_active=True).first()


class SocialNetwork(BaseModel):
    """Ijtimoiy tarmoqlar"""
    name = models.CharField(max_length=50, verbose_name="Nomi")
    url = models.CharField(verbose_name="Havola")
    icon = models.CharField(max_length=100, verbose_name="Icon class")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class HeaderSettings(BaseModel):
    """Header sozlamalari"""
    # Banner matn
    banner_text = models.CharField(max_length=255, blank=True, verbose_name="Banner matni")
    banner_link = models.CharField(blank=True, verbose_name="Banner havolasi")
    show_banner = models.BooleanField(default=False, verbose_name="Bannerni ko'rsatish")

    # Header button
    show_header_button = models.BooleanField(default=True, verbose_name="Header tugmasini ko'rsatish")
    button_text = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni")
    button_link = models.CharField(blank=True, verbose_name="Tugma havolasi")

    # Qidiruv
    show_search = models.BooleanField(default=True, verbose_name="Qidiruvni ko'rsatish")

    # Til
    show_language_switcher = models.BooleanField(default=True, verbose_name="Til almashtirgichni ko'rsatish")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Header sozlamasi"
        verbose_name_plural = "Header sozlamalari"

    def __str__(self):
        return "Header sozlamalari"

    def save(self, *args, **kwargs):
        if self.is_active:
            HeaderSettings.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class HeaderMenu(BaseModel):
    """Header menyu elementi"""
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='children',
        verbose_name="Asosiy menyu"
    )

    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    url = models.CharField(max_length=255, blank=True, verbose_name="URL / Havola")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Icon class")

    # Mega menu uchun
    is_mega_menu = models.BooleanField(default=False, verbose_name="Mega menu")
    description = models.TextField(blank=True, verbose_name="Tavsif (Mega menu uchun)")
    image = models.ImageField(upload_to='menu/', blank=True, null=True, verbose_name="Rasm (Mega menu uchun)")

    # Badge
    show_badge = models.BooleanField(default=False, verbose_name="Badge ko'rsatish")
    badge_text = models.CharField(max_length=50, blank=True, verbose_name="Badge matni")
    badge_color = models.CharField(max_length=7, default='#FF0000', verbose_name="Badge rangi")

    # Sozlamalar
    open_new_tab = models.BooleanField(default=False, verbose_name="Yangi oynada ochish")
    css_class = models.CharField(max_length=100, blank=True, verbose_name="CSS class")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Header menyu"
        verbose_name_plural = "Header menyular"
        ordering = ['order', 'title']

    def __str__(self):
        if self.parent:
            return f"{self.parent.title} -> {self.title}"
        return self.title

    def get_children(self):
        """Bolalar menyularni qaytarish"""
        return self.children.filter(is_active=True).order_by('order')

    def has_children(self):
        """Bolalar menyu borligini tekshirish"""
        return self.children.filter(is_active=True).exists()

    def get_url(self):
        """URL ni qaytarish"""
        if not self.url:
            return '#'
        return self.url if self.url.startswith(('http://', 'https://', '/')) else f'/{self.url}'

    @property
    def level(self):
        """Menyu darajasini aniqlash"""
        level = 0
        parent = self.parent
        while parent:
            level += 1
            parent = parent.parent
        return level


class FooterSettings(BaseModel):
    """Footer sozlamalari"""
    # Footer haqida
    about_title = models.CharField(max_length=255, blank=True, verbose_name="Haqida sarlavhasi")
    about_text = models.TextField(blank=True, verbose_name="Haqida matni")

    # Newsletter
    show_newsletter = models.BooleanField(default=True, verbose_name="Newsletter ko'rsatish")
    newsletter_title = models.CharField(max_length=255, blank=True, verbose_name="Newsletter sarlavhasi")
    newsletter_description = models.TextField(blank=True, verbose_name="Newsletter tavsifi")

    # So'nggi yangiliklar
    show_recent_news = models.BooleanField(default=True, verbose_name="So'nggi yangiliklar ko'rsatish")
    recent_news_count = models.PositiveIntegerField(default=2, verbose_name="So'nggi yangiliklar soni")

    # Footer pastki qism
    show_copyright = models.BooleanField(default=True, verbose_name="Copyright ko'rsatish")
    show_payment_icons = models.BooleanField(default=False, verbose_name="To'lov tizimlarini ko'rsatish")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Footer sozlamasi"
        verbose_name_plural = "Footer sozlamalari"

    def __str__(self):
        return "Footer sozlamalari"

    def save(self, *args, **kwargs):
        if self.is_active:
            FooterSettings.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class FooterCategoryMenu(BaseModel):
    """Footer kategoriya menu (ustunlar)"""
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Footer kategoriya menu"
        verbose_name_plural = "Footer kategoriya menyular"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_menu_items(self):
        """Kategoriya ichidagi menyularni qaytarish"""
        return self.menu_items.filter(is_active=True).order_by('order')


class FooterMenuItem(BaseModel):
    """Footer menu elementi"""
    category = models.ForeignKey(
        FooterCategoryMenu,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name="Kategoriya"
    )

    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    url = models.CharField(max_length=255, verbose_name="URL")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Icon class")

    open_new_tab = models.BooleanField(default=False, verbose_name="Yangi oynada ochish")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Footer menu elementi"
        verbose_name_plural = "Footer menu elementlari"
        ordering = ['category', 'order', 'title']

    def __str__(self):
        return f"{self.category.title} - {self.title}"

    def get_url(self):
        """URL ni qaytarish"""
        if not self.url:
            return '#'
        return self.url if self.url.startswith(('http://', 'https://', '/')) else f'/{self.url}'