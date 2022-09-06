from audioop import maxpp
from datetime import date, datetime
from distutils.command.upload import upload
from inspect import signature
from locale import currency
from operator import length_hint
from django.db import models



# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=20)
    gend=(
        ('m','Male'),
        ('f','Female')
    )
    gender=models.CharField(choices=gend,max_length=7)
    address = models.TextField()
    age = models.PositiveSmallIntegerField()
    nationality =models.CharField(max_length=15)
    email = models.EmailField()
    signature=models.ImageField(default='default.jpg', upload_to="headshot")
    
class Account(models.Model):
    account_number=models.IntegerField()
    account_name=models.CharField(max_length=15)
    balance=models.IntegerField()
    pin=models.PositiveSmallIntegerField()
    
class Wallet(models.Model):
    balance=models.IntegerField()
    customer=models.ForeignKey(on_delete=models.CASCADE,to=Customer)
    amount=models.BigIntegerField()
    account_pin=models.PositiveIntegerField()
    currency=models.CharField(max_length=15)
    account=models.ForeignKey(on_delete=models.CASCADE,to=Account) 
      
class Transaction(models.Model):
    wallet=models.ForeignKey(on_delete=models.CASCADE,to=Wallet)
    transaction_amount=models.IntegerField()
    transaction_number=models.IntegerField()
    transaction_type=models.CharField(max_length=15)
    origin_account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="Transaction_original_account")
    destination=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="Transaction_destination")
    transaction_charge=models.IntegerField()
    date_time=models.DateTimeField(default=datetime.now)
  
class Card(models.Model):
    card_number=models.IntegerField()
    card_pin =models.IntegerField()
    debit_card=models.CharField(max_length=10)
    credit_card=models.CharField(max_length=12)
    date_issued=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey(on_delete=models.CASCADE,to=Wallet)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="account_b")
    issuer=models.CharField(max_length=7)
    # signature=models.ImageField()
    
class ThirdPary(models.Model):
    nameof_thirdparty=models.CharField(max_length=13)
    account=models.ForeignKey(on_delete=models.CASCADE,to=Account)
    transaction_account=models.IntegerField()
    location=models.CharField(max_length=15)
    currency=models.CharField(max_length=12)
    id=models.CharField(max_length=10,primary_key=True)
    
    
class Receipt(models.Model):
    receipt_type=models.CharField(max_length=10)
    receipt_date=models.DateTimeField(default=datetime.now)
    bill_number=models.IntegerField()
    total_amount=models.IntegerField()
    # file=models.FileField()
    
class Notification(models.Model):
    message=models.TextField(max_length=100)
    title=models.CharField(max_length=10)
    datetime=models.DateTimeField(default=datetime.now)
    recipient=models.ForeignKey(on_delete=models.CASCADE,to=Receipt)
    status=models.CharField(max_length=11)
    
class Loan(models.Model):
    loan_id=models.IntegerField(primary_key=True)
    wallet=models.ForeignKey(on_delete=models.CASCADE,to=Wallet)
    loan_type=models.CharField(max_length=20)
    amount=models.BigIntegerField()
    loan_balance=models.IntegerField()
    interst_rate=models.IntegerField()
    payment_duedate=models.DateTimeField(default=datetime.now)
    
    
class Reward(models.Model):
    name=models.CharField(max_length=12)
    customer_id=models.IntegerField()
    gender_1=models.CharField(max_length=11)
    zpoints=models.IntegerField()
    date_of_reward=models.DateTimeField(default=datetime.now)
    recipient=models.ForeignKey(on_delete=models.CASCADE, to=Customer)
    