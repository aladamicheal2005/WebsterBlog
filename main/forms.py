from django.forms import ModelForm
from .models import profile, comment





class profileForm(ModelForm):
    class Meta:
        model = profile
        fields = ['Text', 
        'Detail', 
        'image']



class commentForm(ModelForm):
    class Meta:
        model = comment
        
        fields = ['name', 
        'body', 
        ]








