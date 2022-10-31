from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):

    """
    Form for adding a Blog post on the frontend.
    """

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 3
    }), required=True)

    featured_image = forms.ImageField(required=True)

    class Meta:
        """
        Define Form fields
        """

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
        """
        Define Form fields
        """

        model = Post
        exclude = [
            'author',
            'updated_on',
            'created_on',
            'likes',
            'slug',
            'status',
            'comments'
            ]
