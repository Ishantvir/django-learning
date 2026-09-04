from django.shortcuts import render
from  students.models import Student
from viewSets.serializers import StudentSerializer
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response

## GenericAPIView and ModelMixin

# class StudentList(GenericAPIView, ListModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

# class StudentCreate(GenericAPIView, CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
# class StudentUpdate(GenericAPIView,UpdateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

# class StudentDestroy(GenericAPIView, DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


## List and Create - PK not Required
class LCStudentAPI(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

### Retrieve Update and Delete - PK Required
class RUDStudentAPI(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer


### ViewSETS

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    def retrieve(self,request, pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer =  StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer =  StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Partial Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'message':'Data Deleted'})

#### Model Viewset Class
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentModelViewSetRead(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer