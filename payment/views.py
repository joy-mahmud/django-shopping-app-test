from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.
def checkout(request):
    return render(request,'payment/checkout.html')
@csrf_exempt
def checkout_session(request):
    if request.method == "POST":
        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Product Name',  # You can dynamically set this
                            },
                            'unit_amount': 1000,  # Amount in cents (e.g., $10.00)
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url="http://127.0.0.1:8000/payment/success/",
                cancel_url="http://127.0.0.1:8000/payment/cancel/"
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return HttpResponse(status=405)
    

def payment_success(request):
    return render(request,'payment/success.html')

def payment_cancel(request):
    return render(request,'payment/cancel.html')
