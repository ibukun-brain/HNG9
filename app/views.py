from app.models import HNGProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import HNGProfileSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    profile = HNGProfile.objects.get(pk=1)
    serializer = HNGProfileSerializer(profile, many=False)
    return Response(serializer.data)
