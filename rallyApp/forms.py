from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):

    """
    Form for Adding a Blog Post.
    """

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }), required=True)

    class Meta:

        model = Post
        fields = '__all__'
        widgets = {
            'likes': forms.HiddenInput(), 'comments': forms.HiddenInput()
            }


class UpdatePostForm(forms.ModelForm):
    """
    Form for Updating a Blog Post.
    """
    class Meta:

        model = Post
        exclude = ['author', 'updated_on', 'created_on', 'likes', 'slug', 'status', 'comments']
