from django .urls import path
from . import views

urlpatterns = [
    path("register/",views.register_customer,name="registration"),
    path("account/",views.register_account,name="registration"),
    path("wallet/",views.register_wallet,name="registration"),
    path("transaction/",views.register_transaction,name="registration"),
    path("card/",views.register_card,name="registration"),
    path("thirdpary/",views.register_thirdpary,name="registration"),
    path("receipt/",views.register_receipt,name="registration"),
    path("notification/",views.register_notification,name="registration"),
    path("loan/",views.register_loan,name="registration"),
    path("reward/",views.register_reward,name="registration"),
    path("customers/",views.list_customer,name="list_customers")
]
