from django.shortcuts import render

from modules import functions
from frontend.forms import DateForm


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
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            test = form.cleaned_data['test']

    DATE = "20190522"
    record_list = functions.get_recordings("20190522")
    # for record in record_list:
    #     print(record)
    record_list_len = len(record_list)
    # print(record_list_len)
    context_dict = {'record_list': record_list, 'record_list_len': record_list_len}

    # if request.method == 'POST':
    #     context_dict = {'record_list': record_list, 'record_list_len': record_list_len}

    return render(request, 'mgmt/mgmt_recording.html', context_dict)


########################################################################################################################
def vm_info(request):
    context_dict = {}

    if request.method == 'POST':
        context_dict = {'device_info': "lala", 'device_info_len': 1}

    return render(request, 'vm/vm_info.html', context_dict)


########################################################################################################################
