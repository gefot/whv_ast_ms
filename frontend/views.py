from django.shortcuts import render

from modules import functions
from frontend.forms import DateForm


########################################################################################################################
def index(request):
    return render(request, 'base.html')


########################################################################################################################
def config_users(request):

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

    form = DateForm()
    date = ""
    record_list = []
    record_list_len = 0

    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']

    if date is not "":
        record_list = functions.get_recordings(date)
        record_list_len = len(record_list)

    context_dict = {'form': form, 'record_list': record_list, 'record_list_len': record_list_len}

    return render(request, 'mgmt/mgmt_recording.html', context_dict)


########################################################################################################################
def vm_info(request):
    context_dict = {}

    if request.method == 'POST':
        context_dict = {'device_info': "lala", 'device_info_len': 1}

    return render(request, 'vm/vm_info.html', context_dict)

########################################################################################################################
