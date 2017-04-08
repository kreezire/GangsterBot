from django.shortcuts import render
import json
# Create your views here.
from django.http import HttpResponse


def index(request):
    #print request
    #req=json.loads(request.body)
    if request.method == 'POST':
        return
        # What should I return here???
    else:
        #req=json.loads(request.GET)
        #return HttpResponse("Hello, world. This is Faacebook Messenger API.")
        if request.GET.get('hub.verify_token') == 'make_me_an_offer_i_can_not_refuse':
            #print request.GET;
            return HttpResponse(request.GET.get('hub.challenge'))
            #res.status(200).send(req.query['hub.challenge']);
        else:
            #console.error("Failed validation. Make sure the validation tokens match.");
           return HttpResponse("Hello, world. This is Faacebook Messenger API.")