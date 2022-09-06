from django.shortcuts import render

from .forms import CustomerRegistrationForm
from .forms import AccountRegistrationForm
from .forms import WalletRegistrationForm
from .forms import TransactionRegistrationForm
from .forms import CardRegistrationForm
from .forms import ThirdParyRegistrationForm
from .forms import ReceiptRegistrationForm
from .forms import NotificationRegistrationForm
from .forms import LoanRegistrationForm
from .forms import RewardRegistrationForm



# Create your views here.

def register_customer(request):
    form = CustomerRegistrationForm()
    return render(request, 'walletT/register_customer.html',
                  {"form":form})
    
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