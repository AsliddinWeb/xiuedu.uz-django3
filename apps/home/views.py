from django.shortcuts import render
from django.utils import timezone

from .models import (
    BannerSettings, BannerVideo, BannerSlider, BannerNavigation,
    AboutSection, StatisticItem, NewsStaticTexts, Partner,
    LicenseStaticTexts, LicenseItem, ProgramStaticTexts,
    StudentLifeStaticTexts, StudentLifeItem,
    DirectionStaticTexts, EventStaticTexts, LeadershipStaticTexts,
    AdmissionBanner, ScholarshipBanner, GalleryStaticTexts
)
from apps.faculties.models import EducationLevel, Program
from apps.events.models import Event
from apps.about.models import Leader
from apps.gallery.models import GalleryImage
from apps.news.models import News


def home(request):
    """Bosh sahifa view"""

    # 1. Banner
    banner_settings = BannerSettings.get_active()
    banner_video = None
    banner_sliders = None
    if banner_settings and banner_settings.show_video:
        banner_video = BannerVideo.get_active()
    else:
        banner_sliders = BannerSlider.objects.filter(is_active=True).order_by('-created_at')[:5]
    banner_navigations = BannerNavigation.objects.filter(is_active=True).order_by('order')[:2]

    # 2. About
    about_section = AboutSection.get_active()

    # 3. Statistika
    statistic_items = StatisticItem.objects.filter(is_active=True).order_by('order')[:3]

    # 4. Yangiliklar
    news_static = NewsStaticTexts.get_active()
    latest_news = News.objects.filter(is_active=True).select_related('author', 'category').order_by('-published_at')[:4]

    # 5. Hamkorlar
    partners = Partner.objects.filter(is_active=True).order_by('order')

    # 6. Litsenziya
    license_static = LicenseStaticTexts.get_active()
    license_items = LicenseItem.objects.filter(is_active=True).order_by('order')[:4]

    # 7. Ta'lim dasturlari
    program_static = ProgramStaticTexts.get_active()
    education_levels = EducationLevel.objects.filter(
        is_active=True
    ).prefetch_related('programs').order_by('order')

    # 8. Talabalar hayoti
    student_life_static = StudentLifeStaticTexts.get_active()
    student_life_items = StudentLifeItem.objects.filter(is_active=True).order_by('order')[:6]

    # 9. Yo'nalishlar
    direction_static = DirectionStaticTexts.get_active()
    programs_list = Program.objects.filter(
        is_active=True
    ).select_related('education_level', 'faculty').order_by('order')[:16]

    # 10. Tadbirlar
    event_static = EventStaticTexts.get_active()
    upcoming_events = Event.objects.filter(
        is_active=True,
        event_date__gte=timezone.now().date()
    ).order_by('event_date')[:3]

    # 11. Rahbariyat
    leadership_static = LeadershipStaticTexts.get_active()
    leaders = Leader.objects.filter(is_active=True).order_by('order')[:4]

    # 12. Qabul
    admission_banner = AdmissionBanner.get_active()

    # 13. Grandlar
    scholarship_banner = ScholarshipBanner.get_active()

    # 14. Galereya
    gallery_static = GalleryStaticTexts.get_active()
    gallery_images = GalleryImage.objects.filter(is_active=True, is_featured=True).order_by('order')[:6]

    context = {
        'page_title': 'Bosh sahifa',
        # 1. Banner
        'banner_settings': banner_settings,
        'banner_video': banner_video,
        'banner_sliders': banner_sliders,
        'banner_navigations': banner_navigations,
        # 2. About
        'about_section': about_section,
        # 3. Statistika
        'statistic_items': statistic_items,
        # 4. Yangiliklar
        'news_static': news_static,
        'latest_news': latest_news,
        # 5. Hamkorlar
        'partners': partners,
        # 6. Litsenziya
        'license_static': license_static,
        'license_items': license_items,
        # 7. Ta'lim dasturlari
        'program_static': program_static,
        'education_levels': education_levels,
        # 8. Talabalar hayoti
        'student_life_static': student_life_static,
        'student_life_items': student_life_items,
        # 9. Yo'nalishlar
        'direction_static': direction_static,
        'programs_list': programs_list,
        # 10. Tadbirlar
        'event_static': event_static,
        'upcoming_events': upcoming_events,
        # 11. Rahbariyat
        'leadership_static': leadership_static,
        'leaders': leaders,
        # 12. Qabul
        'admission_banner': admission_banner,
        # 13. Grandlar
        'scholarship_banner': scholarship_banner,
        # 14. Galereya
        'gallery_static': gallery_static,
        'gallery_images': gallery_images,
    }
    return render(request, 'home.html', context)