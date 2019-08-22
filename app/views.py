from django.shortcuts import render, redirect

from .models import UserAccount,Inbox,Outbox

def user_view(request):

    if request.method == 'GET':
        return render(request, "user.html", {})

    elif request.method == 'POST':
        user = UserAccount()
        
        user.name = request.POST.get('user_name')
        user.email = request.POST.get('user_mail')
        user.password = request.POST.get('user_password')
        user.save()
        context = {
            'name':user.name,
            'email':user.email,
            'inbox':user.inbox,
            'outbox':user.outbox,
        }
        return render(request, "login.html", context)


def user_login(request):

    if request.method == 'GET':

        return render(request, "user_login.html", {})

    if request.method == 'POST':
        email = request.POST.get('user_mail')
        password = request.POST.get('user_password')
        context = {

            'name': UserAccount.objects.get(email=email).name,
            'email':UserAccount.objects.get(email=email).email,
            'inbox':UserAccount.objects.get(email=email).inbox,
            'outbox':UserAccount.objects.get(email=email).outbox

        }

        return render(request, "login.html",context)
        

def send_message(request):
    
    if request.method == 'GET':
        
        return render(request, "login.html",{})

    if request.method == 'POST':

        uremail = request.POST.get('your_mail')
        email = request.POST.get('target_mail')
        message = request.POST.get('user_message')
        user = UserAccount.objects.get(email=uremail)
        rcv_user = UserAccount.objects.get(email=email)
        
        outbox = Outbox()
        outbox.message = message
        outbox.user_account = UserAccount.objects.get(email=uremail)
        outbox.save()
        user.outbox = outbox
        user.save()
        inbox = Inbox()
        inbox.message = message
        inbox.user_account = outbox.user_account
        inbox.save()
        rcv_user.inbox = inbox
        rcv_user.save() 
        outbox = Outbox.objects.filter(user_account=user)
        
        context = {
            'name':user.name,
            'email':user.email,
            'inbox':user.inbox,
            'outbox':outbox
        }
        
        return render(request, 'login.html',context)