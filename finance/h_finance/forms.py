from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm, forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm, forms.ModelForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class CostForm(forms.ModelForm):
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(empty_label='Выберите категорию', label='Категория', queryset=Category.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    data = forms.DateField() # DateInput
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label='Сумма', widget=forms.NumberInput(attrs={'class': 'form-control'}))

    place_where_spent = forms.CharField(max_length=150, label='Где потрачено', widget=forms.TextInput(attrs={'class': 'form-control'}))
    comments = forms.CharField(label='Комментарии', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Costs
        fields = ['title', 'category', 'data', 'amount', 'place_where_spent', 'comments']


class SelectPeriodForm(forms.Form):
    start_data = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    end_data = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    class Meta:
        fields = ['start_data', 'end_data']
