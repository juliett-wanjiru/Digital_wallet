from django .urls import path
from . import views

urlpatterns = [
    # these are paths of what is in our views
    path("register/", views.register_customer, name="registration"),
    path("account/", views.register_account, name="registration"),
    path("card/", views.register_card, name="registration"),
    path("thirdpary/", views.register_thirdpary, name="registration"),
    path("receipt/", views.register_receipt, name="registration"),
    path("notification/", views.register_notification, name="registration"),
    path("loan/", views.register_loan, name="registration"),
    path("reward/", views.register_reward, name="registration"),

    path("customers/", views.list_customer, name="list_customers"),

    # id single
    path("customers/<int:id>/", views.customer_profile, name="customer_profile"),
    path("customers/edit/<int:id>/", views.edit_customer, name="edit_customer"),
]
