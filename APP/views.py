from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def submit(request):
    if request.method == "POST":
        get_input = request.POST.get('inp')
        print(get_input)
    return render(request, 'about.html')
