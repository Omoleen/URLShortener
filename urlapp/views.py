from django.shortcuts import render, redirect
import uuid
import string
import random
from .models import Urlsmodel
from URLShortener.settings import BASE_URL


# Create your views here.
def shortener(request, *args, **kwargs):
    print(Urlsmodel.objects.all())
    if 'code' not in kwargs.keys():
        return render(request, 'shortener.html')
    else:
        originalinst = Urlsmodel.objects.get(shortened=str(kwargs.get('code')).lower())
        print(originalinst.original)
        # return redirect(originalinst.original)
        if 'http://' not in originalinst.original or 'https://' not in originalinst.original:
            return redirect('http://' + originalinst.original)
        else:
            return redirect(originalinst.original)


def shortenerhtmx(request):
    original = request.POST.get('original')
    print(original)
    result_str = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
    print(result_str)
    Urlsmodel.objects.create(original=original, shortened=result_str)
    link = BASE_URL+result_str
    return render(request, 'result.html', {'link': link})
