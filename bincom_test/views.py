from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView
from .models import AnnouncedPuResults, PollingUnit


# Create your views here.


class PollingResultList(ListView):
    models = AnnouncedPuResults
    queryset = AnnouncedPuResults.objects.all()
    template_name = 'bincom_test/announcedpollingunitresult.html'
    context_object_name = 'polling_results'


class IndividualPollingResult(DetailView):
    models = AnnouncedPuResults
    queryset = AnnouncedPuResults.objects.all()
    context_object_name = 'polling_result'
    template_name = 'bincom_test/individualpollingresult.html'


class NewPollingUnit(CreateView):
    models = AnnouncedPuResults
    queryset = AnnouncedPuResults.objects.all()
    fields = '__all__'
    success_url = reverse_lazy('polling_unit')
    template_name = 'bincom_test/new_polling_data.html'

    def form_valid(self, form):
        super(NewPollingUnit, self).form_valid(form)
