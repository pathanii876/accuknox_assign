from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
import time
from .models import SyncModel
import threading


@receiver(post_save, sender=SyncModel)
def after_instance(sender, instance, created, **kwargs):
    print(f'signal received when instance {instance.name} is created')
    print('waiting for signal to finish its job')
    time.sleep(4)
    print('signal processing completed')


# define a custom signal
thread_signal = Signal()

@receiver(thread_signal)
def signal_handler(sender, **kwargs):
    print(f'signal running in a thread : {threading.current_thread().name}')


transaction_signal = Signal()

@receiver(transaction_signal)
def transaction_signal_handler(sender, **kwargs):
    raise Exception('****Intentional Error****')