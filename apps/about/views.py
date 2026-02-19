from django.shortcuts import render

from .models import (AboutBreadcrumb, AboutUniversity, AboutStatistic,
                     AboutHistory, AboutFunfact, AboutMission,
                     AboutMissionItem, AboutCampusTour, Leader)


def about(request):
    """Universitet haqida sahifa"""

    # 1. Breadcrumb
    breadcrumb = AboutBreadcrumb.get_active()

    # 2. Universitet haqida
    about_university = AboutUniversity.get_active()
    about_statistics = AboutStatistic.objects.filter(is_active=True).order_by('order')[:3]

    # 3. Tarix
    history = AboutHistory.get_active()

    # 4. Funfact
    funfacts = AboutFunfact.objects.filter(is_active=True).order_by('order')[:3]

    # 5. Missiya
    mission = AboutMission.get_active()
    mission_items_left = AboutMissionItem.objects.filter(is_active=True, side='left').order_by('order')
    mission_items_right = AboutMissionItem.objects.filter(is_active=True, side='right').order_by('order')

    # 6. Kampus sayohati
    campus_tour = AboutCampusTour.get_active()

    # 7. Rahbariyat
    leaders = Leader.objects.filter(is_active=True).order_by('order')

    context = {
        'page_title': 'Universitet haqida',
        # 1
        'breadcrumb': breadcrumb,
        # 2
        'about_university': about_university,
        'about_statistics': about_statistics,
        # 3
        'history': history,
        # 4
        'funfacts': funfacts,
        # 5
        'mission': mission,
        'mission_items_left': mission_items_left,
        'mission_items_right': mission_items_right,
        # 6
        'campus_tour': campus_tour,
        # 7
        'leaders': leaders,
    }
    return render(request, 'about/about.html', context)