from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML
from .models import CamperConversion, Category, Electric, PostImage
from django.forms.widgets import CheckboxSelectMultiple, ClearableFileInput
from django.utils.translation import ugettext_lazy


class MyClearableFileInput(ClearableFileInput):
    clear_checkbox_label = ugettext_lazy('Delete')


class ConversionForm(forms.ModelForm):

    class Meta:
        model = CamperConversion
        fields = '__all__'
        labels = {
            'price': 'Price (£)', 'name': 'Your Name', 'listing_title': 'Listing Title (pick something which captures attention)',
            'year' : 'Vehicle Registration Year', 'vehicle_length' : 'Vehicle Length (m)', 'vehicle_width' : 'Vehicle Width (m)',
            'vehicle_height' : 'Vehicle Height (m)', 'vehicle_description' : 'Vehicle Description - please provide as much information as possible to potential buyers about the mechanical and asthetic elements of the vehicle. For example: vehicle history, bodywork condition and other information not already provided above',
            'Berths' : 'Berths (how many can it sleep - if any.....)', 'beds_description' : 'Beds Description (please leave a little information about the sleeping arrangements, including the bed sizes)',
            'max_weight': '<strong>Maximum Weight (MAM or MTPLM)</strong> (You MUST ensure the correct weight is listing on your advert!)<br><br>MAM, used in the context of driving licences, is the maximum weight of a vehicle or trailer including the maximum load that can be carried safely while used on the road. This is also known as gross vehicle weight (GVW) or permissible maximum weight. <br> MTPLM stands for Maximum Technically Permissible Laden Mass. This is the maximum weight, determined by the manufacturer, that is deemed to be safe to load the caravan to. On UK-spec caravans, the MTPLM is given on a plate near the entrance door.',
            'unladen_weight_verified': 'Unladen Weight Verifed? - Please check this box if you have had the conversion weighed since completion',
            'unladen_weight': '<strong>Unladen Weight </strong>- If you have have the vehicle on a weightbridge, please provide the readout in kg. Please provide a photograph to support this when uploading your images.',
            'registered_body_type': '<strong>Registered Body Type</strong> - What is the body registered as with the DVLA? You can find this in Body Type field (D.5) on the vehicle V5C registered keeper document.',
            'unique_ref': '<strong>Unique Ref </strong>( ignore this, it is for us to assign your listing token during checkout )',
        }

        # Hidden field, which defines if the listing is active on the site
        widgets = {
            'is_active': forms.HiddenInput(),
            'user': forms.HiddenInput(),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['unique_ref'].disabled = True
        self.fields['category'].choices = friendly_names
        self.fields['electrics'].widget = CheckboxSelectMultiple()
        self.fields['electrics'].queryset = Electric.objects.all()
        self.fields['electrics'].required = True
        self.fields['main_image'].widget = MyClearableFileInput()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-3'


class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Making location required
        self.fields['image'].required = False
        # self.fields['image'].widget = MyClearableFileInput()

    class Meta:
        model = PostImage
        fields = ('image',)
