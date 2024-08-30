from django import forms
from  .models import TeacherModel

class TeacherAddForm(forms.ModelForm):
    class Meta:
        model = TeacherModel
        exclude = ['id']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'vacant': forms.TextInput(attrs={'class': 'form-control'}),
            'next_meeting_subject': forms.TextInput(attrs={'class': 'form-control'}),
        }