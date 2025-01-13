from django.urls import path
from . import views
urlpatterns = [
    path('checkout-session/',views.checkout_session, name="checkout_session"),
    path('checkout-view/',views.checkout, name="checkout_view"),
    path('cancel/',views.payment_cancel, name="cancel_paymet"),
    path('success/',views.payment_success,name="success_payment")
]
