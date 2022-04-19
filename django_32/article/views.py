from django.shortcuts import render, get_object_or_404


from .models import Article


def articles_view(request, *args, **kwargs):
    template_name = 'article_list.html'

    obj_qs = Article.objects.all()
    context = {
        'obj_list': obj_qs
    }
    return render(request, template_name, context)


def search_article_view(request):
    template_name = 'search.html'
    # print(dir(request))
    # print(request.GET)
    query_dict = request.GET  # This is dictionary

    try:
        query = int(query_dict.get('q'))
    except:
        query = None

    art_obj = None
    if query is not None:
        art_obj = Article.objects.get(id=query)

    context = {
        'object': art_obj,
    }
    return render(request, template_name, context)


def article_detail_view(request, article_id):
    template_name = 'article_detail.html'

    # if id is not None:
    #     art_obj = Article.objects.get(id=id)
    art = get_object_or_404(Article, pk=article_id)
    context = {
        'art': art,
    }
    return render(request, template_name, context)


def article_create_view(request):
    print(request.POST, ' <<< post')

    template_name = 'create_article.html'
    context = {}
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print(title, content)
        object_art = Article.objects.create(title=title, content=content)
        context['object'] = object_art

    return render(request, template_name, context)


def article_update_view(request):
    template_name = 'edit_article.html'
    context = {

    }
    return render(request, template_name, context)


def article_delete_view(request):
    template_name = 'delete_article.html'
    context = {

    }
    return render(request, template_name, context)
