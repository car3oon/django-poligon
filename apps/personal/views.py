from django.shortcuts import render


def index(request):
    return render(request, 'personal/index.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content': [
        'Please contact me via this mail:',
        'car3on@gmail.com']})
