from .models import *
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'user_email', 'text_comments')


class AddStockForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input'}), label='Название')
    # slug = forms.SlugField(max_length=100, label='URL')
    summary = forms.CharField(max_length=255, label='Описание')
    text = forms.CharField(widget=forms.Textarea(attrs={'cols':60, 'rows': 10}), label='Текст')
    is_published = forms.BooleanField(label='Публикация', required=False)
    author = forms.ModelChoiceField(queryset=User.objects.all(), label='Автор', empty_label='Автор не выбран')
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='Категория не выбрана')