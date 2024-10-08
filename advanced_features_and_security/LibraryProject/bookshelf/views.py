from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import BookForm
from .forms import ExampleForm

@permission_required('bookshelf.book_list', raise_exception=True)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_detail.html', {'article': article})

@permission_required('your_app_name.can_create', raise_exception=True)
def article_create(request):
    # Logic for creating an article
    pass

@permission_required('your_app_name.can_edit', raise_exception=True)
def article_edit(request, pk):
    # Logic for editing an article
    pass

@permission_required('your_app_name.can_delete', raise_exception=True)
def article_delete(request, pk):
    # Logic for deleting an article
    pass


def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

