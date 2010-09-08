from django.shortcuts import render_to_response, get_object_or_404, redirect
from models import *
from forms import *

def create(request):
    """create (multiple ?) entries of contributions"""
    
    if request.method == 'GET':
        if request.GET.get('document') and request.GET.get('page_number'):
            page = get_object_or_404(Page, document__id=request.GET.get('document'), page_number=request.GET.get('page_number'))
            form = ContributionForm()
    if request.method == 'POST':
        form = ContributionForm(request.POST)
        form.save()