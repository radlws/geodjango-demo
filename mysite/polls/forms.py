from django import forms
from polls.models import BlogEntry


class BlogEntryForm(forms.ModelForm):

    class Meta:
        model = BlogEntry