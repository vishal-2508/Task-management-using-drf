from rest_framework import serializers
from .models import User

class UserSerializers(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # print('password : ', password)
    class Meta:
        model = User
        fields = ['id', 'user_type', 'username', 'password', 'email', 'first_name', 'last_name' ]

    def create_user(self, user_data_dict):
        user = User.objects.create_user(
            username=user_data_dict['username'],
            password=user_data_dict['password'],
            first_name=user_data_dict.get('first_name'),
            last_name=user_data_dict.get('last_name'),
            user_type=user_data_dict.get('user_type'),
            email=user_data_dict.get('email')
        )
        return user





    # def create(self, validated_data):
    #     # print("val : ", validated_data)
    #     # print("val : ", type(validated_data))
    #     # print(validated_data['username'], type(validated_data['username']))
    #     # print(validated_data['password'], type(validated_data['password']))
    #     # print(validated_data.get('email'), type(validated_data.get('email')))
    #     # print(validated_data.get('user_type'), type(validated_data.get('user_type')))
    #     user = User.objects.create_user(
    #         username=validated_data['username'],
    #         password=validated_data['password'],
    #         first_name=validated_data.get('first_name'),
    #         last_name=validated_data.get('last_name'),
    #         user_type=validated_data.get('user_type'),
    #         email=validated_data.get('email')
    #     )
    #     return user
    