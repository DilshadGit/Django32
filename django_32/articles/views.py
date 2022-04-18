from django.shortcuts import render

# Create your views here.


def articles_view(request):
    template_name = 'article_list.html'
    context = {
        '': ,
    }
    return render(request, context, template_name)


def article_detail_view(request):
    template_name = 'article_detail.html'
    context = {
        '': ,
    }
    return render(request, context, template_name)


def articles_update_view(request):
    template_name = 'edit_article.html'
    context = {
        '': ,
    }
    return render(request, context, template_name)


def articles_create_view(request):
    template_name = 'create_article.html'
    context = {
        '': ,
    }
    return render(request, context, template_name)


def articles_delete_view(request):
    template_name = 'delete_article.html'
    context = {
        '': ,
    }
    return render(request, context, template_name)
