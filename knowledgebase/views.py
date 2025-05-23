from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import City, FAQ, BookingDetail
from .serializers import FAQSerializer, BookingDetailSerializer

@api_view(['GET'])
def get_faqs(request):
    city_name = request.GET.get('city')
    try:
        city = City.objects.get(name__iexact=city_name)
        faqs = FAQ.objects.filter(city=city)
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)
    except City.DoesNotExist:
        return Response({"error": "City not found"}, status=404)

@api_view(['GET'])
def get_booking_details(request):
    city_name = request.GET.get('city')
    try:
        city = City.objects.get(name__iexact=city_name)
        booking = BookingDetail.objects.get(city=city)
        serializer = BookingDetailSerializer(booking)
        return Response(serializer.data)
    except (City.DoesNotExist, BookingDetail.DoesNotExist):
        return Response({"error": "City or booking details not found"}, status=404)
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.logger import log_conversation

@api_view(['POST'])
def log_interaction(request):
    if log_conversation(request.data):
        return Response({"message": "Interaction logged successfully."})
    return Response({"message": "Logging failed."}, status=500)


from .utils.logger import log_post_call

@api_view(['POST'])
def post_call_analysis(request):
    if log_post_call(request.data):
        return Response({"message": "Post-call data logged."})
    return Response({"message": "Post-call logging failed."}, status=500)
