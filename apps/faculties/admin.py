from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import (Faculty, Department, Staff, Division,
                     EducationLevel, Program, ProgramVariant)


# Inlines
class DepartmentInline(TranslationTabularInline):
    model = Department
    extra = 0
    fields = ['name', 'slug', 'head_full_name', 'order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    show_change_link = True


class StaffInline(TranslationTabularInline):
    model = Staff
    extra = 0
    fields = ['full_name', 'staff_type', 'position', 'phone', 'order', 'is_active']
    fk_name = 'department'


class DivisionStaffInline(TranslationTabularInline):
    model = Staff
    extra = 0
    fields = ['full_name', 'staff_type', 'position', 'phone', 'order', 'is_active']
    fk_name = 'division'


class ProgramInline(TranslationTabularInline):
    model = Program
    extra = 0
    fields = ['name', 'slug', 'education_level', 'code', 'order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    show_change_link = True


class ProgramVariantInline(TranslationTabularInline):
    model = ProgramVariant
    extra = 1
    fields = ['study_form', 'study_duration', 'contract_price', 'grant_slots', 'contract_slots', 'is_active']


# 1. Fakultet
@admin.register(Faculty)
class FacultyAdmin(TranslationAdmin):
    list_display = ['name', 'dean_full_name', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'dean_full_name']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DepartmentInline, ProgramInline]

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'slug', 'short_description', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Dekan', {
            'fields': ('dean_full_name', 'dean_photo', 'dean_degree',
                       'dean_phone', 'dean_email', 'dean_bio', 'dean_reception_days')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 2. Kafedra
@admin.register(Department)
class DepartmentAdmin(TranslationAdmin):
    list_display = ['name', 'faculty', 'head_full_name', 'order', 'is_active']
    list_filter = ['is_active', 'faculty']
    search_fields = ['name', 'head_full_name']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [StaffInline]

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('faculty', 'name', 'slug', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Kafedra mudiri', {
            'fields': ('head_full_name', 'head_photo', 'head_degree',
                       'head_phone', 'head_email', 'head_bio', 'head_reception_days')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 3. Xodim
@admin.register(Staff)
class StaffAdmin(TranslationAdmin):
    list_display = ['full_name', 'staff_type', 'position', 'department', 'division', 'order', 'is_active']
    list_filter = ['is_active', 'staff_type', 'department__faculty', 'department', 'division']
    search_fields = ['full_name', 'position', 'degree']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Tegishlilik', {
            'fields': ('staff_type', 'department', 'division'),
            'description': 'Kafedra YOKI bo\'limdan birini tanlang'
        }),
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('full_name', 'photo', 'position', 'degree')
        }),
        ('Aloqa', {
            'fields': ('phone', 'email')
        }),
        ('Qo\'shimcha', {
            'fields': ('bio',)
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 4. Bo'lim
@admin.register(Division)
class DivisionAdmin(TranslationAdmin):
    list_display = ['name', 'head_full_name', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'head_full_name']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [DivisionStaffInline]

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'slug', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Bo\'lim boshlig\'i', {
            'fields': ('head_full_name', 'head_photo', 'head_degree',
                       'head_phone', 'head_email', 'head_bio', 'head_reception_days')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 5. Ta'lim darajasi
@admin.register(EducationLevel)
class EducationLevelAdmin(TranslationAdmin):
    list_display = ['name', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'background_image', 'style_class')
        }),
        ('Boshqa', {
            'fields': ('order', 'is_active')
        }),
    )


# 6. Ta'lim yo'nalishi
@admin.register(Program)
class ProgramAdmin(TranslationAdmin):
    list_display = ['name', 'education_level', 'faculty', 'code', 'order', 'is_active']
    list_filter = ['is_active', 'education_level', 'faculty', 'department']
    search_fields = ['name', 'code']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProgramVariantInline]

    fieldsets = (
        ('Tegishlilik', {
            'fields': ('education_level', 'faculty', 'department')
        }),
        ('Asosiy ma\'lumotlar', {
            'fields': ('name', 'slug', 'code', 'short_description', 'description')
        }),
        ('Rasm', {
            'fields': ('image', 'image_alt_uz', 'image_alt_ru', 'image_alt_en')
        }),
        ('Qo\'shimcha', {
            'fields': ('language', 'employment_rate', 'accreditation')
        }),
        ('Boshqa', {
            'fields': ('link', 'order', 'is_active')
        }),
    )