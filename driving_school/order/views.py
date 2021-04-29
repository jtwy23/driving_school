from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random
from .models import Order, cancel_order_for_money_back
from home.models import customer_more_information, products
import datetime
from django.views.generic import ListView, DetailView, View
import stripe
from decouple import config

# Create your views here.


# stripe Secret key
stripe.api_key = config('STRIPE')


def my_orders(request):
    # Get user
    user = request.user
    # Filter the orders which are same user and ordered boolean true
    get_all_order = Order.objects.filter(user=user, ordered=True)
    context = {'get_all_order': get_all_order}
    return render(request, 'my_order.html', context)


# Custmer order details page
# Get order ID by passing ID in link
def my_order_details(request, pk):
    # Get the details of the order
    get_the_order = Order.objects.get(id=pk)
    update_info = customer_more_information.objects.get(Customer=get_the_order.user)
    context = {'get_the_order': get_the_order, 'update_info': update_info}
    return render(request, 'my_order_details.html', context)


# Pupil cancellation of order
def customer_canceled_order(request):
    # To get current time and date
    now_time = datetime.datetime.now()

    # Get order ID to get the details
    order_id = request.POST.get('order_id')
    get_order = Order.objects.get(id=order_id)

    # Get time and date of order time
    order_time = get_order.order_date

    date_time_str = order_time

    # Cancellation time period
    date_time_obj = datetime.datetime.strptime(
        date_time_str, '%Y-%m-%d %H:%M:%S.%f')
    print(date_time_obj.date())

    differnt_time = now_time - date_time_obj
    print(differnt_time)
    print(differnt_time.days)
    print(differnt_time.seconds)
    print(differnt_time.microseconds)

    # Get time different in days
    differnt_time_days = differnt_time.days

    # If less than 1 day that means less than 24 hours
    if differnt_time_days < 1:
        get_order.customer_cancel_order = True
        get_order.save()
        messages.success(
            request,
            "You will receive a refund in 3 working days as you have cancelled your order within the 24 hour period."
        )

        # If less than 1 that means less than 24 hours save a new table for admin to pay back the customer
        money_back_admin = cancel_order_for_money_back(
            user=request.user, order=get_order)
        money_back_admin.save()

        return redirect('my_order_details', get_order.id)
    else:
        get_order.customer_cancel_order = True
        get_order.save()
        messages.success(
            request,
            "You are cancelling your lesson and losing your fee because you did not cancel within 24 hours of buying your lesson."
        )
        return redirect('my_order_details', get_order.id)


# Cart
def cart(request):
    return render(request, 'shoping-cart.html')


# Checkout
def checkout(request):
    if request.method == "POST":
        # get all input
        prod_details = request.POST.get('prod_details')
        checkout_money = request.POST.get('checkout_money')

        all_prod = request.POST.get('all_prod')

        all_prod = all_prod[:-1]

        all_prod = all_prod[2:]

        str = all_prod

        all_products = str.split(",")

        all_prod_price = request.POST.get('all_prod_price')
        all_prod_qty = request.POST.get('all_prod_qty')
        all_prod_price_qty = request.POST.get('all_prod_price_qty')

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zip = request.POST.get('zip')

        # Save all the orders to database by loop
        for i in all_products:

            lesson_Id = int(i)

            # By ID get the lesson details
            get_lesson = products.objects.get(id=lesson_Id)

            # Single price lesson
            single_price = get_lesson.product_price

            # Lesson instructor
            instructor = get_lesson.Intructor

            # Generate random order ID
            random_num = random.randint(2345678909800, 9923456789000)

            uniqe_confirm = Order.objects.filter(order_id=random_num)

            while uniqe_confirm:
                random_num = random.randint(234567890980000, 992345678900000)
                if not Order.objects.filter(order_id=random_num):
                    break

            user = request.user
            # Save order
            post_order = Order(
                user=user, Lesson=get_lesson, Instructor=instructor,
                order_id=random_num, Lesson_price=single_price,
                first_name=first_name, last_name=last_name, email=email,
                phone=phone, address=address, zip=zip, order_date=datetime.datetime.now())
            post_order.save()

        Thanks = True
        return render(request, 'checkout.html', {'Thanks': Thanks})

    else:
        # If customer is logged in:
        if request.user.is_authenticated:
            user=request.user
            # Filter those orders which have not made payment yet
            order = Order.objects.filter(user=user, ordered=False)
            # For new order customers that have unpaid orders
            if order:
                messages.info(request, 'You have unpaid items in your basket.')
                return redirect('payment')
            else:
                # Get customer details
                filter_user = customer_more_information.objects.filter(
                    Customer=user)
                if filter_user:
                    get_user = customer_more_information.objects.get(
                        Customer=user)
                    context4 = {'get_user': get_user}
                    return render(request, 'checkout.html', context4)
                else:
                    messages.info(request, 'Please give us some information.')
                    return redirect('edit_profile')
        else:
            messages.success(
                request,
                'You need to login / signup before making a purchase.'
            )
            return redirect('signup_login')


