from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from librarian.api.serializer import LibrarianSerializer
from librarian.models import Librarian


class LibrarianView(GenericAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

    def get(self, request):
        librarian = Librarian.objects.all()
        serializer = LibrarianSerializer(librarian, many=True)
        return Response(serializer.data, 200)

    def post(self, request):
        data = request.data
        serializer = LibrarianSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Librarian Successfully created"}, 201)
        else:
            return Response(serializer.errors, 422)

class LibrarianUpdateAndDelete(GenericAPIView):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSerializer

    def put(self, request, pk):
        librarian = Librarian.objects.get(id=pk)
        data = request.data
        serializer = LibrarianSerializer(librarian, data =data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message":"Librarian successfully updated!!"
            })
        else:
            return Response(serializer.errors,422)
        
    def delete(self, request, pk):
        librarian = Librarian.objects.filter(id=pk)
        librarian.delete()
        return Response({
            "message":"Librarian successfully deleted!!"
        },204)