from django import forms

class studentForm(forms.Form):
    firstname=forms.CharField(label="enter your first name")
    secondname=forms.CharField(label="enter your second name")