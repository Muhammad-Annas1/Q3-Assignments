import stripe
import os
from dotenv import load_dotenv

load_dotenv()

class PaymentProcessor:
    def __init__(self):
        stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

    def process_payment(self, user_email, amount):
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=["card"],
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": "Book Purchase",
                            },
                            "unit_amount": int(amount * 100),
                        },
                        "quantity": 1,
                    }
                ],
                mode="payment",
                customer_email=user_email,
                success_url="https://example.com/success",
                cancel_url="https://example.com/cancel",
            )
            return session.url
        except Exception as e:
            print("Stripe error:", e)
            return None
