from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.management import call_command
from django.conf import settings
from django.contrib import messages

from dataentry.utils import check_csv_errors, get_all_custom_models
from dataentry.tasks import import_data_task, export_data_task
from dataentry.forms import CompressImageForm
from dataentry.models import Upload

from PIL import Image
import io


def students(request):
    students = [
        {'id':1, 'name': 'ahmed shalan', 'age': 45}
    ]
    return HttpResponse(students)


def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES.get('file_path')
        model_name = request.POST.get('model_name')
        
        # store this file inside the Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)

        # construct the full path
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        
        file_path = base_url+relative_path

        # check for the csv errors
        try:
            check_csv_errors(file_path, model_name)
        except Exception as e:
            messages.error(request, str(e))
            return redirect('import_data')

        # handle the import data task here
        import_data_task.delay(file_path, model_name)
        
        # show the message to the user
        messages.success(request, 'Your data is being imported, you will be notified once it is done.')
        return redirect('import_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/importdata.html', context)


def export_data(request):
    if request.method == 'POST':
        model_name = request.POST.get('model_name')

        # call the export data task
        export_data_task.delay(model_name)

        # show the message to the user
        messages.success(request, 'Your data is being exported, you will be notified once it is done.')
        return redirect('export_data')
    else:
        custom_models = get_all_custom_models()
        context = {
            'custom_models': custom_models,
        }
    return render(request, 'dataentry/exportdata.html', context)


def compress(request):
    user = request.user
    if request.method == 'POST':
        form = CompressImageForm(request.POST, request.FILES)
        if form.is_valid():
            original_img = form.cleaned_data['original_img']
            quality = form.cleaned_data['quality']

            compressed_image = form.save(commit=False)
            compressed_image.user = user

            # perform compression
            img = Image.open(original_img)

            output_format = img.format
            buffer = io.BytesIO()
            img.save(buffer, format=output_format, quality=quality)
            buffer.seek(0)
            
            # save the compressed image inside the model
            compressed_image.compressed_img.save(
                f'compressed_{original_img}', buffer
            )

            # Automatically download the compressed file
            response = HttpResponse(buffer.getvalue(), content_type=f'image/{output_format.lower()}')
            response['Content-Disposition'] = f'attachment; filename=compressed_{original_img}'
            return response
            # return redirect('compress')
    else:
        form = CompressImageForm()
        context = {
            'form': form,
        }
        return render(request, 'image_compression/compress.html', context)