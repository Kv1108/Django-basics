# created

from django.http import HttpResponse

'''
# website navigator
def index(request):
    return HttpResponse("""<h1> website navigator</h1> <a href='https://www.google.com'> Google</a> <a href='https://www.youtube.com'> Youtube</a> <a href = 'https://www.github.com'> Github </a>""")


def about(request):
    return HttpResponse("About")

'''

def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("Remove Punct")

def capfirst(request):
    return HttpResponse("Capitalize First")

def newlineremove(request):
    return HttpResponse("New Line Remove")

def spaceremov(request):
    return HttpResponse("Space Remove")

def charcount(request):
    return HttpResponse("Character Count")