from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "my_to_do_app/index.html")
