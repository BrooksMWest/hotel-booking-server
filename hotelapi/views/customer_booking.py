"""View module for handling requests about books"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hotelapi.models import Customer
from hotelapi.models import Booking
from hotelapi.models import CustomerBooking
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class CustomerBookingView(ViewSet):
    """customer booking view"""

    def retrieve(self, request, pk):
        """Handle GET requests for different customers that are on a booking

        Returns:
            Response -- JSON serialized customers on a booking
        """
        customerBooking = CustomerBooking.objects.get(pk=pk)
        serializer = CustomerBookingSerializer(customerBooking)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all customer bookings

        Returns:
            Response -- JSON serialized list of customer bookings
        """
        customerBookings = CustomerBooking.objects.all()


        serializer = CustomerBookingSerializer(customerBookings, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized customer instance or error message
        """
        try:
            customerBooking = CustomerBooking.objects.create(
                customer_id=request.data["customer_id"],
                booking_id=request.data["booking_id"],  
            )

            # Serialize and return the new book
            serializer = CustomerBookingSerializer(customerBooking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
        # Handle missing fields
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
        # Handle foreign key errors or other object issues
            return Response({"error": "Customers, bookings, or related object not found."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
        # Catch-all for any other errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def update(self, request, pk):
        """Handle PUT requests for the genres on a book

        Returns:
           Response -- Empty body with 204 status code or error message
        """
        try:
            customerBooking = CustomerBooking.objects.get(pk=pk)
            customerBooking.customer_id = request.data["customer_id"]
            customerBooking.booking_id = request.data["booking_id"]  # Ensure the key matches your frontend
            customerBooking.save()

            serializer = CustomerBookingSerializer(customerBooking)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Customer.DoesNotExist:
            raise Http404("The customers for this booking can not be found")
        except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        customerBooking = CustomerBooking.objects.get(pk=pk)
        customerBooking.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        

class CustomerBookingSerializer(serializers.ModelSerializer):
    """JSON serializer for customer bookings
    """
    customer = serializers.PrimaryKeyRelatedField(read_only=True)
    booking = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CustomerBooking
        fields = ('id','customer', 'booking')
