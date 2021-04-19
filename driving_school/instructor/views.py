from django.shortcuts import render, redirect
from .models import instructor_information
from order.models import Order
from home.models import products


# Login for instructor
def login_func_instructor(request):
    if request.method == "POST":
        # Get email and password from template
        instructor_log_email = request.POST.get('instructor_log_email')
        instructor_log_password = request.POST.get('instructor_log_password')

        # Check the email that is in database or not.
        check_filter_instructor = instructor_information.objects.filter(
            email=instructor_log_email)

        # If the email is valid
        if check_filter_instructor:
            # Get the info of the instructor by email
            get_instructor = instructor_information.objects.get(
                email=instructor_log_email)
            instructor_password = get_instructor.password
            # Now matching password
            # If password matched
            if instructor_log_password == instructor_password:
                # Start login session of instructor
                request.session['instructor_id'] = get_instructor.id
                request.session[
                    'instructor_first_name'] = get_instructor.first_name
                request.session[
                    'instructor_last_name'] = get_instructor.last_name
                request.session['instructor_email'] = get_instructor.email
                request.session['instructor_phone'] = get_instructor.phone
                request.session['instructor_address'] = get_instructor.address
                return redirect('home_instructor')
            else:
                # Else show error.
                erorr_message_2 = "Your Password Is Wrong, Please Try Again!"

                value_func2 = {
                    'erorr_message_2': erorr_message_2, 
                    'instructor_log_email': instructor_log_email}
                # Error message
                return render(
                    request, 'login_func_instructor.html', value_func2)
        else:
            # else show error message
            erorr_message_2 = "Invalid Credentials, Please Try Again!"

            value_func2 = {
                'erorr_message_2': erorr_message_2,
                'instructor_log_email': instructor_log_email}
            # Error message
            return render(request, 'login_func_instructor.html', value_func2)
    else:
        if request.session.get('instructor_id'):
            return redirect('home_instructor')
        else:
            return render(request, 'login_func_instructor.html')


# Instructor homepage
def home_instructor(request):
    # Get the logged in instructor session
    user_id = request.session.get('instructor_id')

    # Get instructor by id from instructor_information table
    get_instructor_by_id = instructor_information.objects.get(id=user_id)

    # filter all order by instructor_information
    filter_order_by_instructor = Order.objects.filter(
        Instructor=get_instructor_by_id, ordered=True).order_by('-id')
    # print(filter_order_by_instructor)
    context = {'filter_order_by_instructor': filter_order_by_instructor}
    return render(request, 'index_instructor.html', context)


# Intructor - my lesson
def my_lessons(request):
    # Get the logged in instructor session
    user_id = request.session.get('instructor_id')
    # Get the instructor by id from instructor_information table
    get_instructor_by_id = instructor_information.objects.get(id=user_id)
    # Filter all lessons by products
    filter_lessons_by_instructor = products.objects.filter(
        Intructor=get_instructor_by_id)
    context = {'filter_lessons_by_instructor': filter_lessons_by_instructor}
    return render(request, 'my_lessons.html', context)


# Instructor profile
def instructor_profile(request):
    # Get the logged in instructor session
    user_id = request.session.get('instructor_id')
    # Get the instructor by id from instructor_information table
    get_instructor_by_id = instructor_information.objects.get(id=user_id)
    context = {'get_instructor_by_id': get_instructor_by_id}
    return render(request, 'instructor_profile.html', context)


# Instructor order details
# Get ID by passing an ID by link
def order_details(request, pk):
    # Get order details by ID
    get_order = Order.objects.get(id=pk)
    context = {'get_order': get_order}
    return render(request, 'order_details.html', context)
    

# Instructor cancel order
def make_cancel_order(request):
    # Get order ID
    order_id = request.POST.get('order_id')
    # Get order details
    get_order = Order.objects.get(id=order_id)
    # Make instructor_cancel_order boolean field True and save
    get_order.instructor_cancel_order = True
    get_order.save()
    return redirect('order_details', get_order.id)
