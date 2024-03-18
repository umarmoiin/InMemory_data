from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.conf import settings
from django.contrib import messages

import os
import atexit
import json


def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            key_input = form.cleaned_data['key']
            value_input = form.cleaned_data['value']

            # Retrieve existing data from TEMPORARY_DATA
            temporary_data = getattr(settings, 'TEMPORARY_DATA', None)
            
            # Add new data to the dictionary with user-provided key
            temporary_data[key_input] = value_input
            
            # Store the updated dictionary in TEMPORARY_DATA
            settings.TEMPORARY_DATA = temporary_data
            
            # Store data in the database (Task model)
            # Task.objects.create(user_input=user_input, user_input2=user_input2)

            return redirect('home')  # Redirect to the same page to display the output
    else:
        form = TaskForm()

    # Retrieve data from settings
    temporary_data = getattr(settings, 'TEMPORARY_DATA', None)

    # Retrieve data from the database
    db_data = Task.objects.all()

    context = {'form': form, 'temporary_data': temporary_data, 'db_data': db_data}

    return render(request, 'home.html', context)

def load_temporary_data_from_file():
    # Specify the file path where the data is saved
    file_path = 'temporary_data.json'

    # Check if the file exists before attempting to read it
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                # Load the data from the file into TEMPORARY_DATA
                temporary_data = json.load(file)
                settings.TEMPORARY_DATA = temporary_data
            except json.JSONDecodeError:
                # Handle the case where the file contains invalid JSON
                pass

# Call the function when the module is loaded
load_temporary_data_from_file()

def save_temporary_data_to_file():
    # Retrieve data from TEMPORARY_DATA
    temporary_data = getattr(settings, 'TEMPORARY_DATA', {})
    
    file_path = 'temporary_data.json'
    try:
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = {}

    # Merge the existing data with the new data
    
    merged_data = existing_data.copy()
    merged_data.update(temporary_data)

    # Save the dictionary to a file (you can choose the file path and format)
    with open(file_path, 'w') as file:
        json.dump(merged_data, file)
        print("Sucessfully saved")

# When sever is terminated the save_temporary_data_to_file is executed
atexit.register(save_temporary_data_to_file)

def FileUpload(request, *args, **kwargs):
    file_paths =[]

    if request.method == 'POST':
        form1 = UploadTestFileForm(request.POST, request.FILES)
        print("Uploaded")
        if form1.is_valid():
            print(request.FILES)
            files = request.FILES.getlist('file')
            
            for fi in files:
                file_path = os.path.join(settings.MEDIA_ROOT, fi.name)
                with open(file_path, 'wb+') as f:
                    for chunk in fi.chunks():
                        f.write(chunk)
                file_paths.append(file_path)
            messages.success(request, 'Files uploaded successfully.')
            
    else:
        form1 = UploadTestFileForm()
    
    context = {'form1': form1, 'file_paths': file_paths} 
    return render(request, 'fileupload.html', context)
