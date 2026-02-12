from django.db import models
from apps.core.models import BaseModel, ImageModel

# 1. Banner
class BannerSettings(BaseModel):
    """Banner sozlamalari"""
    show_video = models.BooleanField(default=False, verbose_name="Video ko'rsatish")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "1. Banner sozlamasi"
        verbose_name_plural = "1. Banner sozlamalari"

    def __str__(self):
        return "Banner sozlamalari"

    def save(self, *args, **kwargs):
        if self.is_active:
            BannerSettings.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class BannerVideo(BaseModel):
    """Banner video"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Qo'shimcha sarlavha")
    video_file = models.FileField(upload_to='banners/videos/', verbose_name="Video fayl (MP4)")
    poster_image = models.ImageField(upload_to='banners/posters/', blank=True, null=True, verbose_name="Poster rasm")

    button_text = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, blank=True, verbose_name="Tugma havolasi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "1. Banner Video"
        verbose_name_plural = "1. Banner Videolar"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            BannerVideo.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class BannerSlider(BaseModel, ImageModel):
    """Bosh sahifa banner slider"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Qo'shimcha sarlavha")
    description = models.TextField(blank=True, verbose_name="Tavsif")

    button_text = models.CharField(max_length=100, blank=True, verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, blank=True, verbose_name="Tugma havolasi")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "1. Banner Slider"
        verbose_name_plural = "1. Banner Sliderlar"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class BannerNavigation(BaseModel):
    """Banner pastidagi navigatsiya (Bakalavriat/Magistratura)"""
    title = models.CharField(max_length=100, verbose_name="Sarlavha")
    description = models.CharField(max_length=255, verbose_name="Tavsif")
    link = models.CharField(max_length=255, verbose_name="Havola")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Icon class")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "1. Banner Navigatsiya"
        verbose_name_plural = "1. Banner Navigatsiyalar"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def get_link(self):
        if not self.link:
            return '#'
        return self.link if self.link.startswith(('http://', 'https://', '/')) else f'/{self.link}'


