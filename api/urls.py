from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RegisterView, PatientViewSet,
    DoctorListCreateView, DoctorDetailView,
    MappingListCreateView, MappingDetailView
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth_login'),

    path('', include(router.urls)),
    path('doctors/', DoctorListCreateView.as_view(), name='doctor_list_create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),

    path('mappings/', MappingListCreateView.as_view(), name='mapping_list_create'),
    path('mappings/<int:id>/', MappingDetailView.as_view(), name='mapping_detail'),
]