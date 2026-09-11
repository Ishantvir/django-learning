from django.shortcuts import render
from  students.models import Student
from viewSets.serializers import StudentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .mypagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .throttling import auraRateThrottle

#Pagination, Permission and Authentication
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [JWTAuthentication]
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    pagination_class = MyCursorPagination


## Filtering
class StuList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user_id = user)

### Django-filter
class Studjfilter(ListAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city']

### search-filter
class searchf(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [SearchFilter]
    # search_fields = ['name']
    search_fields = ['^name']

### ordering-filter
class orderingf(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    filter_backends = [OrderingFilter]
    # ordering_fields = ['name', 'city]
    ordering_fields = '__all__'

''' All filtering concept'''
class filterOrderSearch(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(user_id = user)

    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['id', 'name', 'city', 'age']
    search_fields = ['^name', '^city']
    ordering_fields = ['id', 'name', 'city']

class StudentThrottling(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [AnonRateThrottle,UserRateThrottle]
    throttle_classes = [AnonRateThrottle, auraRateThrottle]