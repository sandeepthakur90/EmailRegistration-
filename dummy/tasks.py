from django.shortcuts import render,redirect
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from celery import shared_task

@shared_task
def MailSendFunction(otp,email):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'   
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

    subject = "Your Registration is sucessfull"
    html_content = f"<html>your registration successfull otp is :{otp} </html>"
    sender = {"name":"sandeep","email":"sandeep@thoughtwin.com"}
    to = [{"email":email,"name":"name"},]
    reply_to = {"email":"replytome@gmail.ca","name":"FName LName"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, reply_to=reply_to, html_content=html_content, sender=sender, subject=subject)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    
    