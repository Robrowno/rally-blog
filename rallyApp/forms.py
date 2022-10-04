from django import forms
from .models import Comment


class EditCommentForm(forms.ModelForm):

    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }))

    class Meta:
        model = Comment
        fields = ('body',)
