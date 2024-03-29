from .models import *
from django import forms
from django.core.exceptions import ValidationError


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'user_email', 'text_comments')


class AddStockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Artifact
        fields = ['title', 'summary', 'text', 'photo', 'is_published', 'author', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'text': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title