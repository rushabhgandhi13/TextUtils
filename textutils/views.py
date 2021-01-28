# This file is creatred by Rushabh Gandhi
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def analyze(request):

    # Get the text
    djtext = request.POST.get('text', 'default')
    #checkbox
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose1=""

    #functions for modifying text
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose1+="|Removed punctuations|"
        params = {'purpose':purpose1, 'analyzed_text': analyzed}
        djtext=analyzed

    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper() 
        purpose1+="|Upper case|"
        params = {'purpose':purpose1, 'analyzed_text': analyzed}
        djtext=analyzed
    
    if newlineremover=="on":
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
        purpose1+="|Removed NewLines|"
        params = {'purpose':purpose1, 'analyzed_text': analyzed}
        djtext=analyzed
        

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        purpose1+="|Removed extra spaces|"
        params = {'purpose':purpose1, 'analyzed_text': analyzed}
        

    if(extraspaceremover!="on"and newlineremover!="on" and fullcaps!="on"and removepunc != "on"):
        return HttpResponse("Please select a valid option")
    else:
        return render(request, 'analyze.html', params)
     