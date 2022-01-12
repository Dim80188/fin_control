from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, ListView, View, UpdateView, DeleteView
from .models import *
from .forms import *
from django.urls import reverse_lazy, reverse
from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'h_finance/index.html')


# def register(request):
#     if request.method == 'POST':
#         form = UserRegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Вы успешно зарегистрировались')
#             return redirect('home')
#         else:
#             messages.error(request, 'Ошибка регистрации')

#     else:
#         form = UserRegisterForm()
#     return render(request, 'h_finance/register.html', {"form": form})

# def user_login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserLoginForm()
#     return render(request, 'h_finance/login.html', {"form": form})

# def user_logout(request):
#     logout(request)
#     return redirect('login')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class UserLoginView(LoginView):
    template_name = 'h_finance/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class UserRegisterView(CreateView):
    model = User
    template_name = 'h_finance/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    success_msg = 'Пользватель успешно создан'

    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        aut_user = authenticate(username=username, password=password)
        login(self.request, aut_user)
        return form_valid

    def get_success_url(self):
        return self.success_url


class AddCosts(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = CostForm
    template_name = 'h_finance/add_costs.html'
    success_url = reverse_lazy('add_costs')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

class AddInkome(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    form_class = InkomForm
    template_name = 'h_finance/add_inkome.html'
    success_url = reverse_lazy('add_inkome')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)



class AllCosts(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Costs
    template_name = 'h_finance/view_all_costs.html'
    context_object_name = 'costs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список расходов'
        return context

    def get_queryset(self):

        return Costs.objects.filter(author=self.request.user)

class AllInkome(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Inkome
    template_name = 'h_finance/view_inkome.html'
    context_object_name = 'inkome'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доходы'
        return context

    def get_queryset(self):
        return Inkome.objects.filter(author=self.request.user)


class DayCosts(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Costs
    template_name = 'h_finance/view_all_costs.html'
    context_object_name = 'costs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список расходов за сегодня'
        return context

    def get_queryset(self):

        now = datetime.now()
        return Costs.objects.filter(author=self.request.user, data__gte=now)

class DayInkome(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Inkome
    template_name = 'h_finance/view_inkome.html'
    context_object_name = 'inkome'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доходы за сегодня'
        return context

    def get_queryset(self):
        now = datetime.now()
        return Inkome.objects.filter(author=self.request.user, data__gte=now)

class WeekCosts(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Costs
    template_name = 'h_finance/view_all_costs.html'
    context_object_name = 'costs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список расходов за неделю'
        return context

    def get_queryset(self):

        now = datetime.now() - timedelta(minutes=60*24*7)
        return Costs.objects.filter(author=self.request.user, data__gte=now)

class WeekInkome(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Inkome
    template_name = 'h_finance/view_inkome.html'
    context_object_name = 'inkome'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доходы за неделю'
        return context

    def get_queryset(self):
        now = datetime.now() - timedelta(minutes=60*24*7)
        return Inkome.objects.filter(author=self.request.user, data__gte=now)

class MonthCosts(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Costs
    template_name = 'h_finance/view_all_costs.html'
    context_object_name = 'costs'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список расходов за месяц'
        return context

    def get_queryset(self):

        now = datetime.now() - timedelta(minutes=60*24*30)
        return Costs.objects.filter(author=self.request.user, data__gte=now)

class MonthInkome(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Inkome
    template_name = 'h_finance/view_inkome.html'
    context_object_name = 'inkome'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Доходы за месяц'
        return context

    def get_queryset(self):
        now = datetime.now() - timedelta(minutes=60*24*30)
        return Inkome.objects.filter(author=self.request.user, data__gte=now)


def select_period(request):
    if request.method == 'POST':
        form = SelectPeriodForm(request.POST)
        if form.is_valid():
            start_c = form.cleaned_data['start_data']
            end_c = form.cleaned_data['end_data']
            tranz_p = Costs.objects.filter(author=request.user, data__range=(start_c, end_c))
            return render(request, 'h_finance/view_selected_costs.html', {'tranz_p': tranz_p})

    else:
        form = SelectPeriodForm()
    return render(request, 'h_finance/select_period.html', {'form': form})

class UpdateCosts(LoginRequiredMixin, UpdateView):
    model = Costs
    template_name = 'h_finance/update_cost.html'
    form_class = CostForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].author:
            return self.handle_no_permission()
        return kwargs

class DeleteCosts(LoginRequiredMixin, DeleteView):
    model = Costs
    template_name = 'h_finance/view_all_costs.html'
    success_url = reverse_lazy('home')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.request.user != self.object.author:
            return self.handle_no_permission()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)



# def update_costs(request, pk):
#     success_update = False
#     get_cost = Costs.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = CostForm(request.POST, instance = get_cost)
#         if form.is_valid():
#             form.save()
#             success_update = True


#     context = {
#         'get_cost': Costs.objects.get(pk=pk),
#         'update': True,
#         'form': CostForm(instance = get_cost),
#         'success_update': success_update
#     }
#     return render(request, 'h_finance/update_cost.html', context)

# def delete_costs(request, pk):
#     get_cost = Costs.objects.get(pk=pk)
#     get_cost.delete()
#     return redirect(reverse('home'))
