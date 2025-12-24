# created

from django.http import HttpResponse
from django.shortcuts import render

'''
# website navigator
def index(request):
    return HttpResponse("""<h1> website navigator</h1> <a href='https://www.google.com'> Google</a> <a href='https://www.youtube.com'> Youtube</a> <a href = 'https://www.github.com'> Github </a>""")


def about(request):
    return HttpResponse("About")

'''

def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

def analyze(request):
    #get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'remove punctuations', 'analyzed_text':analyzed}
    #analyze the text
    #return HttpResponse("Remove Punct <a href='/'> Back </a>")
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")

'''
def capfirst(request):
    return HttpResponse("Capitalize First <a href='/'> Back </a>")

def newlineremove(request):
    return HttpResponse("New Line Remove <a href='/'> Back </a>")

def spaceremov(request):
    return HttpResponse("Space Remove <a href='/'> Back </a>")

def charcount(request):
    return HttpResponse("Character Count <a href='/'> Back </a>")
''' 
