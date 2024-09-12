
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated 
from rest_framework import permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
  
class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response({'status': True, 'data': content},status=status.HTTP_200_OK)
    
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from users.serializers import CustomLoginSerializer

class CustomLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        field_errors = ', '.join(serializer.errors.keys())
        return Response(field_errors, status=status.HTTP_200_OK)