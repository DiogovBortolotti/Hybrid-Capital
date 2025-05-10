from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser, Invitation
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'full_name']
        read_only_fields = ['id', 'email', 'full_name']


class InvitationSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    recipient = UserSerializer(read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Invitation
        fields = ['id', 'sender', 'recipient', 'status', 'status_display', 'created_at']
        read_only_fields = ['id', 'created_at']

class SendInvitationSerializer(serializers.Serializer):
    recipient_email = serializers.EmailField(write_only=True)
    
    def validate_recipient_email(self, value):
        try:
            recipient = CustomUser.objects.get(email=value)
            if Invitation.objects.filter(sender=self.context['request'].user, recipient=recipient).exists():
                raise serializers.ValidationError("Você já enviou um convite para este usuário.")
            return recipient
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("Usuário não encontrado.")

class HandleInvitationSerializer(serializers.Serializer):
    invitation_id = serializers.IntegerField()
    
    def validate_invitation_id(self, value):
        try:
            invitation = Invitation.objects.get(
                id=value,
                recipient=self.context['request'].user,
                status='pending'
            )
            return invitation
        except Invitation.DoesNotExist:
            raise serializers.ValidationError("Convite inválido ou já processado.")