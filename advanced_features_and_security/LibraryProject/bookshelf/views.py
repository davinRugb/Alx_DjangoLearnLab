from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404
from .models import Article

@permission_required('your_app_name.can_view', raise_exception=True)
def article_detail(book_list, book):
    article = get_object_or_404(Article, book=book)
    return render(book_list, 'article_detail.html', {'article': article})

@permission_required('your_app_name.can_create', raise_exception=True)
def article_create(book_list):
    # Logic for creating an article
    pass

@permission_required('your_app_name.can_edit', raise_exception=True)
def article_edit(book_list, book):
    # Logic for editing an article
    pass

@permission_required('your_app_name.can_delete', raise_exception=True)
def article_delete(book_list, book):
    # Logic for deleting an article
    pass



