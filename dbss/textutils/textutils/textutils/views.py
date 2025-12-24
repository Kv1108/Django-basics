# created

from django.http import HttpResponse

'''
# website navigator
def index(request):
    return HttpResponse("""<h1> website navigator</h1> <a href='https://www.google.com'> Google</a> <a href='https://www.youtube.com'> Youtube</a> <a href = 'https://www.github.com'> Github </a>""")
'''

def index(request):
    return HttpResponse("""<h1> website navigator</h1> <a href='https://www.google.com'> Google</a> <a href='https://www.youtube.com'> Youtube</a> <a href = 'https://www.github.com'> Github </a>""")

def about(request):
    return HttpResponse("About")