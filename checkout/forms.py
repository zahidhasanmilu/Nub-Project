# from django import forms
# from django.forms import ModelForm
# from .models import Order


# class StudentForm(ModelForm):
#     class Meta:
#         model=Order
#         fields = ('oid','pid','uid','full_name','email','address','town','zip_code','phone','price','comment','qty')
        

#         widgets ={
#             'oid' : forms.NumberInput(attrs={'class':'form-control'}),
#             'pid' : forms.NumberInput(attrs={'class':'form-control'}),
#             'uid' : forms.NumberInput(attrs={'class':'form-control'}),
#             'full_name' : forms.TextInput(attrs={'class':'form-control'}),
#             'email' : forms.EmailInput(attrs={'class':'form-control'}),
#             'address' : forms.TextInput(attrs={'class':'form-control'}),
#             'town' : forms.TextInput(attrs={'class':'form-control'}),
#             'zip_code' : forms.NumberInput(attrs={'class':'form-control'}),
#             'phone' : forms.TextInput(attrs={'class':'form-control'}),
#             'price' : forms.TextInput(attrs={'class':'form-control'}),
#             'comment' : forms.TextInput(attrs={'class':'form-control'}),
#             'qty' : forms.NumberInput(attrs={'class':'form-control'}),
            
#         }