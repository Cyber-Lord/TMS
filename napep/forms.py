from django import forms
from .constants import *
from .models import Brand

class AddOwnerForm(forms.Form):
	fname = forms.CharField(max_length=30)
	lname = forms.CharField(max_length=30)
	oname = forms.CharField(max_length=30)
	state = forms.CharField(max_length=30)
	lga = forms.CharField(max_length=30)
	phone_number = forms.CharField(max_length=15)
	gender = forms.CharField(widget=forms.Select(choices=GENDER), max_length=6)
	occupation = forms.CharField(max_length=100)

class AddGroupForm(forms.Form):
	g_name = forms.CharField(max_length=50, label="Union Name")
	g_code = forms.CharField(max_length=10, label="Union Code")
	g_office = forms.CharField(max_length=200, label="Union Office Address")
	g_phone = forms.CharField(max_length=15, label="Union Contact Number")
	g_email = forms.CharField(max_length=50, label="Union Email Address")

class AddRiderForm(forms.Form):
	fname = forms.CharField(max_length=30)
	lname = forms.CharField(max_length=30)
	oname = forms.CharField(max_length=30)
	state = forms.CharField(max_length=30)
	address = forms.CharField(max_length=200)
	gender = forms.CharField(widget=forms.Select(choices=GENDER), max_length=6)
	phone_number = forms.CharField(max_length=15)
	passport = forms.ImageField()
	occupation = forms.CharField(max_length=20)
	union_id_number = forms.CharField(max_length=20)
	ice_name = forms.CharField(max_length=50)
	ice_number = forms.CharField(max_length=15)

class AddTricycleForm(forms.ModelForm):
	plate_number = forms.CharField(max_length=10)
	reg_number = forms.CharField(max_length=15)
	maker = forms.ModelChoiceField(queryset=Brand.objects.all(), label="Maker")
	dealer_name = forms.CharField(max_length=100, label="Dealer Name")
	dealer_phone = forms.CharField(max_length=15)
	dealer_receipt_number = forms.CharField(max_length=20)
	chasis_number = forms.CharField(max_length=30)
	receipt_issuance_date = forms.DateField()
	status = forms.CharField(widget=forms.Select(choices=GENDER), max_length=3)
	engine_number = forms.CharField(max_length=50)
	date_acquired = forms.DateField()
	owned_by = forms.CharField()


	class Meta:
		from .models import Tricycle
		model = Tricycle
		exclude = ('driver', 'group', 'maker', 'owned_by', 'id')

class AddBrandForm(forms.Form):
	brand_name = forms.CharField(max_length=20)


class AddUserForm(forms.Form):
	class Meta:
		from .models import User
		model = User
		fields = '__all__'