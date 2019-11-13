from django import forms

class DetailForm(forms.Form):
    fullname = forms.CharField(label="Fullname", widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(label="Address", widget=forms.Textarea(attrs={'class':'form-control'}))

class ReksadanaCreateForm(forms.Form):
    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    price = forms.IntegerField(label="Price", widget=forms.NumberInput(attrs={'class':'form-control'}))
    number = forms.IntegerField(label="Amount", widget=forms.NumberInput(attrs={'class':'form-control'}))