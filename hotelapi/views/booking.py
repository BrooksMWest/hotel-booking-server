"""View module for handling requests about booking """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hotelapi.models import Event
from hotelapi.models import Booking



class BookingView(ViewSet):
    """Level up booking  view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single booking 

        Returns:
            Response -- JSON serialized booking 
        """
        # Here we are getting a single booking by the primary key (pk) 
        booking = Booking.objects.get(pk=pk)
        # sending it to our serializer to be converted to useable json
        serializer = BookingSerializer(booking)
        # then returing the serialzed data
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all booking  

        Returns:
            Response -- JSON serialized list of booking 
        """
        #Booking is a variable stores the data accessed through our bookings model in this case we are accessing all of the data
        book = Booking.objects.all()
        
         #This is serializing the data and converting it to a json    
        serializer = BookingSerializer(book, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        # Here I am 
        event = Event.objects.get(id=request.data["event"])

        book = Booking.objects.create(
            sale=request.data["sale"],
            number_of_party=request.data["number_of_party"],
            check_in_date=request.data["check_in_date"],
            check_out_date=request.data["check_out_date"],
        )
        serializer = BookingSerializer(book)
        return Response(serializer.data)
    
    
    def update(self, request, pk):
        """Handle PUT requests for a book"""

        # Fetch the book to be updated
        booking = Booking.objects.get(pk=pk)

        # Fetch the event based on the `event` field
        event = Event.objects.get(pk=request.data["event"])

        # Update book details
        booking.paid = request.data["paid"]
        booking.number_of_party = request.data["number_of_party"]
        booking.check_in_date = request.data["check_in_date"]
        booking.check_out_date = request.data["check_out_date"]
        booking.event = event  # Update the event relationship
        booking.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        book = Booking.objects.get(pk=pk)
        book.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        

        
class BookingSerializer(serializers.ModelSerializer):
    """JSON serializer for booking
    """
    class Meta:
        model = Booking
        fields = ('paid', 'number_of_party', 'check_in_date', 'check_out_date', 'event')