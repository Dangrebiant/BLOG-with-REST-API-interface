from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.serializers import (
	EmailField,
	CharField, 
	HyperlinkedIdentityField,
	ModelSerializer,
	SerializerMethodField,
	ValidationError
	)



User = get_user_model()

class UserDetailSerializer(ModelSerializer):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
		]

class UserCreateSerializer(ModelSerializer):
	email = EmailField(label = 'Email Address', )
	email2 = EmailField(label = 'Confirm Email')
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'email2',
			'password',
		]
		extra_kwargs = {"password":{"write_only":True}}
	#validation
	def validate_email(self, value):
		data = self.get_initial()
		email1 = data.get('email')
		email2 = value
		if email1 != email2:
			raise ValidationError("Emails must match.")

		user_qs = User.objects.filter(email = email2)
		if user_qs.exists():
			raise ValidationError("User with this email has already registered.")
		return value

	def create(self, validated_data):
		username = validated_data['username']
		email = validated_data['email']
		password = validated_data['password']
		user_obj = User(
			 username = username,
			 email = email
			)
		user_obj.set_password(password)
		user_obj.save()
		return validated_data

class UserLoginSerializer(ModelSerializer):
	token = CharField(allow_blank=True, read_only=True)
	username = CharField(required = False, allow_blank = True)
	email = EmailField(label = 'Email Address', required = False, allow_blank=True)
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'password',
			'token',
		]
		extra_kwargs = {"password":{"write_only":True}}
	
	def validate(self, data):
		user_obj = None
		email = data.get("email", None)
		username = data.get("username", None)
		password = data ["password"]
		if not email and not username:
			raise ValidationError("Email or Username is required to login.")
		user = User.objects.filter(
			Q(email = email)|
			Q(username = username)
			).distinct()
		#excluding users with empty emails
		user = user.exclude(email__isnull = True).exclude(email__iexact='')
		#checking if there is only 1 user
		if user.exists() and user.count() ==1:
			user_obj = user.first()
		else:
			raise ValidationError("This username /email is not valid.")
		if user_obj:
			if not user_obj.check_password(password):
				raise ValidationError("Wrong password")

		data["token"] = "14vGs6kgyw8yiwoYjN7WUWOdD4gYj41B"

		return data


