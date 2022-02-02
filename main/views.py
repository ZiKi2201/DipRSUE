from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Applications
from .models import Reviews
from .forms import ReviewsForm
from .forms import ApplicationsForm

def index(request):
    review = Reviews.objects.all()
    application = Applications.objects.all()
    if request.method == 'POST':
        formRev = ReviewsForm(request.POST)
        formApp = ApplicationsForm(request.POST)
        if formRev.is_valid():
                formRev.save()
                return redirect('/')
        else:
            formRev.add_error(None, 'Ошибка добавления отзыва')
        if formApp.is_valid():
            formApp.save()
            return redirect('/')
        else:
            formApp.add_error(None, 'Ошибка добавления отзыва')
    formRev = ReviewsForm()
    formApp = ApplicationsForm()
    data = {
        'review': review,
        'application': application,
        'formRev': formRev,
        'formApp': formApp
        }
    return render(request, 'main/index.html', data)
