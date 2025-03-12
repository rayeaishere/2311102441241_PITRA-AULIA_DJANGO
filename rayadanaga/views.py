from django.shortcuts import render

def home(request):
    template_name = "home.html"
    context = {
        'title':'welcome',
        'description': 'your fashion lookbook',
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        'title':'website kami bla bla bla',
        'description' : 'blablabla',
    }
    return render(request, template_name, context)
