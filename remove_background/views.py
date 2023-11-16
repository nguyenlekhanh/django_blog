from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadFileForm
from .rembg import remove
import os
from django.conf import settings
from io import BytesIO

# Create your views here.

def process_uploaded_file(file):
    # This function reads the content of the uploaded file into BytesIO.
    # You may customize this logic based on the type of file you expect.
    #content = BytesIO(file.read())
    #return content

    file_content = file.read()
    return file_content


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        # Assuming 'uploaded_file' is the name attribute of your file input in the form.
        uploaded_file =  request.FILES['file']

        # Process the uploaded file
        file_content = process_uploaded_file(uploaded_file)

        file_content = remove(file_content)

        # Create a response with the file content
        response = HttpResponse(file_content, content_type=uploaded_file.content_type)
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.name}"'

        return response
    else:
        form = UploadFileForm()
        # Render the form for users to submit
    return render(request, 'remove_background/upload.html', {'form': form})

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         file = request.FILES['file']
#         if form.is_valid():
#             handle_uploaded_file(request.FILES["file"])
#         #R = remove(file)
#         #R.save("img1.png")
#         return HttpResponse("The name of uploaded file is" + str(file))
#     else:
#         form = UploadFileForm()
#     return render(request, 'remove_background/upload.html', {'form': form})


# def handle_uploaded_file(f):
#     static_folder = "uploads"  # Specify the static folder within STATIC_ROOT
#     static_directory = os.path.join(settings.STATIC_ROOT, static_folder)

#     os.makedirs(static_directory, exist_ok=True)  # Create the directory if it doesn't exist

#     file_path = os.path.join(static_directory, f.name)

#     with open(file_path, "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

#     output_path = os.path.join(static_directory, 'output.png')
#     with open(file_path, 'rb') as i:
#         with open(output_path, 'wb') as o:
#             input = i.read()
#             output = remove(input)
#             o.write(output)

#     print(file_path)
#     return file_path  # Optionally, you can return the full file path
