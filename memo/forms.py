# memo/forms.py
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['key', 'value']
        labels = {'user_input': 'key', 'user_input2': 'value'}
        
class UploadTestFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

