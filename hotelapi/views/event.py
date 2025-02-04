"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from hotelapi.models import Room
from hotelapi.models import Event
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class EventView(ViewSet):
    """Hotel booking event view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized event
        """
        
        try:
            event = Event.objects.get(pk=pk)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)



    def list(self, request):
        """Handle GET requests to get all events

        Returns:
            Response -- JSON serialized list of events
        """
        events = Event.objects.all()

        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized event instance or error message
        """
        try:
            event = Event.objects.create(
                event_name = request.data["event_name"],
                description=request.data["description"], 
                image_url=request.data["image_url"],
                date=request.data["date"],
                time=request.data["time"],
            )
            # Serialize and return the new event
            serializer = EventSerializer(event)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except KeyError as e:
   
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
        # Handle foreign key errors or other object issues
            return Response({"error": "Event not found"}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
        # Catch-all for any other errors
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    

    def update(self, request, pk):
        """Handle PUT requests for an event

        Returns:
           Response -- Empty body with 204 status code or error message
        """
        try:
            event = Event.objects.get(pk=pk)

            event.event_name=request.data["event_name"] 
            event.description=request.data["description"]
            event.image_url=request.data["image_url"]
            event.date=request.data["date"]
            event.time=request.data["time"]
            event.save()

            serializer = EventSerializer(event, data=request.data, partial=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Event.DoesNotExist:
            raise Http404("Event not found")
        except KeyError as e:
            return Response({"error": f"Missing field: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        try:
            event = Event.objects.get(pk=pk)
            event.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        

class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for events
    """
    class Meta:
        model = Event
        depth =1
        fields = ('id','event_name', 'description', 'image_url', 'date', 'time')
