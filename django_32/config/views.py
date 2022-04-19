import random
import string

from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    '''
    This is get session
    '''
    print('Card id: ', request.session.get('card_1d'))
    # printing uppercase
    names = ('DilshadGit, DilMac, Dillux')
    letters = string.ascii_uppercase
    dev = (''.join(random.choice(letters) for x in range(8)))

    # print('User: ', request.session.get('user'))
    template_name = 'index.html'

    context = {
        'admin': dev,
        'index': 'Welcome to Django32 Platform',
    }
    return render(request, template_name, context)


# lesson 13
