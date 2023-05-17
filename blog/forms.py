from django import forms
from .models import Order, Customer, TGUser, Product


class OrderFrom(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
class BookForm(forms.Form):
    title = forms.CharField(max_length=200)
    description = forms.CharField(max_length=3000)
    publish_date = forms.DateField(required=False)

class TGUserForm(forms.ModelForm):
    class Meta:
        model = TGUser
        fields = ('tg_id', 'first_name', 'last_name', 'user_name', 'about')
