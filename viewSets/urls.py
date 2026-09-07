from django.contrib import admin
from django.urls import path, include
# from .views import StudentList, StudentCreate, StudentRetrieve,StudentUpdate,StudentDestroy
from .views import LCStudentAPI, RUDStudentAPI, StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDestroy, StudentListCreate, StudentRetrieveUpdateDestroy, StudentViewSet, StudentModelViewSet, StudentModelViewSetRead
from .jwtviews import StudentModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

# router.register('studentapiview', StudentViewSet, basename='student')
# router.register('studentapiview', StudentModelViewSet, basename='student')
# router.register('studentapiview', StudentModelViewSetRead, basename='student')
router.register('jwt', StudentModelViewSet, basename='student')

urlpatterns = [
    # path('', StudentList.as_view()),
    # path('add/', StudentCreate.as_view()),
    # path('single/<int:pk>/', StudentRetrieve.as_view()),
    # path('update/<int:pk>/', StudentUpdate.as_view()),
    # path('delete/<int:pk>/', StudentDestroy.as_view()),
    path('studentapi/', LCStudentAPI.as_view()), 
    path('studentapirud/<int:pk>/', RUDStudentAPI.as_view()), 

    path('list/', StudentList.as_view()),
    path('create/', StudentCreate.as_view()),
    path('fetch/<int:pk>/', StudentRetrieve.as_view()),
    path('updates/<int:pk>/', StudentUpdate.as_view()),
    path('destroy/<int:pk>/', StudentDestroy.as_view()),
    path('updates/<int:pk>/', StudentUpdate.as_view()),
    path('destroy/<int:pk>/', StudentDestroy.as_view()),
    path('lcstudent/', StudentListCreate.as_view()),
    path('rudstudent/<int:pk>/', StudentRetrieveUpdateDestroy.as_view()),
    path('view/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),
]