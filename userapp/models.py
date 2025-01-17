import uuid
from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.first_name + "  " + self.last_name


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    acc_no = models.IntegerField()
    pin = models.IntegerField()
    balance = models.IntegerField(validators=[MinValueValidator(2000)], default=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return str(self.acc_no)


class Transactions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    action = models.CharField(max_length=8, default='deposit')

    def __str__(self):
        return str(self.amount)+" "+self.action


class Transfer(models.Model):
    Transaction_Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions_sender')
    reciver = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions_reciver')
    amount = models.IntegerField(validators=[MinValueValidator(0)], default=0)

    def __str__(self):
        return "Sender : "+str(self.sender)+" , "+" Reciver : "+str(self.reciver)+" , "+" Amount : "+str(self.amount)