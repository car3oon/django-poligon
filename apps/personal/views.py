from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'personal/index.html')


@login_required(login_url="/account/login/")
def contact(request):
    return render(request, 'personal/basic.html', {'content': [
        'Please contact me via this mail:',
        'car3on@gmail.com']})
