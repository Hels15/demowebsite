from django.shortcuts import render


def home_view(request):
    return render(request,"home.html")
def contact_view(request):
    return render(request,"contact.html")
def about_view(request):
    return render(request,"about.html")
# Create your views here.
