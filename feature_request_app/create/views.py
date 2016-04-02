from django.shortcuts import render

from .forms import FeatureRequestForm


def single_page_app(request):
    form = FeatureRequestForm(request.POST)

    if form.is_valid():
        pass

    return render(request, 'single-page-app.html', {'form':form})