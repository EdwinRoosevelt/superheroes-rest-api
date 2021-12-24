from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from serializers import SuperHeroesSerializer

superheroes = [
            {
                "name": "Superman",
                "universe": "DC"
            }
        ]


class superheroes(APIView):

    def get(self, request, format=None):
        return Response({"superheroes": superheroes})

    def post(self, request):
        serializer = SuperHeroesSerializer(data=request)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'value received'
            return Response({'message': message})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        