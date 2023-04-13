from django.shortcuts import render, HttpResponse
from home.models import Video, Image
# from .form import ImageForm
# from .forms import Video_form

# Create your views here.


def index(request):
    # if request.method == "POST":
    #     form = ImageForm(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         obj = form.instance
    #         return render(request, "index.html", {"obj": obj})
    # else:
    #     form = ImageForm()
    #     img = Image.objects.all()
    return render(request, 'index.html')


def gallery(request):
    img = Image.objects.all().last()
    vid = Video.objects.all().last()
    return render(request, 'gallery.html', {"img": img, 'vid': vid})


def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
    return render(request, 'appointment.html')

def contact(request):
    return render(request, 'contact.html')

def open(request):
    return render(request, 'open.html')

def photo(request):
    return render(request, 'photo.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def video(request):
    return render(request, 'video.html')