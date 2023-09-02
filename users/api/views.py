from users.api.serializers import DoctorSerializer,DoctorProfileSerializer, DepartmentSerializer, PatientSerializer
from rest_framework import generics
from users.models import Doctor,Departments
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from users.models import User,DoctorProfile, Departments


class DoctorList(generics.ListAPIView):
    queryset = User.objects.filter(role="DOCTOR")
    serializer_class = DoctorSerializer
    permission_classes=[IsAuthenticated]

class OneDoctor(generics.RetrieveAPIView):
    queryset = DoctorProfile.objects.all()
    serializer_class = DoctorProfileSerializer
    # permission_classes=[IsAuthenticated]
    
    
class DepartmentList(generics.ListAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes=[IsAuthenticated]

class OneDepartment(generics.RetrieveAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    # permission_classes=[IsAuthenticated]

@api_view(['POST'])
def login_view(request):
    email= request.data['email']
    password= request.data['password']
    
    user = User.objects.filter(email=email).first()
    
    if user is None:
        raise AuthenticationFailed("User not found")
    
    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect password")
    
    return Response({
        'message':'Successfully logged_in'
    })
    
    
    
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_patients(request):
    if request.method == 'GET':
        patients= User.objects.filter(role="PATIENT")
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def patient_details(request,pk):
    try:
        patient= User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response({'message':'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PatientSerializer(patient)
        return Response(serializer.data)