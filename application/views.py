from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Application, Job
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import JobForm
from datetime import date, datetime

def calculateAge(born): 
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day)) 

def index(request):
    return render(request,"application/index.html", {})
def home(request):
    try:
        job_list = Job.objects.all()
        paginator = Paginator(job_list, 10) # Show 10 jobs  per page

        page = request.GET.get('page')
        jobs = paginator.get_page(page)
    except Application.DoesNotExist:
        raise Http404("There Are Jobs Currently In the System")
    return render(request, 'application/home.html', {'jobs': jobs})

def submit_form(request):
    request.POST._mutable = True
    if (request.POST.get('position')) or (request.GET.get('position')):
        if request.method == 'POST':
            request.POST._mutable = True
            date_of_birth = request.POST.get('date_of_birth')
            newage = int(calculateAge(datetime.strptime(date_of_birth, '%Y-%m-%d').date()))
            request.POST['age'] = newage
            form = JobForm(request.POST)
            if  form.is_valid():
                # form.cleaned_data['age'] = 
                print(form.cleaned_data['date_of_birth'])
                form.save()
                messages.success(request, ('Submitted Successfully'))
                return redirect('home')
            else:
                form = JobForm(request.POST)
        else:
            form = JobForm()
        context = {'form': form}
        print(request.GET.get('position'))
        context['form'].fields['position'].initial = request.GET.get('position')
        return render(request, 'application/form.html', context)
    else:
        return redirect('home')