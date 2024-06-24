from django import forms
from .models import Contact, Comment

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        # fields = ['name', 'email', 'message']
        fields = '__all__'


class SubscriptionForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    email = forms.EmailField()

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['user', 'body']