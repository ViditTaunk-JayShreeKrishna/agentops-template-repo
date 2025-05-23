from django.urls import path
from . import views

urlpatterns = [
    path('get-faqs/', views.get_faqs),
    path('get-booking-details/', views.get_booking_details),
    path('log-interaction/', views.log_interaction),
    path('post-call/', views.post_call_analysis),
]
