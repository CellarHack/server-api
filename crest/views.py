from django.shortcuts import render
from rest_framework import viewsets

from models import Metric, Event

class MetricViewSet(viewsets.ModelViewSet):

    model = Metric

class EventViewSet(viewsets.ModelViewSet):

    model = Event
