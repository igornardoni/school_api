from django.contrib import admin
from django.urls import path, include
from school_api.views import (StudentsViewSet, CourseViewSet, RegistrationViewSet,
                              StudentRegistrationList, CourseRegistrationList)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('courses', CourseViewSet, basename='courses')
router.register('registrations', RegistrationViewSet, basename='registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/registrations/', StudentRegistrationList.as_view(),
         name='student-registrations'),
    path('course/<int:pk>/registrations/', CourseRegistrationList.as_view(),
         name='course-registrations'),
    path('api-auth/', include('rest_framework.urls')),
]

