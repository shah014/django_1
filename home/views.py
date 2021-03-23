from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

# second way
# from django.http import HttpResponse
#
#
# def home(request):
#     response = HttpResponse()
#     response.content = "Hello World"
#     return response
# ....yo garepachi html file banauna pardaina



