from django.shortcuts import render, redirect
from .models import instructor_information
from order.models import Order
from home.models import products


# login for instructor
def login_func_instructor(request):
    if request.method == "POST":
        # get email and password from template
        instructor_log_email=request.POST.get('instructor_log_email')
        instructor_log_password=request.POST.get('instructor_log_password')

        # check the email that is have in database or not.
        check_filter_instructor = instructor_information.objects.filter(email=instructor_log_email)

        # if the email is valid
        if check_filter_instructor:
            # get the info of the instructor by email
            get_instructor = instructor_information.objects.get(email=instructor_log_email)
            instructor_password=get_instructor.password
            # now matching password
            # if password matched:
            if instructor_log_password==instructor_password:
                #start login session of instructor
                request.session['instructor_id'] = get_instructor.id
                request.session['instructor_first_name'] = get_instructor.first_name
                request.session['instructor_last_name'] = get_instructor.last_name
                request.session['instructor_email'] = get_instructor.email
                request.session['instructor_phone'] = get_instructor.phone
                request.session['instructor_address'] = get_instructor.address
                return redirect('home_instructor')
            else:
                # else show error.
                erorr_message_2 = "Password is Wrong, Please Try Again !!"

                value_func2 = {'erorr_message_2': erorr_message_2, 'instructor_log_email': instructor_log_email}
                # messages.error(request, "Invalid Credentials, Please Try Again !!")
                return render(request, 'login_func_instructor.html', value_func2)
        else:
            # else show error.
            erorr_message_2 = "Invalid Credentials, Please Try Again !!"

            value_func2 = {'erorr_message_2': erorr_message_2, 'instructor_log_email': instructor_log_email}
            # messages.error(request, "Invalid Credentials, Please Try Again !!")
            return render(request, 'login_func_instructor.html', value_func2)
    else:
        if request.session.get('instructor_id'):
            return redirect('home_instructor')
        else:
            return render(request, 'login_func_instructor.html')



# home page of instructor
def home_instructor(request):
    # user = request.session['instructor_first_name']
    # get the loged in instructor session
    user_id = request.session.get('instructor_id')

    # get the instructor by id from instructor_information table
    get_instructor_by_id = instructor_information.objects.get(id=user_id)

    # filter all order by instructor_information
    filter_order_by_instructor = Order.objects.filter(Instructor=get_instructor_by_id, ordered=True).order_by('-id')
    # print(filter_order_by_instructor)
    context={'filter_order_by_instructor':filter_order_by_instructor}
    return render(request, 'index_instructor.html',context)


# intructor my lesson
def my_lessons(request):
    # get the loged in instructor session
    user_id = request.session.get('instructor_id')
    # get the instructor by id from instructor_information table
    get_instructor_by_id = instructor_information.objects.get(id=user_id)
    # filter all lesson by products
    filter_lessons_by_instructor = products.objects.filter(Intructor=get_instructor_by_id)
    # print(filter_order_by_instructor)
    context = {'filter_lessons_by_instructor': filter_lessons_by_instructor}
    return render(request, 'my_lessons.html', context)
