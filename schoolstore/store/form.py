from django import forms
from .models import Purchase

class PurchaseForm(forms.ModelForm):
    class Meta:
        model=Purchase
        fields = ['name', 'dob', 'age', 'gender', 'phno', 'mail', 'address', 'department', 'course', 'purpose', 'material1', 'material2', 'material3', 'material4', 'material5']