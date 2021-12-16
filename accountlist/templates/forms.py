 from django import forms

 class AccountListForm(forms.Form):
     text = forms.CharField(max_length = 45,
     widget = forms.TextInput(
         attrs = {'class':'form-control','placeholder':'Enter here','aria-label':'Account','aria-describeby':'add-btn'}
     ))