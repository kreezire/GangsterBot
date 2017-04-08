from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse


def index(request):
    #print request
    #req=json.loads(request.body)
    if request.method == 'POST':
        return
    else:
        if request.GET.get('hub.verify_token') == 'make_me_an_offer_i_can_not_refuse':
            return HttpResponse(request.GET.get('hub.challenge'))
        else:
           return HttpResponse("Hello, world. This is Faacebook Messenger API.")