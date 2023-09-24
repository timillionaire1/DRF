from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from .models import Snippet
from .forms import MyForm

# Create your views here.
# def home(request):
#     details=MyForm(request.POST)
#     if request.method == 'POST':
#         # details=myForm(request.POST)
#         if details.is_valid():
#             details.save()
#             return
#         else:
#             template = loader.get_template('text.html')
#             return HttpResponse(template.render())
#             # return render(request, 'text.html')
#     else:
#         context={
#             'form':details
#         }
#         return render(request, 'text.html', context)


def home(request):
    if request.method == 'POST':
        details=MyForm(request.POST)
        if details.is_valid():
            details.save()
            return HttpResponse("data has been submitted")
        else:
            template = loader.get_template('text.html')
            return HttpResponse(template.render())
            # return render(request, 'text.html')
    else:
        details=MyForm()
        context={
            'form':details
        }
        return render(request, 'text.html', context)
