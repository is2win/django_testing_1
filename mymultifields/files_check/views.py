from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocCheckForm
from django.views.generic.base import TemplateView
from .models import DocCheck, CheckerFiles
from appmulti.models import Forward, Option

def model_form_upload(request):
    if request.method == 'POST':
        form = DocCheckForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index.html')
    else:
        form = DocCheckForm()
    context = {
        'form': form
    }
    return render(request, 'files_check/upload.html', context=context)


class MainPage(TemplateView):
    template_name = 'files_check/index.html'


def take_files_two(request, pk):
    files_obj = get_object_or_404(DocCheck, pk=pk)
    if files_obj.file_mssp:
        result = 'Сверка завершена'
    else:
        result = 'Error - no file'
    checking = CheckerFiles(title=files_obj.title + ' check', dock_check=files_obj, result=result)
    checking.save()
    forwards = Forward.objects.all()
    context = {
        'checking': checking,
        'forwards': forwards,
    }
    return render(request, 'files_check/check_info.html', context=context)

