from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


from .models import Article
from .forms import ArticleForm


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


@login_required
def article_create_view(request):
    # print(request.POST)

    template_name = 'create_article.html'
    form = ArticleForm(request.POST or None)
    print(dir(form))
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        context['form'] = form
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            print(title, content)
            object_art = Article.objects.create(title=title, content=content)
            context['object'] = object_art
            context['create_date'] = True
   
    return render(request, template_name, context)

# @login_required
# def article_create_view(request):
#     # print(request.POST)

#     template_name = 'create_article.html'
#     form = ArticleForm()
#     print(dir(form))
#     context = {
#         'form': form
#     }
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             print(title, content)
#             object_art = Article.objects.create(title=title, content=content)
#             context['object'] = object_art
#             context['create_date'] = True
   
#     return render(request, template_name, context)


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
