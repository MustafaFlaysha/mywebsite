from django.shortcuts import render

# Create your views here.
def mywebsite_app(request):
    return render(request, 'hello_world.html', {})