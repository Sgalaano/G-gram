from django import forms
from models import Image, Comments

class NewstatusForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','image_caption')

class NewstatusForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)