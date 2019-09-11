from django.contrib.auth import get_user_model  # If used custom user model

User = get_user_model()

from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ('id', 'password', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
