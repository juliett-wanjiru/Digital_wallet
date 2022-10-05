from django.contrib import admin

from .models import Customer
from .models import Account
from .models import Wallet
from .models import Transaction
from .models import Card
from .models import ThirdPary
from .models import Notification
from .models import Receipt
from .models import Loan
from .models import Reward
# Register your models here.
# querying data
# retrive a subset of data stored in a model
# apply filtering  to your query based on the attributes of your model

class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email")
    search_fields=("first_name","last_name","email")
admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display=("account_pin","customer","balance")
    search_fields=("account_pin","customer","balance")
admin.site.register(Wallet,WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_number","account_name","pin")
    search_fields=("account_number","account_name","pin")
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("transaction_amount","transaction_number","transaction_charge")
    search_fields=("transaction_amount","transaction_number","transaction_charge")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_number","date_issued","account")
    search_fields=("card_number","date_issued","account")  
admin.site.register(Card,CardAdmin)

class ThirdParyAdmin(admin.ModelAdmin):
    list_display=("nameof_thirdparty","account","location")
    search_fields=("nameof_thirdparty","account","location")  
admin.site.register(ThirdPary,ThirdParyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("datetime","message","status")
    search_fields=("datetime","message","status")  
admin.site.register(Notification,NotificationAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display=("receipt_type","receipt_date","total_amount")
    search_fields=("receipt_type","receipt_date","total_amount")  
admin.site.register(Receipt,ReceiptAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display=("loan_id","loan_type","interst_rate")
    search_fields=("loan_id","loan_type","interst_rate")  
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display=("customer_id","name","date_of_reward")
    search_fields=("customer_id","name","date_of_reward")  
admin.site.register(Reward,RewardAdmin)






  