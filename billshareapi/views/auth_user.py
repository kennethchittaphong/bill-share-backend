from billshareapi.models import User, AuthUser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.http import HttpResponseServerError
from rest_framework import serializers, status
import datetime
from django.core.exceptions import ObjectDoesNotExist

class AuthUserView(ViewSet):
    
    def retrieve(self, request, pk):
            
            try:
                authuser = AuthUser.objects.get(pk=pk)
                serializer = AuthUserSerializer(authuser)
                return Response(serializer.data)
            except Exception as ex:
                return HttpResponseServerError(ex)

    def list(self, request):
            
            authusers = AuthUser.objects.all()
            uid_query = request.query_params.get('uid', None)
            if uid_query is not None:
                authusers = authusers.filter(uid=uid_query)
            serializer = AuthUserSerializer(authusers, many = True)
            return Response(serializer.data)

    def create(self, request):
    
        
        
        uid = request.data['uid']

        # Use the built-in authenticate method to verify
        # authenticate returns the user object or None if no user is found
        try:
            user = AuthUser.objects.get(uid=uid)
            if user is None:
                print(user)
                return Response(user)
            else:
                print('user exist ===')
                print(user)
                AuthUser.objects.filter(uid=uid).update(
                    last_login = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                
                return Response('update success')

            # If authentication was successful, respond with their token
            data = { 'valid': False }
            return Response(data)
        except ObjectDoesNotExist:
            print('user login exception case ===')
            authuser = AuthUser.objects.create(
                uid = request.data["uid"],
                name = request.data["name"],
                email = request.data["email"],
                is_staff = request.data["is_staff"],
                is_active = request.data["is_active"],
                last_login = request.data["last_login"],
                is_superuser= request.data["is_superuser"],
                password = request.data["password"],
            )
            serializer = AuthUserSerializer(authuser)
            return Response(serializer.data)
        except Exception as e:
            print(repr(e))
            # Bad login details were provided. So we can't log the user in.
            data = { 'valid': False }
            return Response(data)
        

    def update(self, request, pk):
            
            authuser = AuthUser.objects.get(pk=pk)
            authuser.uid = request.data["uid"]
            authuser.save()

            return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):

            authuser = AuthUser.objects.get(pk=pk)
            authuser.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class AuthUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AuthUser
        fields = ('id', 'name', 'email', 'is_staff', 'is_active', 'last_login', 'is_superuser', 'password', 'uid') 
        depth = 1