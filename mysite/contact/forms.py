from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(label='YOur Email', required=False)
    message = forms.CharField(widget=forms.Textarea)
