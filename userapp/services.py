
from userapp.models import User
from random import randint
from userapp.serializer import AccountSerializer
from rest_framework.response import Response
from userapp.models import Account , User

def random_acc_no_generator():
    return randint(1000000000, 9999999999)

 
def create_acc_no(pk, pin):
    if User.objects.get(pk=pk).accounts.count() < 3:
        json_obj = {
                    'acc_no': random_acc_no_generator(), 
                    'pin': pin['pin'],
                    'balance': 2000,
                    'user': User.objects.get(pk=pk).pk ,
                }
        

        serialized = AccountSerializer(data=json_obj)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else : 
            return Response(serialized.errors)

    else :
        return Response("Cannot have more than 3 acocunts")
