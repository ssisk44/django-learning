from django.http import HttpResponse


def home_view(request):
    """ Create a function view to return http response """
    return HttpResponse("<h1>Hello World!</h1><p>Hi there</p>")