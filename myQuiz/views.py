from django.shortcuts import render
from myQuiz.forms import UserForm,ContactUsForm,ResultForm
from myQuiz.models import User
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.core.mail import send_mail,BadHeaderError

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt




def index(request):
        if request.method== "POST":
            contact=ContactUsForm(data=request.POST)
            if contact.is_valid():
                    subject = request.POST.get('subject', '')
                    message = request.POST.get('message', '')
                    from_email = request.POST.get('email', '')
                    total_message=from_email+'\n'+subject+'\n'+message
                    print(total_message)
                    contact.save()
                    try:
                        
                        send_mail(subject, total_message, from_email, ['vaibhavbaghel3196@gmail.com'])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'Thanks for contacting me',extra_tags='alert')
                    return HttpResponseRedirect('/')
                   
        else:
            contact = ContactUsForm()
        return render(request,'index.html',context={'contacts':contact})



@login_required
def startPage(request):
    
   return render(request,'start.html')
   
  
def contactus(request):
        if request.method== "POST":
            contact=ContactUsForm(data=request.POST)
            if contact.is_valid():
                    subject = request.POST.get('subject', '')
                    message = request.POST.get('message', '')
                    from_email = request.POST.get('email', '')
                    total_message=from_email+'\n'+subject+'\n'+message
                    contact.save()
                    try:
                        
                        send_mail(subject, total_message, from_email, ['vaibhavbaghel3196@gmail.com'])
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    messages.success(request, 'Thanks for contacting me',extra_tags='alert')
                    return HttpResponseRedirect('/')
                   
        else:
            contact = ContactUsForm()
        return render(request,'index.html',context={'contacts':contact})



@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('index'))

def register(request):
    if not request.session.get('username'):
        registered = False

        if request.method == 'POST':

            # Get info from "both" forms
            # It appears as one form to the user on the .html page
            user_form = UserForm(data=request.POST)

            # Check to see both forms are valid
            if user_form.is_valid():

                # Save User Form to Database
                user = user_form.save()

                # Hash the password
                user.set_password(user.password)

                # Update with Hashed password
                user.save()


                # Registration Successful!
                registered = True
                login(request,user)
                request.session['username']=user.username
          
                return HttpResponseRedirect(reverse('user_login'))

            else:
                # One of the forms was invalid if this else gets called.
                print(user_form.errors)

        else:
            # Was not an HTTP post so we just render the forms as blank.
            user_form = UserForm()

        # This is the render and context dictionary to feed
        # back to the registration.html file page.
        return render(request,'signup.html',
                            {'user_form':user_form,
                            'registered':registered})
    return HttpResponseRedirect(reverse('startPage'))

def user_login(request):
    if not request.session.get('username'):
        if request.method == 'POST':
            # First get the username and password supplied
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Django's built-in authentication function:
            user = authenticate(username=username, password=password)

            # If we have a user
            if user:
                #Check it the account is active
                if user.is_active:
                    # Log the user in.
                    login(request,user)
                    # Send the user back to some page.
                    # In this case their homepage.
                    #request.session.set_expiry(60)
                    request.session['username']=username
                    return HttpResponseRedirect(reverse('startPage'))
                else:
                    # If account is not active:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                messages.success(request, 'Wrong Credentials!',extra_tags='alert')

        else:
            #Nothing has been provided for username or password.
            return render(request, 'login.html',)
    return HttpResponseRedirect(reverse('startPage'))


@login_required
def main(request):
    
        return render(request,'main.html')



def lastContact(request):
    if request.session.get('username'):
         return HttpResponseRedirect(reverse('main'))
    return render(request,'lastContact.html')
    
  
    


