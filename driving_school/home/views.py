from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .models import EmailConfirmed, products, Categories, customer_more_information, reviews
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .forms import change_profile, change_user_profile
# Create your views here.


def index(request):
    # Filters all the products
    all_products = products.objects.all()
    # Filters all categories
    all_Categories = Categories.objects.all()
    context1 = {'all_products': all_products, 'all_Categories': all_Categories}
    return render(request, 'index.html', context1)


# All lessons page
def all_lessons(request):
    # Filters all the products
    all_products = products.objects.all()
    # Filters all categories
    all_Categories = Categories.objects.all()
    context1 = {'all_products': all_products, 'all_Categories': all_Categories}
    return render(request, 'all_lessons.html', context1)


# Search all products
def product_search(request):
    # Get the search key from the template
    search_product = request.GET.get('search')
    print(search_product)

    # Search the lesson by icontains
    if search_product:
        search_result = products.objects.filter(
            Q(product_name__icontains=search_product) |
            Q(description__icontains=search_product)
        ).order_by('-id')

        search_result_count = products.objects.filter(
            Q(product_name__icontains=search_product) |
            Q(description__icontains=search_product)
        ).count()

        print(search_result)
        context5 = {
            'search_product': search_product,
            'search_result': search_result,
            'search_result_count': search_result_count
        }
        return render(request, 'product.html', context5)


# Signup function
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

        # Check error inputs
        user_email_info = User.objects.filter(email=email_sign)

        erorr_message = ""

        if user_email_info:
            # Error message
            erorr_message = "Email Already Exist"

        elif password_sign != password_sign_re:
            # Error message
            erorr_message = "Passwords are not match !!"

        elif len(password_sign) < 7:
            # Error message
            erorr_message = "Password Must Be At Least 7 Digits!"

        if not erorr_message:

            # Create user
            myuser = User.objects.create_user(
                email_sign, email_sign, password_sign)
            myuser.first_name = first_name
            myuser.last_name = last_name
            myuser.is_active = False
            myuser.save()

            # Customer more information
            customer_more_info = customer_more_information(
                Customer=myuser, Address=address_sign, Postcode=postcode_sign, 
                Phone_number=phone_sign
            )
            customer_more_info.save()

            # send mail
            user = EmailConfirmed.objects.get(user=myuser)
            site = get_current_site(request)
            email = myuser.email
            first_name = myuser.first_name
            last_name = myuser.last_name

            domain="driving-school-v1.herokuapp.com"

            # 8000-apricot-stingray-k3ued494.ws-eu03.gitpod.io

            sub_of_email = "Activation Email From Driving School."
            email_body = render_to_string(
                'verify_email.html',
                {
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'domain': domain,
                    'activation_key': user.activation_key
                }
            )

            send_mail(
                sub_of_email,  # Subject of message
                email_body,  # Message
                '',  # From Email
                [email],  # To Email

                fail_silently=True
            )

            # Save all data
            messages.success(
                request, 'Check Your Email to Activate Your Account!')

            return redirect('/')

        else:

            value_dic = {'first_name': first_name, 'last_name': last_name, 'email_sign': email_sign,
                         'address_sign': address_sign, 'postcode_sign':postcode_sign, 'phone_sign':phone_sign, 'erorr_message': erorr_message}
            return render(request, 'signup_func.html', value_dic)
    return render(request, 'signup_func.html')


# The activation key for active signup customer
def email_confirm(request, activation_key):
    user = get_object_or_404(EmailConfirmed, activation_key=activation_key)
    if user is not None:
        user.email_confirmed = True
        user.save()

        myuser = User.objects.get(email=user)
        myuser.is_active = True
        myuser.save()
        first_name = myuser.first_name
        last_name = myuser.last_name

        condict = {'first_name': first_name, 'last_name':last_name}
        return render(request, 'registration_complete.html', condict)


# Login function
def login_func(request):
    if request.method == 'POST':
        log_username = request.POST['log_username']
        log_password = request.POST['log_password']
        # Authenticates username and password for login
        user = authenticate(username=log_username, password=log_password)

        erorr_message_2 = ""

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            erorr_message_2 ="Invalid Credentials, Please Try Again!"

            value_func2 = {
                'erorr_message_2': erorr_message_2, 'log_username': log_username
            }
            return render(request, 'signup_func.html', value_func2)


