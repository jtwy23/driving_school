from django.shortcuts import render, redirect
from .models import instructor_information



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

    return render(request, 'login_func_instructor.html')


def home_instructor(request):
    return render(request, 'index_instructor.html')