class PaymentView(View):
    # For get
    def get(self, *args, **kwargs):
        user = self.request.user
        # Get orders still to pay
        order = Order.objects.filter(user=user, ordered=False)

        sum_of_bill = 0

        # Order price
        for i in order:
            sum_of_bill = sum_of_bill + int(i.Lesson_price)

        # Discount conditions
        if sum_of_bill >= 100:
            sum_of_bill = (sum_of_bill / 100) * 70
        else:
            sum_of_bill = (sum_of_bill / 100) * 90

        sum_of_bill = "%0.2f" % sum_of_bill

        context = {
            'sum_of_bill': sum_of_bill,
            'order': order,
            "DISPLAY_COUPON_FORM": False

        }
        return render(self.request, 'payment.html', context)

    # For post
    def post(self, *args, **kwargs):
        print(self.request.user)
        # User details
        user=self.request.user

        # Filter the orders which are unpaid and the same user
        order = Order.objects.filter(user=user, ordered=False)
        print(order)

        sum_of_bill = 0
        # Discount conditions
        for i in order:
            print(i)
            sum_of_bill = sum_of_bill + int(i.Lesson_price)
        print(sum_of_bill)

        try:
            # Try making payment from stripe gateway
            customer = stripe.Customer.create(
                email=self.request.user.email,
                description=self.request.user.username,
                source=self.request.POST['stripeToken']
            )
            amount = int(sum_of_bill)

            # Discount condition
            if amount > 100:
                a = amount*70
                print(a)
            else:
                a = amount*90
                print(a)

            charge = stripe.Charge.create(
                amount=a,
                currency="gbp",
                customer=customer,
                description="Payment for Driving School",
            )

            # Orders paid and make ordered boolean True
            for i in order:
                i.ordered = True
                i.save()

                last_order_id = i.id

            order_cus = Order.objects.get(id=last_order_id)

            # sending email to customer about the order
            email_for_buy = render_to_string(
                'email_to_buy.html',
                {
                    'first_name': self.request.user.first_name,
                    'last_name': self.request.user.last_name,
                    'order': order,
                    'order_cus': order_cus,
                }
            )

            email = self.request.user.email
            send_mail(
                'Purchase Order',  # Subject
                email_for_buy,  # Message
                '',  # From email
                [email],  # To email

                fail_silently=True,
            )

            messages.success(self.request, 'Payment is Successful!')

        # If there is any error in payment
        # Ff try is not working properly then
        except stripe.error.CardError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('index')

        except stripe.error.RateLimitError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('index')
        except stripe.error.InvalidRequestError as e:
            messages.info(self.request, "Invalid Request!")
            return redirect('index')
        except stripe.error.AuthenticationError as e:
            messages.info(self.request, "Authentication Error!")
            return redirect('index')
        except stripe.error.APIConnectionError as e:
            messages.info(self.request, "Check Your Connection!")
            return redirect('index')
        except stripe.error.StripeError as e:
            messages.info(self.request, "There was an error please try again!")
            return redirect('index')
        except Exception as e:
            messages.info(
                self.request, "A serious error occured we were notified!")
            return redirect('index')

        return redirect('index')
