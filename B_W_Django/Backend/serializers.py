from rest_framework import serializers # immport seralizer of DJango rest frameowork.
from .models import reg
from django.contrib.auth.models import User # import user model here
from rest_framework.authtoken.views import Token
# its Model serializer one more serializer restframe have that is serializer.serialiozer.
# model serializer implemenent create and update method in seralizer class by default but in serializer.serializer we have create update and create method. for more read go to django restframework APi documentation
# in here create and update method implement by default. for update datac and create data in model.
class regSerializer(serializers.ModelSerializer):
    #The Meta class is important here because it defines the metadata information that our model has (database) and that must be converted to the Student class.
    class Meta:
        fields=( # here mention only those Fields of DB table which you want or like to pass frontend.
            'id',
            'Username',
            'email',
            
        )
        model=reg # mention which model you want to Serialize.


# here create serialier for Authtenticate with User table
# create Usertable seralizer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password']
        # this extra_kwargs use for what? - when user call api then password will show along with username . so we want when this API call password not show only username will show for this
        # we puted password is write only not for read and its required field.
        extra_kwargs ={'password':{
            'write_only':True,
            'required':True
        }}
    # this function became override here
    # why we use this function why it neccessory?
    # without this function our password save into normal string that string user passed from view or front end but we want save that password which sent by the user save in hase code.
    # so for saving password in password field in hasing format or hasing algo . so for this we are using below function.
    # one more task below func is doing for us. we know this application token base authentication. so we want wherever user register itself in this app. for that user token will created and assocaite to the user for further auth.
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        # create token for register user ..
        Token.objects.create(user=user) # if you want to see created token of the user go admin pannel in token sectionS
        return user