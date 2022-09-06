import imp
from zipfile import Path
from django .urls import path
from .views import register_customer
from .views import register_account
from .views import register_wallet
from .views import register_transaction
from .views import register_card
from .views import register_thirdpary
from .views import register_receipt
from .views import register_notification
from .views import register_loan
from .views import register_reward




urlpatterns = [
    path("register/",register_customer,name="registration"),
]
# cus regist rep

urlpatterns = [
    path("register/",register_account,name="registration"),
]

urlpatterns = [
    path("register/",register_wallet,name="registration"),
]

urlpatterns = [
    path("register/",register_transaction,name="registration"),
]

urlpatterns = [
    path("register/",register_card,name="registration"),
]

urlpatterns = [
    path("register/",register_thirdpary,name="registration"),
]

urlpatterns = [
    path("register/",register_receipt,name="registration"),
]

urlpatterns = [
    path("register/",register_notification,name="registration"),
]

urlpatterns = [
    path("register/",register_loan,name="registration"),
]

urlpatterns = [
    path("register/",register_reward,name="registration"),
]