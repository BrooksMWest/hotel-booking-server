"""View module for handling requests about rooms"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hotelapi.models import Room
from hotelapi.models import Booking
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class RoomView(ViewSet):
    """Level up room view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single room

        Returns:
            Response -- JSON serialized room
        """
        
        try:
            room = Room.objects.get(pk=pk)
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)



    def list(self, request):
        """Handle GET requests to get all rooms

        Returns:
            Response -- JSON serialized list of rooms
        """
        rooms = Room.objects.all()

        booking = request.query_params.get('booking', None)
        if booking is not None:
            rooms = rooms.filter(booking=booking)


        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized room instance or error message
        """
        try:
            booking = Booking.objects.get(pk=request.data["booking_id"])
            room = Room.objects.create(
                room_number = request.data["room_number"],
                vacancy=request.data["vacancy"],  # Ensure the key matches your frontend
                room_size=request.data["room_size"],
                star_rating=request.data["star_rating"],
                price=request.data["price"],
                good_view=request.data["good_view"],
                smoking=request.data["smoking"],
                booking=booking
            )
            # Serialize and return the new book
            serializer = RoomSerializer(room)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
   
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
        # Handle foreign key errors or other object issues
            return Response({"error": "Booking or related object not found."}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
        # Catch-all for any other errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def update(self, request, pk):
        """Handle PUT requests for a room

        Returns:
           Response -- Empty body with 204 status code or error message
        """
        try:
            room = Room.objects.get(pk=pk)

            # booking_id = request.data.get("booking_id")
            # if booking_id:
            #     try:
            #         booking = Booking.objects.get(pk=booking_id)
            #         room.booking = booking
            #     except Booking.DoesNotExist:
            #         return Response({"error": "Invalid booking_id, booking not found."}, status=status.HTTP_400_BAD_REQUEST)
            booking = Booking.objects.get(pk=request.data["booking"])

                
            room.room_number=request.data["room_number"] 
            room.vacancy=request.data["vacancy"]
            room.room_size=request.data["room_size"]
            room.star_rating=request.data["star_rating"]
            room.price=request.data["price"]
            room.good_view=request.data["good_view"]
            room.smoking=request.data["smoking"]
            room.booking=booking
            room
            room.save()

            serializer = RoomSerializer(room)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Room.DoesNotExist:
            raise Http404("Room not found")
        except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        try:
            room = Room.objects.get(pk=pk)
            room.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Room.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)

        

class RoomSerializer(serializers.ModelSerializer):
    """JSON serializer for rooms
    """
    class Meta:
        model = Room
        depth =1
        fields = ('id','room_number', 'vacancy', 'room_size', 'star_rating', 'price', 'good_view', 'smoking', 'booking')
