from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from home.models import Person
from .serializers import PersonSerializer, PersonModelSerializer
from rest_framework import status
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, \
    DestroyAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from home.models import Vehicle
from .serializers import VehicleModelSerializer
from rest_framework.viewsets import ModelViewSet
from .mixins import ListUpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view
from .serializers import RegisterSerializersModel
from django.contrib.auth.models import User
from .permissions import IsSystemAdmin


def registration_view(request):
    # if request.method==['POST']:
    ser = RegisterSerializersModel(data=request.data)
    data = {}
    if ser.is_valid():
        account = ser.save()
        # data['response'] = 'Successfully registered new user'
        # data['username'] = account.username
        # data['email'] = account.email
    else:
        data = ser.errors
    return Response(ser.data)


class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializersModel
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class RegisterUser(CreateAPIView):
    serializer_class = RegisterSerializersModel
    queryset = User.objects.all()


class BookView(APIView):
    def get(self, *args, **kwargs):
        r = {'b_name': 'Maths', 'b_author': 'Karan'}
        return Response(r)


# class PersonView(APIView):
#     def get(self, *args, **kwargs):
#         p = Person.objects.all()
#         serializer = PersonSerializer(p, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         print(data)
#         ser = PersonSerializer(data=data)
#         if ser.is_valid():
#             v_data = ser.validated_data
#             Person.objects.create(**v_data)
#             return Response({
#                 "message": "Added Successfully",
#                 "data": v_data
#
#             }, status=status.HTTP_201_CREATED)
#         return Response({
#             "message": "Something went wrong"
#         }, status=status.HTTP_400_BAD_REQUEST)

class PersonView(APIView):
    def get(self, *args, **kwargs):
        p = Person.objects.all()
        serializer = PersonModelSerializer(p, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        ser = PersonModelSerializer(data=data)
        if ser.is_valid():
            v_data = ser.validated_data
            # Person.objects.create(**v_data)
            ser.save()
            return Response({
                "message": "Added Successfully",
                "data": v_data

            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)


class PersonGenericView(ListAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonModelSerializer
    queryset = Person.objects.all()


class VehicleView(APIView):
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsSystemAdmin]
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsSystemAdmin]
        else:
            permissions = [IsAuthenticated]
        return [permissions() for permission in permissions]

    def get(self, *args, **kwargs):
        s = Vehicle.objects.all()
        serializer = VehicleModelSerializer(s, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        ser = VehicleModelSerializer(data=data)
        if ser.is_valid():
            v_data = ser.validated_data
            ser.save()
            return Response({
                "message": "Added Successfully",
                "data": v_data

            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Something went wrong"
        }, status=status.HTTP_400_BAD_REQUEST)


class VehicleGenericView(ListAPIView):
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()


class VehicleCreateView(CreateAPIView):
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()


class VehicleUpdateView(UpdateAPIView):
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()


class VehicleDestroyView(DestroyAPIView):
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()


# class VehicleRetrieveUpdateView(RetrieveUpdateAPIView):
#     serializer_class = VehicleModelSerializer
#     queryset = Vehicle.objects.all()
#
#
# class VehicleRetrieveDestroyView(RetrieveDestroyAPIView):
#     serializer_class = VehicleModelSerializer
#     queryset = Vehicle.objects.all()

class VehicleModelViewSet(ModelViewSet):
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()


class VehicleListModelViewSet(ListUpdateModelMixin):
    serializer_class = VehicleModelSerializer
    queryset = Vehicle.objects.all()
