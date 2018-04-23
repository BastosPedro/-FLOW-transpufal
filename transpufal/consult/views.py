from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Process, Category

@login_required
def index(request):
    num_categories = Category.objects.all().count()
    num_processes = Process.objects.all().count()
    num_finished_processes = Process.objects.filter(status='C').count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    return render(
        request,
        'index.html',
        context={'num_categories': num_categories, 'num_processes': num_processes, 'num_finished_processes': num_finished_processes, 'num_visits':num_visits},
    )

class ProcessListView(LoginRequiredMixin, generic.ListView):
        model = Process

class ProcessDetailView(LoginRequiredMixin, generic.DetailView):
        model = Process
# Create your views here.
