from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        urm_no =request.POST.get('urmNo')
        print(urm_no)
    return render(request,'ocr_form.html')