# Logout function
def logout_func(request):
    # Logout from user id
    logout(request)
    return redirect('index')


# Product details page to show details of product by passing product id
def product_detail(request, pk):
    get_product = products.objects.get(id=pk)
    # Products category
    cat_pro = get_product.category
    # Get all products by category
    all_pro_cat = products.objects.filter(category=cat_pro)

    filter_product_reviews = reviews.objects.filter(product=get_product).order_by('-id')
    filter_product_reviews_qty = reviews.objects.filter(product=get_product).count()
    #print(filter_product_reviews_qty)

    # making average rating
    total_ratings=0
    for i in filter_product_reviews:
        total_ratings = total_ratings + int(i.ratings)
        #print(total_ratings)

    if filter_product_reviews_qty==0:
        average_rating = 0
    else:
        average_rating = total_ratings/filter_product_reviews_qty
        #print(average_rating)

    average_rating = "%0.1f" % average_rating

    # print('this is all')
    # print(average_rating, filter_product_reviews_qty)

    context2 = {'get_product': get_product, 'all_pro_cat': all_pro_cat, 'filter_product_reviews':filter_product_reviews, 'filter_product_reviews_qty':filter_product_reviews_qty, 'average_rating':average_rating}
    return render(request, 'product-detail.html', context2)


# My profile page
def profile(request):
    # If the user is logged in
    if request.user.is_authenticated:
        user = request.user

        filter_user = customer_more_information.objects.filter(Customer=user)
        if filter_user:
            get_user = customer_more_information.objects.get(Customer=user)
            context2 = {'get_user': get_user}
            return render(request, 'profile.html', context2)
        else:
            return render(request, 'profile.html')
    else:
        return redirect('index')


# Edit profile
def edit_profile(request):
    # If the user is logged in
    if request.user.is_authenticated:
        user = request.user
        # Use form.py to edit profile
        form2 = change_user_profile(instance=user)

        # If user has data in customer_more_information table
        filter_customer_details = customer_more_information.objects.filter(
            Customer=user)

        if filter_customer_details:
            get_customer_details = customer_more_information.objects.get(
                Customer=user)
            form1 = change_profile(instance=get_customer_details)

            if request.method == 'POST':
                form1 = change_profile(
                    request.POST, instance=get_customer_details)
                if form1.is_valid():
                    form1.save()
                    
                form2 = change_user_profile(request.POST, instance=user)
                if form2.is_valid():
                    form2.save()

                messages.success(
                    request, 'Your Profile Is Successfully Updated!')
                return redirect('profile')

            context3 = {'form1': form1, 'form2': form2}
            return render(request, 'edit_profile.html', context3)
        # If user has no data in customer_more_information table
        # User details will save to customer_more_information table
        else:
            if request.method == 'POST':
                phone_no = request.POST.get('phone_no')
                Postcode = request.POST.get('Postcode')
                address = request.POST.get('address')

                # Customer more information
                # User details will save to customer_more_information table
                customer_more_info = customer_more_information(
                    Customer=user, Address=address,
                    Postcode=Postcode, Phone_number=phone_no)
                customer_more_info.save()

                # Edit user table
                form2 = change_user_profile(request.POST, instance=user)
                if form2.is_valid():
                    form2.save()

                messages.success(
                    request, 'Your Profile Is Successfully Updated!')
                return redirect('profile')

            context3 = {'form2': form2}
            return render(request, 'edit_profile.html', context3)
    else:
        return redirect('index')




def customer_review(request):
    rating_number=request.POST.get('rating_number')
    review_text=request.POST.get('review_text')

    product_id=request.POST.get('product_id')
    get_details_product = products.objects.get(id=product_id)

    user = request.user

    filter_review = reviews.objects.filter(customer=user, product=get_details_product)

    if filter_review:
        messages.success(request, 'You Can not Give Feedback More Than Once.')
        return redirect('product_detail', product_id)
    else:

        data_reviews = reviews(customer=user, product=get_details_product, ratings=rating_number, review_text=review_text)
        data_reviews.save()

        messages.success(request, 'Your Review Has Been Added !!')
        return redirect('product_detail', product_id)

