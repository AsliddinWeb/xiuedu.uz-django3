from django.shortcuts import render
from django.utils import timezone

from .models import (BannerSettings, BannerVideo, BannerSlider, BannerNavigation, AboutSection, StatisticItem,
                     NewsStaticTexts, Partner, LicenseStaticTexts, LicenseItem, ProgramStaticTexts,
                     StudentLifeStaticTexts, StudentLifeItem, DirectionStaticTexts, EventStaticTexts)

from apps.faculties.models import EducationLevel, Program
from apps.events.models import Event


def home(request):
    """Bosh sahifa view"""
    # Banner sozlamalari
    banner_settings = BannerSettings.get_active()

    # Video yoki sliderlar
    banner_video = None
    banner_sliders = None

    if banner_settings and banner_settings.show_video:
        banner_video = BannerVideo.get_active()
    else:
        banner_sliders = BannerSlider.objects.filter(is_active=True).order_by('-created_at')[:5]

    # 1. Banner navigatsiyalar
    banner_navigations = BannerNavigation.objects.filter(is_active=True).order_by('order')[:2]

    # 2. About section
    about_section = AboutSection.get_active()

    # 3. Statistika
    statistic_items = StatisticItem.objects.filter(is_active=True).order_by('order')[:3]

    # 4. Yangiliklar static matnlari
    news_static = NewsStaticTexts.get_active()

    # 5. Partner
    partners = Partner.objects.filter(is_active=True).order_by('order')

    # 6. License
    license_static = LicenseStaticTexts.get_active()
    license_items = LicenseItem.objects.filter(is_active=True).order_by('order')[:4]

    # 7. Programs
    program_static = ProgramStaticTexts.get_active()
    education_levels = EducationLevel.objects.filter(
        is_active=True
    ).prefetch_related('programs').order_by('order')

    # 8. Students life
    student_life_static = StudentLifeStaticTexts.get_active()
    student_life_items = StudentLifeItem.objects.filter(is_active=True).order_by('order')[:6]

    # Programs
    direction_static = DirectionStaticTexts.get_active()
    programs_list = Program.objects.filter(is_active=True).select_related('education_level', 'faculty').order_by(
        'order')[:16]

    # 10. Events
    event_static = EventStaticTexts.get_active()
    upcoming_events = Event.objects.filter(is_active=True, event_date__gte=timezone.now().date()).order_by(
        'event_date')[:3]

    context = {
        'page_title': 'Bosh sahifa',
        'banner_settings': banner_settings,
        'banner_video': banner_video,
        'banner_sliders': banner_sliders,
        'banner_navigations': banner_navigations,
        'about_section': about_section,
        'statistic_items': statistic_items,
        'news_static': news_static,
        'partners': partners,
        'license_static': license_static,
        'license_items': license_items,
        'program_static': program_static,
        'education_levels': education_levels,
        'student_life_static': student_life_static,
        'student_life_items': student_life_items,
        'direction_static': direction_static,
        'programs_list': programs_list,
        'event_static': event_static,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'home.html', context)