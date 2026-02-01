from django.shortcuts import render


def home(request):
    """Bosh sahifa view"""
    context = {
        'page_title': 'Bosh sahifa',
    }
    return render(request, 'home.html', context)
