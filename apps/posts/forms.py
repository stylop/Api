from ckeditor_uploader.fields import RichTextUploadingField
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField()
    published_date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Post
        fields = [
            "title",
            "text",
            "image",
            "published_date",
        ]