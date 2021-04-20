from django import forms


class ContactUsForm(forms.Form):
    email = forms.EmailField(label='email')
    msg = forms.CharField(label='msg', widget=forms.Textarea)