from django.urls import path 
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('Simu/', views.Simu, name = 'Simu'), 
    
   ]




Names = ['compte', "contact", 'creation', "index", "panier","produit","Simu","cart"]

for name in Names:
    urlpatterns.append(path(name+'/',getattr(views,name),name=name))

urlpatterns += staticfiles_urlpatterns()