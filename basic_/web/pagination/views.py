from django.shortcuts import render

from basic_.web.pagination.pagination import Page

LIST = {x for x in range(150)}


def user(request):
    page_key_name = 'p'
    cur_page = int(request.GET.get(page_key_name, 1))

    page = Page(cur_page, len(LIST))

    items = LIST[page.start:page.end]

    page_bar = page.url_build(f'/user?{page_key_name}=')

    return render(request, 'user.html', {'items': items, 'page_bar': page_bar})
