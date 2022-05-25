from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from entries.models import EntryModel

from entries.api.serializers import EntrySerializer
from rest_framework import status
from rest_framework.renderers import JSONRenderer

class EntryListAPI(APIView):
    def get(self,request):
        entries = EntryModel.objects.all()
        serializer = EntrySerializer(entries, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=201)
        
        return Response(status=400, data=serializer.errors)
    
class EntryDetailAPI(APIView):
    def get(self, request, pk):
        entries = get_object_or_404(EntryModel, pk=pk)
        serializer = EntrySerializer(instance=entries)
        return Response(serializer.data)


    def put(self, request, pk):
        #entries = Entry.object.get(pk=pk)
        entries = get_object_or_404(EntryModel, pk=pk)
        serializer = EntrySerializer(instance=entries, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
        entries = get_object_or_404(EntryModel, pk=pk)
        entries.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    