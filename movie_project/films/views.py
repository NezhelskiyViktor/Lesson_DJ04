from django.shortcuts import render, redirect
from .models import Film_post
from .forms import Films_postForm


def page1(request):
    films = Film_post.objects.all()
    return render(request, 'films/page1.html', {'films': films})  #, {'films': films})


def page2(request):
    error = ''
    if request.method == 'POST':
        form = Films_postForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
            return redirect('page1')
        else:
            error = "Данные были заполнены некорректно"
    form = Films_postForm()
    return render(request, 'films/page2.html', {'form': form, 'error': error})
