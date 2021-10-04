from django.shortcuts import render

# Create your views here.


def compte(request):
    context={}
    return render(request, "acrobat\\compte.html", context=context)
def creation(request):
    context={}
    return render(request, "acrobat\\creation.html", context=context)
def index(request):
    context={}
    return render(request, "acrobat\\index.html", context=context)
def panier(request):
    context={}
    return render(request, "acrobat\\panier.html", context=context)
def produit(request):
    context={}
    return render(request, "acrobat\\produit.html", context=context)
def Simu(request):
    context={}
    return render(request, "acrobat\\Simu.html", context=context)
def contact(request):
    context={}
    return render(request, "acrobat\\contact.html", context=context)
def cart(request):
    context={}
    return render(request, "acrobat\\cart.html", context=context)
    
