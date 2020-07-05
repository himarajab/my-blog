from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView,UpdateView,DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .forms import DataForm
from .models import Data
# from .mine import read_url


class DataCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form': DataForm()}
        return render(request, 'core/data_form.html', context)

    def post(self, request, *args, **kwargs):
        form = DataForm(request.POST)
        if form.is_valid():
            data = form.save()
            data.save()
            return HttpResponseRedirect(reverse_lazy('my_core:detail-data', args=[data.id]))
        return render(request, 'core/data_form.html', {'form': form})


class DataUpdateView(UpdateView):
    model = Data
    fields= 'title','body'
    template_name = 'core/data_update.html'
    success_url = reverse_lazy('my_core:home')


class DataListView(ListView):
    model = Data


class DataDeleteView(DeleteView):
    model = Data
    success_url = reverse_lazy('my_core:home')




class Home(TemplateView):
    template_name = 'core/home.html'


