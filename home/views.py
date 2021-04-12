from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Person
# Create your views here.


def home(request):
    # print(request.GET.get('hello'))
    # print(request.scheme)
    # print(request.path)
    # print(request.method)
    # a = request.GET.get('show')
    person_info = [{'name':'Anil', 'address': 'Kapan', 'age': 24},
                   {'name':'Anup', 'address': 'chabahil', 'age': 24},
                   {'name':'Labin', 'address': 'Kapan', 'age': 24}
                   ]
    # # return JsonResponse({'year': year})
    # return render(request, template_name='slider2.html', context={'person_info': person_info})
    return render(request, template_name='base.html', context={'person_info': person_info})

# second way
# from django.http import HttpResponse
#
#
# def home(request):
#     response = HttpResponse()
#     response.content = "Hello World"
#     return response
# ....yo garepachi html file banauna pardaina


def form1(request):
    # print(request.method)
    # return render(request, template_name='form1.html')

    if request.method.lower() == 'post':
        name = request.POST['name']
        address = request.POST['address']
        age = request.POST['age']
        email = request.POST['email']
        Person.objects.create(name=name, address=address, age=age, email=email)
        return redirect('home')
    return render(request, template_name='form1.html')




