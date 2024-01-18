from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Finch, Toy
from .forms import FeedingForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about (request):
    return render(request, 'about.html')

def finch_index(request):
    finch = Finch.objects.all()
    return render(request, 'finch/index.html', {'finch' : finch })

def finch_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    feedingform = FeedingForm()
    return render(request, 'finch/detail.html', {'finch' : finch, 'feeding_form': feedingform })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['name', 'bird', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finch'

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # it's also important to validate forms.
    # django gives us a built in function for that
    if form.is_valid():
        # dont want to save the feeding to the db until we have a cat id
        new_feeding = form.save(commit=False)
        # this is where we add the cat id
        new_feeding.finch_id = finch_id
        new_feeding.save()
    # finally, redirect to the cat detail page
    return redirect('detail', finch_id=finch_id)

class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']
    
# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'
    