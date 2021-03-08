from django.shortcuts import render


def home_page(request):
    my_title = "Welcome to Home Page"
    return render(request, "home_page.html", {"title": my_title})


def about_us(request):
    my_title = "Welcome to AboutUs Page"
    return render(request, "home_page.html", {"title": my_title})


def contact_us(request):
    my_title = "Welcome to ContactUs Page"
    return render(request, "home_page.html", {"title": my_title})
