from django.shortcuts import render


def single_page_app(request):
    return render(request, 'single-page-app.html', {})