# 2. About University
class AboutSection(BaseModel, ImageModel):
    """Universitet haqida section"""
    subtitle = models.CharField(max_length=255, verbose_name="Qo'shimcha sarlavha")
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    description_2 = models.TextField(blank=True, verbose_name="Tavsif 2")

    # Chap tarafdagi rasmlar
    left_image_1 = models.ImageField(upload_to='about/', verbose_name="Chap rasm 1")
    left_image_2 = models.ImageField(upload_to='about/', verbose_name="Chap rasm 2")

    # Aylanuvchi matn
    circle_text = models.CharField(max_length=255, verbose_name="Aylanuvchi matn")

    # Missiya
    mission_title = models.CharField(max_length=100, verbose_name="Missiya sarlavhasi")
    mission_icon = models.FileField(upload_to='icons/', blank=True, null=True, verbose_name="Missiya icon")

    # Viziya
    vision_title = models.CharField(max_length=100, verbose_name="Viziya sarlavhasi")
    vision_icon = models.FileField(upload_to='icons/', blank=True, null=True, verbose_name="Viziya icon")

    # Tugma
    button_text = models.CharField(max_length=100, verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, verbose_name="Tugma havolasi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "2. Universitet haqida"
        verbose_name_plural = "2. Universitet haqida"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.is_active:
            AboutSection.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


# 3. Statistic Item
class StatisticItem(BaseModel):
    """Statistika elementi"""
    title = models.CharField(max_length=100, verbose_name="Sarlavha (90%, Top 10, №1)")
    description = models.CharField(max_length=255, verbose_name="Tavsif")
    icon = models.CharField(max_length=100, blank=True, verbose_name="Icon class")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "3. Statistika bloki"
        verbose_name_plural = "3. Statistika bloki"
        ordering = ['order', 'title']

    def __str__(self):
        return f"{self.title} - {self.description[:30]}"


# 4. News Static Texts
class NewsStaticTexts(BaseModel):
    """Yangiliklar section static matnlari"""

    title = models.CharField(max_length=255, default="So'nggi yangiliklar", verbose_name="Sarlavha")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    button_text = models.CharField(max_length=100, default="Barchasini ko'rish", verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, default="/news/", verbose_name="Tugma havolasi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "4. Yangiliklar statik matnlari"
        verbose_name_plural = "4. Yangiliklar statik matnlari"

    def __str__(self):
        return "Yangiliklar section matnlari"

    def save(self, *args, **kwargs):
        if self.is_active:
            NewsStaticTexts.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()

# 5. Partner
class Partner(BaseModel):
    """Hamkor tashkilotlar logotipi"""
    name = models.CharField(max_length=255, verbose_name="Nomi")
    logo = models.FileField(upload_to='partners/', verbose_name="Logotip (SVG/PNG)")
    link = models.URLField(blank=True, verbose_name="Veb-sayt havolasi")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "5. Hamkor"
        verbose_name_plural = "5. Hamkorlar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


# 6. Litsenziya va Akkreditatsiya
class LicenseStaticTexts(BaseModel):
    """Litsenziya section statik matnlari"""
    title = models.CharField(max_length=255, default="Litsenziya va Akkreditatsiya", verbose_name="Sarlavha")
    button_text = models.CharField(max_length=100, default="Batafsil", verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, default="#", verbose_name="Tugma havolasi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "6. Litsenziya statik matnlari"
        verbose_name_plural = "6. Litsenziya statik matnlari"

    def __str__(self):
        return "Litsenziya section matnlari"

    def save(self, *args, **kwargs):
        if self.is_active:
            LicenseStaticTexts.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class LicenseItem(BaseModel):
    """Litsenziya/Akkreditatsiya elementi"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif")
    background_image = models.ImageField(upload_to='licenses/', verbose_name="Fon rasmi")
    button_text = models.CharField(max_length=100, default="Ko'rish", verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, default="#", verbose_name="Tugma havolasi")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "6. Litsenziya elementi"
        verbose_name_plural = "6. Litsenziya elementlari"
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


# 7. Ta'lim dasturlari
class ProgramStaticTexts(BaseModel):
    """Ta'lim dasturlari section statik matnlari"""
    title = models.CharField(max_length=255, default="Ta'lim dasturlari", verbose_name="Sarlavha")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "7. Ta'lim dasturlari statik matnlari"
        verbose_name_plural = "7. Ta'lim dasturlari statik matnlari"

    def __str__(self):
        return "Ta'lim dasturlari section matnlari"

    def save(self, *args, **kwargs):
        if self.is_active:
            ProgramStaticTexts.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


# 8. Talabalar hayoti
class StudentLifeStaticTexts(BaseModel):
    """Talabalar hayoti section statik matnlari"""
    title = models.CharField(max_length=255, default="Talabalar Hayoti", verbose_name="Sarlavha")
    title_highlight = models.CharField(max_length=100, default="Hayoti", verbose_name="Ajratilgan so'z (<span>)")
    description = models.TextField(blank=True, verbose_name="Tavsif")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "8. Talabalar hayoti statik matnlari"
        verbose_name_plural = "8. Talabalar hayoti statik matnlari"

    def __str__(self):
        return "Talabalar hayoti section matnlari"

    def save(self, *args, **kwargs):
        if self.is_active:
            StudentLifeStaticTexts.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class StudentLifeItem(BaseModel, ImageModel):
    """Talabalar hayoti elementi"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    link = models.CharField(max_length=255, default="#", verbose_name="Havola")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "8. Talabalar hayoti elementi"
        verbose_name_plural = "8. Talabalar hayoti elementlari"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


# 9. Yo'nalishlar
class DirectionStaticTexts(BaseModel):
    """Yo'nalishlar section statik matnlari"""
    title = models.CharField(max_length=255, default="Ta'lim yo'nalishlari", verbose_name="Sarlavha")
    button_text = models.CharField(max_length=100, default="Ko'proq yuklash", verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, default="/programs/", verbose_name="Tugma havolasi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "9. Yo'nalishlar statik matnlari"
        verbose_name_plural = "9. Yo'nalishlar statik matnlari"

    def __str__(self):
        return "Yo'nalishlar section matnlari"

    def save(self, *args, **kwargs):
        if self.is_active:
            DirectionStaticTexts.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


# 10. Tadbirlar
class EventStaticTexts(BaseModel):
    """Tadbirlar section statik matnlari"""
    title = models.CharField(max_length=255, default="Yaqinlashib kelayotgan tadbirlar", verbose_name="Sarlavha")
    button_text = models.CharField(max_length=100, default="Barchasini ko'rish", verbose_name="Tugma matni")
    button_link = models.CharField(max_length=255, default="/events/", verbose_name="Tugma havolasi")
    side_image = models.ImageField(upload_to='home/events/', blank=True, null=True, verbose_name="Yon tarafdagi rasm")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "10. Tadbirlar statik matnlari"
        verbose_name_plural = "10. Tadbirlar statik matnlari"

    def __str__(self):
        return "Tadbirlar section matnlari"

    def save(self, *args, **kwargs):
        if self.is_active:
            EventStaticTexts.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()