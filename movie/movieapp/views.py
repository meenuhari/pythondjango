from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import  Movie
from .forms import Movieform
# Create your views here.
# def home(request):
#     k = Movie.objects.all()
#     return render(request,template_name="home.html",context={'movie':k})

class MovieList(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movielist"


# def addmovie(request):
#     if (request.method == "POST"):
#         n = request.POST['n']
#         d = request.POST['d']
#         y = request.POST['y']
#
#         i = request.FILES['i']
#         b = Movie.objects.create(name=n,desc=d, year=y,  img=i)
#         b.save
#         return home(request)
#     return render(request,template_name="addmovie.html")

class  Movieadd(CreateView):
    model = Movie
    template_name = "addmovie.html"
    fields = '__all__'
    success_url = reverse_lazy('home')







# def viewdetail(request,p):
#     b = Movie.objects.get(id=p)
#     return render(request, template_name="viewdetail.html",context={'movie':b})
class MovieDetail(DetailView):
    model=Movie
    template_name="viewdetail.html"
    context_object_name = "movie"


# def editdetail(request,p):
#     b = Movie.objects.get(id=p)
#     if (request.method == "POST"):  # creates form object initialized with values inside request.POST
#         form = Movieform(request.POST, request.FILES, instance=b)
#         if form.is_valid():
#             form.save()  # saves form object inside db table
#         return home(request)
#
#     form = Movieform(instance=b)
#
#     return render(request,template_name="edit.html",context={'form':form})
class  MovieEdit(UpdateView):
    model = Movie
    template_name = "edit.html"
    fields = '__all__'
    success_url = reverse_lazy('home')

# def delete(request,id):
#     if(request.method==)



class Moviedelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('home')
    template_name = "delete.html"
