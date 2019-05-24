from django.shortcuts import render
from django.http import HttpResponse

from modules import functions


# Create your views here.
def index(request):
    return render(request, 'base.html')


########################################################################################################################
def config_users(request):
    context_dict = {}

    users = functions.get_users()
    num_of_users = len(users)
    for user in users:
        print(user)
    context_dict = {'users': users, 'num_of_users': num_of_users}

    return render(request, 'config/config_users.html', context_dict)


########################################################################################################################
def mgmt_cdr(request):
    context_dict = {}

    if request.method == 'POST':
        context_dict = {'device_info': "lala", 'device_info_len': 1}

    return render(request, 'mgmt/mgmt_cdr.html', context_dict)


def mgmt_logs(request):
    context_dict = {}

    if request.method == 'POST':
        context_dict = {'device_info': "lala", 'device_info_len': 1}

    return render(request, 'mgmt/mgmt_logs.html', context_dict)


def mgmt_recording(request):
    context_dict = {}

    if request.method == 'POST':
        context_dict = {'device_info': "lala", 'device_info_len': 1}

    return render(request, 'mgmt/mgmt_recording.html', context_dict)


########################################################################################################################
def vm_info(request):
    context_dict = {}

    if request.method == 'POST':
        context_dict = {'device_info': "lala", 'device_info_len': 1}

    return render(request, 'vm/vm_info.html', context_dict)

########################################################################################################################
