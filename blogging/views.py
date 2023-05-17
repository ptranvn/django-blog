from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" %  a for a in args])
    if kwargs:
        body += "Kwargs: \n"
        body += "\n".join(["\t%s: %s" % a for a in kwargs.items()])

    return HttpResponse(body, content_type="text/plain")