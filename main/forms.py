from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']
        
        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Ism Familiya', 'class': 'mt-3 form'}),
            "phone": forms.TextInput(attrs={"placeholder": '99-999-9999', 'class': 'mt-3 form', 'pattern': r'[0-9]{2}-[0-9]{3}-[0-9]{4}'}),
            "message": forms.Textarea(attrs={"placeholder": 'Qoshimcha xabarlar...', 'class': 'mt-3'})
        }

class ContestRegisterForm(forms.ModelForm):
    class Meta:
        model = ContestRegister
        fields = ['full_name', 'age', 'experience', 'phone', 'about']
        
        widgets = {
            "full_name": forms.TextInput(attrs={'placeholder': 'Ism Familiya', 'class': 'mt-3 form'}),
            "age": forms.NumberInput(attrs={'placeholder': 'Yoshingiz', 'class': 'mt-3 form'}),
            "experience": forms.TextInput(attrs={'placeholder': 'Tajribangiz necha oy/yil ?', 'class': 'mt-3 form'}),
            "phone": forms.TextInput(attrs={"placeholder": '99-999-9999', 'class': 'mt-3 form', 'pattern': r'[0-9]{2}-[0-9]{3}-[0-9]{4}'}),
            "about": forms.Textarea(attrs={"placeholder": 'Qoshimcha xabarlar...', 'class': 'mt-3', 'rows': 4, 'cols': 32})
        }


class EventRegisterForm(forms.ModelForm):
    class Meta:
        model = EventRegister
        fields = ['full_name', 'age', 'experience', 'phone', 'about']
        
        widgets = {
            "full_name": forms.TextInput(attrs={'placeholder': 'Ism Familiya', 'class': 'mt-3 form'}),
            "age": forms.NumberInput(attrs={'placeholder': 'Yoshingiz', 'class': 'mt-3 form'}),
            "experience": forms.TextInput(attrs={'placeholder': 'Tajribangiz necha oy/yil ?', 'class': 'mt-3 form'}),
            "phone": forms.TextInput(attrs={"placeholder": '99-999-9999', 'class': 'mt-3 form', 'pattern': r'[0-9]{3}-[0-9]-{2}[0-9]{3}-[0-9]{4}'}),
            "about": forms.Textarea(attrs={"placeholder": 'Qoshimcha xabarlar...', 'class': 'mt-3'})
        }

		
class ContestQuestionForm(forms.Form):
    class Meta:
        model = ContestQuestion
        fields = ['full_name', 'age', 'phone', 'about']
        
        widgets = {
            "full_name": forms.TextInput(attrs={'placeholder': 'Ism Familiya', 'class': 'mt-3 form'}),
            "age": forms.NumberInput(attrs={'placeholder': 'Yoshingiz', 'class': 'mt-3 form'}),
            "phone": forms.TextInput(attrs={"placeholder": '99-999-9999', 'class': 'mt-3 form', 'pattern': r'[0-9]{3}-[0-9]-{2}[0-9]{3}-[0-9]{4}'}),
            "about": forms.Textarea(attrs={"placeholder": 'Qoshimcha xabarlar...', 'class': 'mt-3', 'rows': 4, 'cols': 22})
        }

class EventQuestionForm(forms.Form):
    class Meta:
        model = EventQuestion
        fields = ['full_name', 'age', 'phone', 'about']
        
        widgets = {
            "full_name": forms.TextInput(attrs={'placeholder': 'Ism Familiya', 'class': 'mt-3 form'}),
            "age": forms.NumberInput(attrs={'placeholder': 'Yoshingiz', 'class': 'mt-3 form'}),
            "phone": forms.TextInput(attrs={"placeholder": '99-999-9999', 'class': 'mt-3 form', 'pattern': r'[0-9]{3}-[0-9]-{2}[0-9]{3}-[0-9]{4}'}),
            "about": forms.Textarea(attrs={"placeholder": 'Qoshimcha xabarlar...', 'class': 'mt-3'})
        }
