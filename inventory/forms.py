from django.forms import *
from django.contrib.auth.models import User
from .models import Category, Product, ProductAdditions, ProductDeductions


form_control = 'form-control'


class StyledForm(Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs["class"] = form_control


class CategoryForm(ModelForm, StyledForm):

    class Meta:
        model = Category
        fields = [
            'title',
            'description',
            'manager',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['manager'].choices = User.objects.filter(is_staff=True)

        self.name = 'Stand Category'
