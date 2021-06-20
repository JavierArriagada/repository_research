from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from .models import Page

# Create your views here.
class PageListView(ListView):

    model = Page


def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'pages/page.html', {'page':page})