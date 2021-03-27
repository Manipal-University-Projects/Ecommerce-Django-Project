from django.shortcuts import render

# Create your views here.


def index(request):
    context = {'data': [i for i in range(10)]}
    return render(request, 'Home/home_page.html', context=context)


def contact(request):
    return render(request, "Home/contact.html")


def about_us(request):
    return render(request, "Home/about_us.html")


def privacy_policy(request):
    return render(request, "Home/privacy_policy.html")
