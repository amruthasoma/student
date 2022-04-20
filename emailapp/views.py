
from email import message
from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.conf import settings
from emailapp.forms import studentmail

# Create your views here.
def stud(request):
    form=studentmail()
    if request.method == 'POST':
        form=studentmail(request.POST)
        if form.is_valid():
            form.save()
            subject = 'greetings from southernland'
            message = 'Here is a golden opportunity to improve your skillset and get high-paid jobs.Pay 2800/- for 2 courses and earn 20+ skill set at a single time.ENROLL TODAY FOR THE OFFERNO EXTENSION FOR THIS OFFERIT IS APPLICABLE ONLY FOR TODAY'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
            message,settings.EMAIL_HOST_USER, [recipient])
            return redirect('/'),
    return render(request,'home.html',{'form':form})    
