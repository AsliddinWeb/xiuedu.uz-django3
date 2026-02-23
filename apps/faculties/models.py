from django.db import models
from apps.core.models import BaseModel, ImageModel


# 1. Fakultet
class Faculty(BaseModel, ImageModel):
    """Fakultet"""
    name = models.CharField(max_length=255, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Qisqa tavsif")

    # Dekan xabari
    dean_message_title = models.CharField(max_length=255, blank=True, verbose_name="Dekan xabari sarlavhasi")
    dean_message = models.TextField(blank=True, verbose_name="Dekan xabari")

    # Missiya va Viziya
    mission = models.TextField(blank=True, verbose_name="Missiya")
    vision = models.TextField(blank=True, verbose_name="Viziya")
    mission_image = models.ImageField(upload_to='faculties/mission/', blank=True, null=True, verbose_name="Missiya rasmi")

    # Dekan
    dean_full_name = models.CharField(max_length=255, verbose_name="Dekan F.I.O")
    dean_photo = models.ImageField(upload_to='faculties/deans/', blank=True, null=True, verbose_name="Dekan rasmi")
    dean_degree = models.CharField(max_length=255, blank=True, verbose_name="Ilmiy daraja")
    dean_phone = models.CharField(max_length=50, blank=True, verbose_name="Dekan telefoni")
    dean_email = models.EmailField(blank=True, verbose_name="Dekan emaili")
    dean_bio = models.TextField(blank=True, verbose_name="Dekan haqida")
    dean_reception_days = models.CharField(max_length=255, blank=True, verbose_name="Qabul kunlari")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Fakultet"
        verbose_name_plural = "Fakultetlar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


# 2. Kafedra
class Department(BaseModel, ImageModel):
    """Kafedra"""
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments', verbose_name="Fakultet")
    name = models.CharField(max_length=255, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Kafedra tarixi")

    # Kafedra mudiri
    head_full_name = models.CharField(max_length=255, verbose_name="Mudir F.I.O")
    head_photo = models.ImageField(upload_to='faculties/department_heads/', blank=True, null=True, verbose_name="Mudir rasmi")
    head_degree = models.CharField(max_length=255, blank=True, verbose_name="Ilmiy daraja")
    head_rank = models.CharField(max_length=255, blank=True, verbose_name="Ilmiy unvon")
    head_phone = models.CharField(max_length=50, blank=True, verbose_name="Mudir telefoni")
    head_email = models.EmailField(blank=True, verbose_name="Mudir emaili")
    head_bio = models.TextField(blank=True, verbose_name="Mudir haqida")
    head_reception_days = models.CharField(max_length=255, blank=True, verbose_name="Qabul kunlari")
    head_address = models.CharField(max_length=500, blank=True, verbose_name="Manzil")

    # Ilmiy faoliyat
    scientific_activity = models.TextField(blank=True, verbose_name="Ilmiy faoliyat")

    # Xalqaro hamkorlik
    international_cooperation = models.TextField(blank=True, verbose_name="Xalqaro hamkorlik")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Kafedra"
        verbose_name_plural = "Kafedralar"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.faculty.name} - {self.name}"


# 3. Xodim (o'qituvchi va ishchi xodimlar)
class Staff(BaseModel):
    """O'qituvchi yoki ishchi xodim"""

    class StaffType(models.TextChoices):
        TEACHER = 'teacher', "O'qituvchi"
        EMPLOYEE = 'employee', "Ishchi xodim"

    # Tegishlilik (kafedra yoki bo'lim)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_members', verbose_name="Kafedra")
    division = models.ForeignKey('Division', on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_members', verbose_name="Bo'lim")

    staff_type = models.CharField(max_length=20, choices=StaffType.choices, default=StaffType.TEACHER, verbose_name="Xodim turi")

    full_name = models.CharField(max_length=255, verbose_name="F.I.O")
    photo = models.ImageField(upload_to='faculties/staff/', blank=True, null=True, verbose_name="Rasm")
    position = models.CharField(max_length=255, verbose_name="Lavozim")
    degree = models.CharField(max_length=255, blank=True, verbose_name="Ilmiy daraja")
    phone = models.CharField(max_length=50, blank=True, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="Email")
    bio = models.TextField(blank=True, verbose_name="Biografiya")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Xodim"
        verbose_name_plural = "Xodimlar"
        ordering = ['order', 'full_name']

    def __str__(self):
        return f"{self.full_name} - {self.position}"


# 4. Bo'lim
class Division(BaseModel, ImageModel):
    """Bo'lim (Moliya, Kadrlar, IT va h.k.)"""
    name = models.CharField(max_length=255, verbose_name="Nomi")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Tavsif")

    # Bo'lim boshlig'i
    head_full_name = models.CharField(max_length=255, verbose_name="Boshliq F.I.O")
    head_photo = models.ImageField(upload_to='faculties/division_heads/', blank=True, null=True, verbose_name="Boshliq rasmi")
    head_degree = models.CharField(max_length=255, blank=True, verbose_name="Ilmiy daraja")
    head_phone = models.CharField(max_length=50, blank=True, verbose_name="Boshliq telefoni")
    head_email = models.EmailField(blank=True, verbose_name="Boshliq emaili")
    head_bio = models.TextField(blank=True, verbose_name="Boshliq haqida")
    head_reception_days = models.CharField(max_length=255, blank=True, verbose_name="Qabul kunlari")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


# 5. Ta'lim yo'nalishi (home section 7 uchun ham ishlatiladi)
class EducationLevel(BaseModel):
    """Ta'lim darajasi (Bakalavriat, Magistratura, Uzluksiz ta'lim)"""
    name = models.CharField(max_length=255, verbose_name="Nomi")
    background_image = models.ImageField(upload_to='faculties/levels/', verbose_name="Fon rasmi")
    style_class = models.CharField(max_length=50, blank=True, verbose_name="CSS class (masalan: v__2)")

    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Ta'lim darajasi"
        verbose_name_plural = "Ta'lim darajalari"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Program(BaseModel, ImageModel):
    """Ta'lim yo'nalishi"""
    education_level = models.ForeignKey(EducationLevel, on_delete=models.CASCADE, related_name='programs', verbose_name="Ta'lim darajasi")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='programs', verbose_name="Fakultet")
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='programs', verbose_name="Kafedra")

    name = models.CharField(max_length=255, verbose_name="Yo'nalish nomi")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Slug")
    code = models.CharField(max_length=50, blank=True, verbose_name="Yo'nalish kodi (60110300)")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    short_description = models.CharField(max_length=500, blank=True, verbose_name="Qisqa tavsif")

    language = models.CharField(max_length=100, blank=True, verbose_name="O'qitish tili")
    employment_rate = models.CharField(max_length=50, blank=True, verbose_name="Ish bilan ta'minlanish (%)")
    accreditation = models.CharField(max_length=255, blank=True, verbose_name="Akkreditatsiya")

    link = models.CharField(max_length=255, blank=True, verbose_name="Havola")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib")
    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Ta'lim yo'nalishi"
        verbose_name_plural = "Ta'lim yo'nalishlari"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.education_level.name} - {self.name}"

    def get_link(self):
        if self.link:
            return self.link
        return f'/programs/{self.slug}/'


