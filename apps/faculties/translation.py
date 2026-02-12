from modeltranslation.translator import register, TranslationOptions

from .models import (Faculty, Department, Staff, Division,
                     EducationLevel, Program, ProgramVariant)


@register(Faculty)
class FacultyTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'short_description',
              'dean_full_name', 'dean_degree', 'dean_bio', 'dean_reception_days')


@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description',
              'head_full_name', 'head_degree', 'head_bio', 'head_reception_days')


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'degree', 'bio')


@register(Division)
class DivisionTranslationOptions(TranslationOptions):
    fields = ('name', 'description',
              'head_full_name', 'head_degree', 'head_bio', 'head_reception_days')


@register(EducationLevel)
class EducationLevelTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'short_description', 'language', 'accreditation')


@register(ProgramVariant)
class ProgramVariantTranslationOptions(TranslationOptions):
    fields = ('study_duration',)