from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer




class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,) 
    serializer_class = RegisterSerializer

class PatientViewSet(viewsets.ModelViewSet):
    """
    Handles all CRUD operations for Patients automatically.
    """
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated] 

    def get_queryset(self):
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class DoctorListCreateView(generics.ListCreateAPIView):
    """
    GET: Retrieve all doctors (Public)
    POST: Add a new doctor (Authenticated only)
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET, PUT, DELETE for a specific doctor.
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class MappingListCreateView(generics.ListCreateAPIView):
    """
    GET: Return all mapping relationships.
    POST: Assign a doctor to a patient.
    """
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]

class MappingDetailView(APIView):
    """
    Handles the overlapping URL structure requirement elegantly.
    GET /mappings/<id>/ -> Treats <id> as patient_id to return their doctors.
    DELETE /mappings/<id>/ -> Treats <id> as the mapping primary key to delete it.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        mappings = PatientDoctorMapping.objects.filter(patient_id=id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        mapping = get_object_or_404(PatientDoctorMapping, id=id)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)