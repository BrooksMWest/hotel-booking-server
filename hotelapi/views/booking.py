"""View module for handling requests about booking """
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hotelapi.models import Event, Booking



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
    
    def create(self, request, *args, **kwargs):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        # Here I am 
        event_id = request.data.get("event")  # Use `.get()` to avoid KeyError

        if not event_id or not Event.objects.filter(id=event_id).exists():
            return Response({"error": "Invalid event ID"}, status=status.HTTP_400_BAD_REQUEST)

        event = Event.objects.get(id=event_id)


        booking = Booking.objects.create(
            paid=request.data["paid"],
            number_of_party=request.data["number_of_party"],
            check_in_date=request.data["check_in_date"],
            check_out_date=request.data["check_out_date"],
            event=event,
            uid=request.data["uid"]
        )
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    
    def update(self, request, pk, *args, **kwargs):
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
        booking.uid = request.data["uid"]
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
        fields = ('id', 'paid', 'number_of_party', 'check_in_date', 'check_out_date', 'event', 'uid')
