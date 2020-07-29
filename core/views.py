from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import TemplateView, ListView, CreateView,UpdateView,DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .forms import DataForm,UpdateForm
from .models import Data



class DataCreateView(CreateView):
    
    def get(self, request, *args, **kwargs):
        context = {'form': DataForm()}
        return render(request, 'core/data_form.html', context)

    def post(self, request, *args, **kwargs):
        


        form = DataForm(request.POST)

        # body_form = dict(request.POST.get('body_json'))
        # print(f'\n request.get {body_form} \n')
        
        if form.is_valid():
            data = form.save(commit=False)

            data.save()
            return HttpResponseRedirect(reverse_lazy('my_core:detail-data', args=[data.id]))
        return render(request, 'core/data_form.html', 
        {
            'form': form,
            # 'body_json':body_json
        })


class DataUpdateView(UpdateView):
    model = Data
    form_class = UpdateForm
    template_name = 'core/data_update.html'
    success_url = reverse_lazy('my_core:home')


class DataListView(ListView):
    model = Data
    

class DataDeleteView(DeleteView):
    model = Data
    success_url = reverse_lazy('my_core:home')


