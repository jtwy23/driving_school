from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact_us
from .forms import ContactUsForm
# Create your views here.


# Contact page
def contact(request):
    if request.method == "POST":
        # Get email and message from template
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        print(email, msg)

        form = ContactUsForm(request.POST)
        message = 'Invalid Message'
        # check whether it's valid:
        if form.is_valid():

            # Save contact us message to database
            contactus = contact_us(email=email, message=msg)
            contactus.save()
            message = 'Thank you for your message. We will get in touch very soon.'

        messages.success(
            request,
            message
        )

    return render(request, 'contact.html')
