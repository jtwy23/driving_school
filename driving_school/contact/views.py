from django.shortcuts import render, redirect
from django.contrib import messages
from .models import contact_us
# Create your views here.


# Contact page
def contact(request):
    if request.method == "POST":
        # Get email and message from template
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        print(email, msg)

        # Save contact us message to database
        contactus = contact_us(email=email, message=msg)
        contactus.save()
        messages.success(request, 'Thank you for your message. We will get in touch very soon.')
        return redirect('index')

    return render(request, 'contact.html')
