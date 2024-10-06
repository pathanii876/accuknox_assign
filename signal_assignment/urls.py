from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name = 'home'),
    path('sync_test/', synchronization_test_view, name= 'sync_test' ),
    path('thread_test/', threading_test_view, name= 'thread_test' ),
    path('trans_test/', transaction_test_view, name= 'trans_test' ),
    path('check_trans/', check_trans_result_view, name= 'check_trans' ),
]