class ProgramVariant(BaseModel):
    """Ta'lim yo'nalishi varianti (shakl bo'yicha)"""

    class StudyForm(models.TextChoices):
        FULL_TIME = 'full_time', "Kunduzgi"
        PART_TIME = 'part_time', "Sirtqi"
        EVENING = 'evening', "Kechki"
        DISTANCE = 'distance', "Masofaviy"
        DUAL = 'dual', "Dual"

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='variants', verbose_name="Yo'nalish")
    study_form = models.CharField(max_length=20, choices=StudyForm.choices, verbose_name="Ta'lim shakli")
    study_duration = models.CharField(max_length=50, verbose_name="O'qish muddati (masalan: 4 yil)")

    contract_price = models.DecimalField(max_digits=12, decimal_places=0, null=True, blank=True, verbose_name="Kontrakt narxi (so'm)")
    grant_slots = models.PositiveIntegerField(default=0, verbose_name="Grant o'rinlar soni")
    contract_slots = models.PositiveIntegerField(default=0, verbose_name="Kontrakt o'rinlar soni")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Ta'lim shakli varianti"
        verbose_name_plural = "Ta'lim shakli variantlari"
        unique_together = ['program', 'study_form']
        ordering = ['study_form']

    def __str__(self):
        return f"{self.program.name} - {self.get_study_form_display()}"

    def get_formatted_price(self):
        if self.contract_price:
            return f"{self.contract_price:,.0f} so'm".replace(',', ' ')
        return "Belgilanmagan"


