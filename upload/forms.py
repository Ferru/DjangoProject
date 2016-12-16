from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_lenght=50)
    file = form.FileField()
