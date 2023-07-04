from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import MenuItemSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuItemSerializer


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
	queryset = Menu.objects.all()
	serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
	queryset = Booking.objects.all()
	serializer_class = BookingSerializer