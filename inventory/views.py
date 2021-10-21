from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import *

from .models import Category, Product, ProductAdditions, ProductDeductions
from .forms import CategoryForm

from django.forms.models import model_to_dict


class CreateCategory(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    form_class = CategoryForm
    template_name = 'form.html'
    success_url = reverse_lazy('inventory:category-list')

    def test_func(self):
        return self.request.user.has_perm('add_Category')


class ListCategory(ListView, LoginRequiredMixin):
    model = Category
    template_name = 'category-list.html'
    paginate_by = 50


class DetailCategory(DetailView, LoginRequiredMixin):
    model = Category
    template_name = 'category-detail.html'


class UpdateCategory(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Category
    template_name = 'form.html'
    success_url = reverse_lazy('inventory:category-list')
    form_class = CategoryForm

    def test_func(self):
        return self.request.user == self.get_object().manager


class DeleteCategory(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Category
    template_name = 'form.html'
    success_url = reverse_lazy('inventory:category-list')

    def test_func(self):
        return self.request.user == self.get_object().manager


class ManageCategories(TemplateView):
    template_name = 'formset.html'