class FacultyBreadcrumb(BaseModel):
    """Fakultetlar sahifasi breadcrumb"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Qo'shimcha sarlavha")
    parent_title = models.CharField(max_length=100, default="Bosh sahifa", verbose_name="Ota sahifa nomi")
    parent_link = models.CharField(max_length=255, default="/", verbose_name="Ota sahifa havolasi")
    background_image = models.ImageField(upload_to='faculties/breadcrumb/', verbose_name="Fon rasmi")

    # --- YANGI MAYDONLAR ---
    dean_message_label = models.CharField(
        max_length=100, default="Dekan xabari",
        verbose_name="'Dekan xabari' sarlavhasi"
    )
    mission_label = models.CharField(
        max_length=100, default="Missiya",
        verbose_name="'Missiya' sarlavhasi"
    )
    vision_label = models.CharField(
        max_length=100, default="Viziya",
        verbose_name="'Viziya' sarlavhasi"
    )
    departments_label = models.CharField(
        max_length=100, default="Kafedralar ro'yxati",
        verbose_name="'Kafedralar ro'yxati' sarlavhasi"
    )

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Breadcrumb"
        verbose_name_plural = "Breadcrumb"

    def __str__(self):
        return "Fakultetlar breadcrumb"

    def save(self, *args, **kwargs):
        if self.is_active:
            FacultyBreadcrumb.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class DivisionBreadcrumb(BaseModel):
    """Bo'limlar sahifasi breadcrumb"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Qo'shimcha sarlavha")
    parent_title = models.CharField(max_length=100, default="Bosh sahifa", verbose_name="Ota sahifa nomi")
    parent_link = models.CharField(max_length=255, default="/", verbose_name="Ota sahifa havolasi")
    background_image = models.ImageField(upload_to='divisions/breadcrumb/', verbose_name="Fon rasmi")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Bo'limlar Breadcrumb"
        verbose_name_plural = "Bo'limlar Breadcrumb"

    def __str__(self):
        return "Bo'limlar breadcrumb"

    def save(self, *args, **kwargs):
        if self.is_active:
            DivisionBreadcrumb.objects.filter(is_active=True).update(is_active=False)
        super().save(*args, **kwargs)

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()


class DepartmentBreadcrumb(BaseModel):
    """Kafedralar sahifasi breadcrumb va label'lar"""
    title = models.CharField(max_length=255, verbose_name="Sarlavha")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Qo'shimcha sarlavha")
    parent_title = models.CharField(max_length=100, default="Bosh sahifa", verbose_name="Ota sahifa nomi")
    parent_link = models.CharField(max_length=255, default="/", verbose_name="Ota sahifa havolasi")
    background_image = models.ImageField(upload_to='departments/breadcrumb/', blank=True, null=True, verbose_name="Fon rasmi")

    # --- Label maydonlar ---
    tab_about_label = models.CharField(max_length=100, default="Kafedra haqida", verbose_name="'Kafedra haqida' tab")
    tab_team_label = models.CharField(max_length=100, default="Kafedra tarkibi", verbose_name="'Kafedra tarkibi' tab")
    tab_science_label = models.CharField(max_length=100, default="Ilmiy faoliyat", verbose_name="'Ilmiy faoliyat' tab")
    tab_international_label = models.CharField(max_length=100, default="Xalqaro hamkorlik", verbose_name="'Xalqaro hamkorlik' tab")

    head_title_label = models.CharField(max_length=100, default="Kafedra mudiri", verbose_name="'Kafedra mudiri' sarlavhasi")
    head_position_label = models.CharField(max_length=100, default="Kafedra mudiri", verbose_name="'Kafedra mudiri' lavozimi")
    degree_label = models.CharField(max_length=100, default="Ilmiy darajasi:", verbose_name="'Ilmiy darajasi' label")
    rank_label = models.CharField(max_length=100, default="Ilmiy unvoni:", verbose_name="'Ilmiy unvoni' label")
    reception_label = models.CharField(max_length=100, default="Qabul kunlari:", verbose_name="'Qabul kunlari' label")
    address_label = models.CharField(max_length=100, default="Manzil:", verbose_name="'Manzil' label")
    phone_label = models.CharField(max_length=100, default="Telefon:", verbose_name="'Telefon' label")
    email_label = models.CharField(max_length=100, default="Email:", verbose_name="'Email' label")

    history_label = models.CharField(max_length=100, default="Kafedra tarixi", verbose_name="'Kafedra tarixi' sarlavhasi")
    about_head_label = models.CharField(max_length=100, default="Mudir haqida", verbose_name="'Mudir haqida' sarlavhasi")
    team_label = models.CharField(max_length=100, default="Kafedra tarkibi", verbose_name="'Kafedra tarkibi' sarlavhasi")
    science_label = models.CharField(max_length=100, default="Ilmiy faoliyat", verbose_name="'Ilmiy faoliyat' sarlavhasi")
    international_label = models.CharField(max_length=100, default="Xalqaro hamkorlik", verbose_name="'Xalqaro hamkorlik' sarlavhasi")
    empty_label = models.CharField(max_length=200, default="Hozircha ma'lumot kiritilmagan", verbose_name="Bo'sh holat matni")

    is_active = models.BooleanField(default=True, verbose_name="Faolmi?")

    class Meta:
        verbose_name = "Kafedra breadcrumb"
        verbose_name_plural = "Kafedra breadcrumb"

    def __str__(self):
        return self.title

    @classmethod
    def get_active(cls):
        return cls.objects.filter(is_active=True).first()

    def has_add_permission(self, request):
        return not DepartmentBreadcrumb.objects.exists()