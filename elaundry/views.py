from django.shortcuts import render
from elaundry.models import *


def register_users(request):
	if(request.POST):
		name = request.POST.get("name")
		rollNo = request.POST.get("rollNo")
		pwd = request.POST.get("password")
		cpwd = request.POST.get("confirmpassword")		
		hostel = request.POST.get("hostel")
		phone = request.POST.get("phno")
		mailId = request.POST.get("mail")

		if(pwd == cpwd):
			Register.objects.create(name = name, rollNo = rollNo, password = pwd, hostel = hostel, mobileNumber = phone, mailId = mailId).publish()
		else:
			print("Re-enter the password")

	return render(request, 'elaundry/login.html', {})

def Home(request):
	if(request.POST):
		if(name == request.POST.get("loginName") and pwd == request.POST.get("loginPassword")):
			return render(request, 'elaundry/login.html', {}) #login ki jagah placeorder.html
		else:
			return render(request, 'elaundry/register_users.html', {})

	return render(request, 'elaundry/login.html', {}) #login ki jagah placeorder.html
		
