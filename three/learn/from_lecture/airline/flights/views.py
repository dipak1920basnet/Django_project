from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from . models import Flight, Airport, Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html",
                  {
                      "flights":Flight.objects.all()
                  })


def flight(request, flight_id):
    flight = Flight.objects.get(id = flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flights = flight).all()
    return render(request, "flights/flight.html",
                  {
                      "flight":flight,
                      "passengers":passengers,
                      "non_passengers": non_passengers
                  })


def book(request, flight_id):

    if request.method == "POST":
        # Accessing the flight
        flight = Flight.objects.get(pk=flight_id)

        # Finding the passenger id from the submitted form data
        passenger_id = int(request.POST["passenger"])

        #Finding the passenger based on id
        passenger = Passenger.objects.get(pk=passenger_id)

        #Add passenger to the flight
        passenger.flights.add(flight)

        #Redirect user to flight pafe
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))