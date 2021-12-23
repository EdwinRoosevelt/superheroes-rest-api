from rest_framework.views import APIView
from rest_framework.response import Response

class superheroes(APIView):

    def get(self, request, format=None):
        superheroes = [
            {
                "name": "Superman",
                "universe": "DC"
            }
        ]
        
        return Response({"superheroes": superheroes})
        