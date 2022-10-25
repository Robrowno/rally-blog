from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }))

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'likes': forms.HiddenInput(), 'comments': forms.HiddenInput()}

class EditPostForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }))

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'likes': forms.HiddenInput(), 'comments': forms.HiddenInput()}
