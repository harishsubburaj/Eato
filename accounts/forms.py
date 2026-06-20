from django import forms
from .models import Banner

class BannerForm(forms.ModelForm):

    class Meta:

        model = Banner

        fields = ['title','image','status']