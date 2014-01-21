#from django.shortcuts import render

# Create your views here.

from django.core.urlresolvers import reverse, reverse_lazy
#from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

#from human_res.forms import EmployeeAddressFormSet
from human_res.models import Employee, Email, Address


#class EditEmployeeAddress(UpdateView):
    #""" """
    #form_class = EmployeeAddressFormSet
    #model = Employee
    #success_url = reverse_lazy('human_res:employee-detail')


class EmployeeCreate(CreateView):
    """add a new employee object then redirect to the list page"""
    model = Employee
    success_url = reverse_lazy('human_res:employee-list')

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('human_res:employee-create')
        return context


class EmployeeDelete(DeleteView):
    """delete a employee object then redirect to the list page"""
    model = Employee
    success_url = reverse_lazy('human_res:employee-list')


class EmployeeDetail(DetailView):
    """display employee information"""
    model = Employee

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetail, self).get_context_data(**kwargs)
        context['address'] = self.object.address_set.all()
        context['email'] = self.object.email_set.all()
        return context


class EmployeeList(ListView):
    """list all of the current employees"""
    model = Employee
    paginate_by = 21


class EmployeeUpdate(UpdateView):
    """edit an employee object then redirect to the list page"""
    model = Employee
    success_url = reverse_lazy('human_res:employee-list')

    def get_context_data(self, **kwargs):
        context = super(EmployeeUpdate, self).get_context_data(**kwargs)
        context['action'] = reverse('human_res:employee-update', kwargs={'pk': self.get_object().id})
        return context


class HumanResourceIndex(TemplateView):
    """display the human resources homepage"""
    template_name = 'human_res/index.html'
