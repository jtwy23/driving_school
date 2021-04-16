from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import EmailConfirmed, products, Categories, customer_more_information
# Create your views here.


def index(request):
    # filter all the products
    all_products = products.objects.all()
    # filter all categories
    all_Categories = Categories.objects.all()
    context1 = {'all_products':all_products, 'all_Categories':all_Categories}
    return render(request, 'index.html', context1)



# signup fumction
def signup_login(request):
    if request.method == "POST":
        # get all data  form teplate
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email_sign = request.POST.get('email_sign')

        address_sign = request.POST.get('address_sign')
        postcode_sign = request.POST.get('postcode_sign')
        phone_sign = request.POST.get('phone_sign')

        password_sign = request.POST.get('password_sign')
        password_sign_re = request.POST.get('password_sign_re')


        # chech the error inputs
        user_email_info = User.objects.filter(email=email_sign)

        erorr_message = ""

        if user_email_info:
            # messages.error(request, "Email Already Exist")
            erorr_message = "Email Already Exist"

        elif password_sign != password_sign_re:
            # messages.error(request, "Passwords are not match")
            erorr_message = "Passwords are not match !!"

        elif len(password_sign) < 7:
            # messages.error(request, "Passwords Must be Al least 7 Digits")
            erorr_message = "Passwords Must be Al least 7 Digits !!"

        if not erorr_message:

            # create user
            myuser = User.objects.create_user(email_sign, email_sign, password_sign)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.is_active = False
            myuser.save()

            # customer more informations
            customer_more_info = customer_more_information(Customer=myuser, Address=address_sign, Postcode=postcode_sign, Phone_number=phone_sign)
            customer_more_info.save()
            # saved all data




            

            messages.success(request, 'Check Your Email for Activate Your Account !!!')

            return redirect('/')

        else:

            value_dic = {'first_name': first_name, 'last_name': last_name, 'email_sign': email_sign,
                         'address_sign':address_sign, 'postcode_sign':postcode_sign, 'phone_sign':phone_sign, 'erorr_message': erorr_message}
            return render(request, 'signup_func.html', value_dic)
    return render(request, 'signup_func.html')


# The activation key for active signup customer
def email_confirm(request, activation_key):
    user= get_object_or_404(EmailConfirmed, activation_key=activation_key)
    if user is not None:
        user.email_confirmed=True
        user.save()

        myuser=User.objects.get(email=user)
        myuser.is_active=True
        myuser.save()
        first_name=myuser.first_name
        last_name=myuser.last_name

        condict = {'first_name': first_name, 'last_name':last_name}
        return render(request, 'registration_complete.html', condict)
        
# login function
def login_func(request):
    if request.method == 'POST':
        log_username = request.POST['log_username']
        log_password = request.POST['log_password']
        # this is for authenticate username and password for login
        user = authenticate(username=log_username, password=log_password)

        erorr_message_2 = ""

        if user is not None:
            login(request, user)
            # messages.success(request, "Successfully Logged In !!")
            return redirect('index')
        else:
            erorr_message_2 ="Invalid Credentials, Please Try Again !!"

            value_func2 = {'erorr_message_2':erorr_message_2, 'log_username':log_username}
            # messages.error(request, "Invalid Credentials, Please Try Again !!")
            return render(request, 'signup_func.html', value_func2)


# logout function
def logout_func(request):
    # this is for logout from user id
    logout(request)
    return redirect('index')
