from django import forms
from .models import Business, Category

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Field, Div


class AddListingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Add Business', css_class='btn-success mt-5'))
        self.helper.layout = Layout(
            Field('name', css_class='form-control'),
            Div(
                Div(
                    Field('description', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                Div(
                    Field('logo', css_class='form-control'),
                    Field('category', css_class='form-control'),
                    Field('address', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    Field('landmark', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                Div(
                    Field('location', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    Field('longitude', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                Div(
                    Field('latitude', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                css_class='row'
            ),
            Div(
                Div(
                    Field('email', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                Div(
                    Field('phone', css_class='form-control'),
                    css_class='col-md-6 col-sm-12'
                ),
                css_class='row'
            ),
            Field('website', css_class='form-control'),
        )

    class Meta:
        model = Business
        fields = ['name', 'logo', 'landmark', 'email',
                  'website', 'description', 'location', 'address',
                  'category', 'longitude', 'latitude',
                  'phone']


class AddCategoryForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper(self)
    #     self.helper.add_input(Submit('submit', 'Add', css_class='btn btn-color mt-5'))
    #
    class Meta:
        model = Category
        fields = ['name', 'img']
