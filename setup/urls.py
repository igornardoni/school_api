from django.contrib import admin
from django.urls import path, include
from school_api.views import StudentsViewSet, CourseViewSet, RegistrationViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('registrations', RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
