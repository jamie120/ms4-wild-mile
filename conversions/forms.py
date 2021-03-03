from django import forms
from .models import CamperConversion, Category, Electric, PostImage
from django.forms.widgets import CheckboxSelectMultiple


class ConversionForm(forms.ModelForm):

    class Meta:
        model = CamperConversion
        fields = '__all__'

        # Hidden field, which defines if the listing is active on the site
        widgets = {'is_active': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        self.fields['electrics'].widget = CheckboxSelectMultiple()
        self.fields['electrics'].queryset = Electric.objects.all()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')

    class Meta:
        model = PostImage
        fields = ('image', )
