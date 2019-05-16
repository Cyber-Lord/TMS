from django.shortcuts import render, redirect
from .models import *
from .decorators import state_required, ministry_required, s_bir_required, lga_required
from django.contrib import messages
from .forms import (
					AddUserForm,
					AddBrandForm,
					AddGroupForm,
					)


def home_page(request):
    owners_count = TricycleOwner.objects.all().count()
    riders_count = Rider.objects.all().count()
    tricycle_count = Tricycle.objects.all().count()
    brand_count = Brand.objects.all().count()
    context =  {
    	'owners_count': owners_count,
    	'riders_count': riders_count,
    	'tricycle_count': tricycle_count,
    	'brand_count': brand_count
    }
    return render(request, 'napep/home.html', context)


def brand_index(request):
	brands = Brand.objects.all()
	return render(request, 'napep/brand/brand.html', {'brands': brands})


def add_brand(request):
	if request.method == 'POST':
		form = AddBrandForm(request.POST)
		if form.is_valid():
			brand_name = form.cleaned_data.get('brand_name')
			Brand.objects.update_or_create(brand_name=brand_name)
			messages.success(request, ' {} has been successfully added'.format(brand_name))
			return redirect('brand')
		else:
			form = AddBrandForm(request.POST)
			return render(request, 'napep/brand/add_brand.html', {'form': form})
	else:
		return render(request, 'napep/brand/add_brand.html', {})


def group_index(request):
	groups = Group.objects.all()
	return render(request, 'napep/group/group.html', {'groups': groups})


def add_group(request):
	if request.method == 'POST':
		form = AddGroupForm(request.POST)
		if form.is_valid():
			union_name = form.cleaned_data.get('g_name')
			union_code = form.cleaned_data.get('g_code')
			union_phone = form.cleaned_data.get('g_phone')
			union_mail = form.cleaned_data.get('g_email')
			union_office = form.cleaned_data.get('g_office')
			if Group.objects.filter(group_code=union_code).exists():
				messages.success(request, 'A union with code \'{}\' code already exists'.format(union_code))
				return render(request, 'napep/group/add_group.html')
			Group.objects.create(
				group_name=union_name,
				group_code=union_code,
				office=union_office,
				contact_mail=union_mail,
				contact_number=union_phone)
			messages.success(request, ' {} ({}) has been successfully added'.format(union_name, union_code))
			return redirect('group')
		else:
			form = AddGroupForm(request.POST)
			return render(request, 'napep/group/add_group.html', {'form': form})
	else:
		return render(request, 'napep/group/add_group.html', {})

def unionadmin(request):
	return render(request, 'napep/union/admin.html', {})


def add_unionadmin(request):
	from django.contrib.auth.hashers import make_password
	if request.method == 'POST':
		form = AddUserForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			union_code = form.cleaned_data.get('union_code')
			if User.objects.filter(username=username).exists():
				messages.success(request, 'A user with that username already exists')
			User.objects.create(
				username=username, 
				password=password, 
				email=email, 
				group=union_code, 
				is_state=True)
			messages.success(request, '{} Successfully recorded'.format(username))
			return redirect('unionadmin')
		else:
			form = AddUserForm(request.POST)
			return render(request, 'napep/union/add_admin.html', {'form': form})
	else:
		context = {'unions': Group.objects.all()}
		return render(request, 'napep/union/add_admin.html', context)