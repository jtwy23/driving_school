from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
import random
from .models import Order
from home.models import customer_more_information, products
# Create your views here.
# from datetime import datetime
import datetime
from django.views.generic import ListView, DetailView, View
# Create your views here.
import stripe


# stripe Secret key
stripe.api_key = "sk_test_51IMFIgGHrfeW2r6w38JXjUr4HRvbtZymCmjpAIiOnTWn7I5xO4ixgqnjZD0JJacIb7N8WOG2iIkpJqWktplQNAJR007vAjrHfH"



def my_orders(request):
    # get user
    user = request.user
    # filter those order, which are same user and ordered Boolean true
    get_all_order = Order.objects.filter(user=user, ordered=True)
    context = {'get_all_order':get_all_order}
    return render(request, 'my_order.html', context)


# custmer order details page
# get order id by passing id in link
def my_order_details(request, pk):
    # get the details of order
    get_the_order = Order.objects.get(id=pk)
    context = {'get_the_order':get_the_order}
    return render(request, 'my_order_details.html', context)


# cart page
def cart(request):
    return render(request, 'shoping-cart.html')



# for Checkout
def checkout(request):
    if request.method =="POST":
        # get all input
        prod_details = request.POST.get('prod_details')
        checkout_money = request.POST.get('checkout_money')

        all_prod = request.POST.get('all_prod')
        print(all_prod)

        all_prod_price = request.POST.get('all_prod_price')
        all_prod_qty = request.POST.get('all_prod_qty')
        all_prod_price_qty = request.POST.get('all_prod_price_qty')
        # print('total')
        # print(checkout_money, prod_details)

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        zip = request.POST.get('zip')


        # print(full_address, city, postal_code, country, phone)

        # save all the order to database by loop
        for i in all_prod:
            print(i)
            # print(type(i))

            check_integer = i.isnumeric()
            print(check_integer)

            # if the value is integer
            if check_integer:
                print('yes')
                print(i)
                print(type(i))

                lesson_Id = int(i)
                print(type(lesson_Id))

                # by id get the lesson details
                get_lesson = products.objects.get(id=lesson_Id)
                print(get_lesson)

                # lesson single price
                single_price = get_lesson.product_price
                # lesson instructor
                instructor = get_lesson.Intructor

                # make random order ID
                random_num = random.randint(2345678909800, 9923456789000)

                uniqe_confirm = Order.objects.filter(order_id=random_num)
                # print(random_num)

                while uniqe_confirm:
                    random_num = random.randint(234567890980000, 992345678900000)
                    if not Order.objects.filter(order_id=random_num):
                        break
                # print(random_num)

                user = request.user
                # save order
                post_order = Order(user=user, Lesson=get_lesson, Instructor=instructor, order_id=random_num, Lesson_price=single_price,
                                   first_name=first_name, last_name=last_name, email=email, phone=phone,
                                   address=address, zip=zip, order_date=datetime.datetime.now())
                post_order.save()
            else:
                print('no')


        Thanks = True
        return render(request, 'checkout.html', {'Thanks': Thanks})

    else:
        # if customer is loged in:
        if request.user.is_authenticated:
            user=request.user
            # filter those orders which have not payment yet
            order = Order.objects.filter(user=user, ordered=False)
            # print(order)
            # for new order customer have to payment the remain unpayment order
            if order:
                messages.info(request, 'You Have a Order Remain to Payment !! To Order New, You Have to Pay The first One.')
                return redirect('payment')
            else:
                # get details about customer
                filter_user=customer_more_information.objects.filter(Customer=user)
                if filter_user:
                    get_user=customer_more_information.objects.get(Customer=user)
                    context4 = {'get_user':get_user}
                    return render(request, 'checkout.html', context4)
                else:
                    # return render(request, 'checkout.html')
                    messages.info(request, 'Please Give Us Some Information.')
                    return redirect('edit_profile')
        else:
            return redirect('signup_login')




class PaymentView(View):
    # for get
    def get(self, *args, **kwargs):
        user = self.request.user
        # get the order details which is remian to payment
        order = Order.objects.filter(user=user, ordered=False)
        print(order)

        sum_of_bill=0

        # making sum of order price
        for i in order:
            print(i)
            sum_of_bill = sum_of_bill + int(i.Lesson_price)
        print(sum_of_bill)

        # making condition for discount counting
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

    # for post
    def post(self, *args, **kwargs):
        print(self.request.user)
        # user details
        user=self.request.user

        # filter those order, which are not paid and same user
        order = Order.objects.filter(user=user, ordered=False)
        print(order)

        sum_of_bill = 0
        # making condition for discount counting
        for i in order:
            print(i)
            sum_of_bill = sum_of_bill + int(i.Lesson_price)
        print(sum_of_bill)


        try:
            # try for making payment from stripe getway
            customer = stripe.Customer.create(
                email=self.request.user.email,
                description=self.request.user.username,
                source=self.request.POST['stripeToken']
            )
            amount = int(sum_of_bill)

            # making condition for discount counting
            if amount>100:
                a = amount*70
                print(a)
            else:
                a=amount*90
                print(a)

            charge = stripe.Charge.create(
                amount=a,
                currency="gbp",
                customer=customer,
                description="Payment for Driving School",
            )

            # making the orders paid and make ordered boolean True
            for i in order:
                i.ordered = True
                i.save()

                last_order_id=i.id


            messages.success(self.request, 'Payment was Successfull !!')

        # if there any error in payment
        # if try is not proper working then
        except stripe.error.CardError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('index')

        except stripe.error.RateLimitError as e:
            messages.info(self.request, f"{e.error.message}")
            return redirect('index')
        except stripe.error.InvalidRequestError as e:
            messages.info(self.request, "Invalid Request !")
            return redirect('index')
        except stripe.error.AuthenticationError as e:
            messages.info(self.request, "Authentication Error !!")
            return redirect('index')
        except stripe.error.APIConnectionError as e:
            messages.info(self.request, "Check Your Connection !")
            return redirect('index')
        except stripe.error.StripeError as e:
            messages.info(self.request, "There was an error please try again !")
            return redirect('index')
        except Exception as e:
            messages.info(self.request, "A serious error occured we were notified !")
            return redirect('index')

        return redirect('index')
