from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadForm
from .models import Document

# Create your views here.

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if(form.is_valid()):
            newdoc = Document(filename = request.POST['filename'], docfile = request.FILES['docfile'])
            newdoc.save(form)
            return redirect("upload:uploadFile")
    else:
        form = UploadForm()
    return render(request, 'upload/upload.html', {'form':form})
            
                                
