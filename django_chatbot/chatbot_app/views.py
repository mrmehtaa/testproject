from pkgutil import ImpImporter
import queue
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Chatbot

def home(request):
    return render(request,"home.html")

@csrf_exempt
def predict(request):
    text = json.loads(request.body)
    question = text['message']
    print("question: ", question)
    ans = Chatbot.objects.get(qus=question).ans
    print(ans)
    message = {"answer":ans} 
    print("message: ",message)
    return JsonResponse(message)