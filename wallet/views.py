from distutils.command.install_egg_info import to_filename
from django.shortcuts import render,redirect
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
        
def customer_profile(request,id):
    customers=models.Customer.objects.get(id=id)
    return render (request, 'walletT/customer_profile.html',
                   {"customers":customers}) 
# EDITING DATA
def edit_customer(request,id):
    if request.method == "POST":
          form = CustomerRegistrationForm(request.POST,instance=models.Customer)
          if form.is_valid():
              form.save()
              return redirect("customer_profile",id=models.Customer.id)
    else:
        form = CustomerRegistrationForm(instance=models.Customer)
        return render(request, 'walletT/edit_customer.html',
                  {"form":form})
        
    
def register_account(request):
    if request.method == "POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
    return render(request, 'walletT/register_account.html',
                  {"form":form})
    
def list_account(request):
    accounts = models.Account.objects.all()
    return render (request, 'walletT/account_list.html',
                   {"accounts":accounts})       
        
    
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