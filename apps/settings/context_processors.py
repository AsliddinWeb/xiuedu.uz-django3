from .models import (
    SiteSettings, SocialNetwork, HeaderSettings, HeaderMenu,
    FooterSettings, FooterCategoryMenu
)


def site_settings(request):
    """Sayt sozlamalarini barcha sahifalarga yuklash"""
    settings = SiteSettings.get_active()
    header_settings = HeaderSettings.get_active()
    footer_settings = FooterSettings.get_active()

    # Header menyular - faqat asosiy (parent=None)
    header_menus = HeaderMenu.objects.filter(
        is_active=True,
        parent=None
    ).prefetch_related('children').order_by('order')

    # Footer kategoriya menyular
    footer_categories = FooterCategoryMenu.objects.filter(
        is_active=True
    ).prefetch_related('menu_items').order_by('order')

    # Ijtimoiy tarmoqlar
    social_networks = SocialNetwork.objects.filter(is_active=True).order_by('order')

    return {
        'site_settings': settings,
        'header_settings': header_settings,
        'footer_settings': footer_settings,
        'header_menus': header_menus,
        'footer_categories': footer_categories,
        'social_networks': social_networks,
    }