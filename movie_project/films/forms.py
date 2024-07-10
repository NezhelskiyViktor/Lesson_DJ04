from .models import Film_post
from django.forms import ModelForm, TextInput, Textarea



class Films_postForm(ModelForm):
    class Meta:
        model = Film_post
        fields = ['title', 'description', 'text']

        widgets = {
                    'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
                    'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма'}),
                    'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Отзыв о фильме'})
                }
