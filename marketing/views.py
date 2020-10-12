from django.shortcuts import render
from .forms import EmailForm
from .models import EmailSubscription
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


# Mailchimp Settings
api_key = settings.MAILCHIMP_API_KEY
server = settings.MAILCHIMP_DATA_CENTER
list_id = settings.MAILCHIMP_EMAIL_LIST_ID


# Subscription Logic
def subscribe(email):
    """
     Contains code handling the communication to the mailchimp api
     to create a contact/member in an audience/list.
     This process is described in the links below :
    """

    mailchimp = Client()
    mailchimp.set_config({
        "api_key": api_key,
        "server": server,
    })

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))


# Subscription View
def email_signup(request):
    if request.method == "POST":
        form = EmailForm(request.POST or None)
        if form.is_valid():
            email_q = EmailSubscription.objects.filter(email=form.instance.email)
            if email_q.exists():
                print(True)
                messages.info(request, "You Are Already Subscribed. Thank You ! ")  #Todo - This message not showing
            else:
                subscribe(form.instance.email)
                form.save()
                messages.success(request, "Your Email has been submitted. Thank you for joining! ")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


"""

    Implementing MailChimp with mailchimp-marketing library
        1. First generate an api key on mailchimp
        2. Get server/data-center from the api key. (e.g - 'us2')
        3. Create an audience/list on mailchimp
        4. Get the audience/list ID
        5. Keep the 3 Credentials in your SETTINGS
        6. Write a function that takes an 'email' as argument and 
                handles the mailchimp api communication with the mailchimp_marketing python library
        
        Some Useful Links below: 
        
        https://mailchimp.com/developer/guides/marketing-api-quick-start/
        https://mailchimp.com/developer/guides/create-your-first-audience/
        https://mailchimp.com/developer/api/marketing/list-members/

"""