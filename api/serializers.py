from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from home.models import Person
from home.models import Vehicle
from django.contrib.auth.models import User


class RegisterSerializersModel(ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            "password": {
                'write_only': True
            }
        }

    def create(self, validated_data):
        account = User(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password!= password2:
            raise serializers.ValidationError({'password': 'Password must match.'})
        account.set_password(password)
        account.save()
        return account


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField(max_length=50)


class PersonModelSerializer(ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    # def create(self, validated_data):
    #     email = validated_data['email']
    #     send_mail(email)
    #     return super.create(validated_data)
    #
    # def update(self, instance, validated_data):


class VehicleSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField()
    cost = serializers.IntegerField()


class VehicleModelSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'
