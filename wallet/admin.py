from django.contrib import admin

# Register your models here.
from .models import Customer
from .models import Customer
from .models import Wallet
from .models import Account
from .models import Transaction
from .models import Card
from .models import ThirdPary
from .models import Notification
from .models import Receipt
from .models import Loan
from .models import Reward

admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(ThirdPary)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)




  