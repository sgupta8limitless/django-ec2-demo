from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["get"])
def testingEndpoint(request):
    return Response({"message":"all Good working"})
