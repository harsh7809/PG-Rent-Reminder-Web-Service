from django.shortcuts import render,HttpResponse
from sms.models import Contact
from datetime import date , datetime, timedelta
from twilio.rest import Client

# harsh
# 1234

def index(request):
  if request.method == "POST":
     number = request.POST.get("number")
     message = request.POST.get("message")
     dates= request.POST.get("dates")
     contact= Contact(number=number,mesasge=message,date=dates)
     contact.save()
     
     return render(request, 'index.html')
  return render(request, 'index.html')


def service(request):
    
    Data = Contact.objects.all()
   #  for a in Data:
   #     print(a.number)
    pgdata={
       'data':Data
            }

    return render(request, 'service.html', pgdata)




def sms(request):
    # to split date
    today = date.today()
    
    # to filter datebase for only today date
    filtered_data = Contact.objects.filter(date=today)
    
    n = []
    m = []

    for i in filtered_data:
        n.append(i.number)
        m.append(i.mesasge)
    
    for i, j in zip(n, m):
        account_sid = 'Enter your account_sid'
        auth_token = 'Enter your auth_token'
        twilio_phone_number = 'Enter twilio number'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=j,
            from_=twilio_phone_number,
            to='+91' + i  )
        n=[]
        m=[]
        

    return render(request, 'sms.html')


def all_alert(request):

    if request.method == "POST":
        message = request.POST.get("message")
    Data = Contact.objects.all()
    n=[]
    for a in Data:
       n.append(a.number)
    # print(n)
    # print(message)
    for i in n:
        account_sid = 'Enter your account_sid'
        auth_token = 'Enter your auth_token'
        twilio_phone_number = 'Enter twilio number'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to='+91' + i  )
        
    return render(request, 'all.html')
    




   

            

           

               

   
    
     
     
       
   