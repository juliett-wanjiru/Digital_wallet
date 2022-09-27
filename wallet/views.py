from django.shortcuts import render
from . import models


from .forms import CustomerRegistrationForm,AccountRegistrationForm,WalletRegistrationForm,TransactionRegistrationForm,CardRegistrationForm,ThirdParyRegistrationForm,ReceiptRegistrationForm,NotificationRegistrationForm,LoanRegistrationForm,RewardRegistrationForm

# Create your views here.

def register_customer(request):
    if request.method == "POST":
          form = CustomerRegistrationForm(request.POST)
          if form.is_valid():
              form.save()
              
    else:
        form = CustomerRegistrationForm()
        return render(request, 'walletT/register_customer.html',
                  {"form":form})
        
def list_customer(request):
    customers = models.Customer.objects.all()
    return render (request, 'walletT/customer_list.html',
                   {"customers":customers})       
        
  
   
    
def register_account(request):
    form = AccountRegistrationForm()
    return render(request, 'walletT/register_account.html',
                  {"form":form})
    
def register_wallet(request):
    form = WalletRegistrationForm()
    return render(request, 'walletT/register_wallet.html',
                  {"form":form})
    
    
def register_transaction(request):
    form =TransactionRegistrationForm()
    return render(request, 'walletT/register_transaction.html',
                  {"form":form})
    
def register_card(request):
    form =CardRegistrationForm()
    return render(request, 'walletT/register_card.html',
                  {"form":form})

def register_thirdpary(request):
    form =ThirdParyRegistrationForm()
    return render(request, 'walletT/register_thirdpary.html',
                  {"form":form})
    
def register_receipt(request):
    form =ReceiptRegistrationForm()
    return render(request, 'walletT/register_receipt.html',
                  {"form":form})
    
def register_notification(request):
    form =NotificationRegistrationForm()
    return render(request, 'walletT/register_notification.html',
                  {"form":form})

def register_loan(request):
    form =LoanRegistrationForm()
    return render(request, 'walletT/register_loan.html',
                  {"form":form})
    
def register_reward(request):
    form =RewardRegistrationForm()
    return render(request, 'walletT/register_reward.html',
                  {"form":form})