from typing import List

from django.shortcuts import render
from app01 import models


# Create your views here.
def article(request, *args, **kwargs):
    article_type: List[models.ArticleType] = models.ArticleType.objects.all()
    category: List[models.Category] = models.Category.objects.all()
    return render(request, 'article.html', {
        'result': (models.Article.objects.filter(
            **{k: v for k, v in kwargs.items() if v != '0'}
        )),
        'article_type': article_type,
        'category': category,
    }, )
