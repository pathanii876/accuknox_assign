from django.shortcuts import render
from django.http import HttpResponse
from . models import SyncModel, TransModel
import time 
from .signals import thread_signal, transaction_signal
import threading
from django.db import transaction


def home_view(request):
    return render(request, 'signal_assignment/home.html')


def synchronization_test_view(request):
    start_time=time.time()
    print('synchronization test is running')
    print('creating MyModel instance')
    instance=SyncModel.objects.create(name='test1')
    print('created MyModel instance')
    end_time=time.time()
    total_time=end_time-start_time
    print(f'total time: {total_time:.2f} seconds')
    return HttpResponse("Synchronization Tested")


def threading_test_view(request):
    print('threading test is running')
    print(f'thread of caller : {threading.current_thread().name}')
    # emit signal
    thread_signal.send(sender=None)
    return HttpResponse("Same Thread Tested")


def transaction_test_view(request):
    with transaction.atomic():
        print('transaction test is running')
        trans = TransModel.objects.create(name='created by transaction test')
        print(f'instance created befor sending signal : {trans.name}')
        print(TransModel.objects.all())
        transaction_signal.send(sender=None)
        return HttpResponse('Transaction Test Done')
    

def check_trans_result_view(request):
    print(TransModel.objects.all())
    return HttpResponse('Trans Result Checked')

