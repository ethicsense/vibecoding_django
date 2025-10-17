from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegistrationForm


class RegisterView(CreateView):
    """회원가입 뷰"""
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '회원가입이 완료되었습니다! 로그인해주세요.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, '회원가입에 실패했습니다. 입력 내용을 확인해주세요.')
        return super().form_invalid(form)


class UserLoginView(LoginView):
    """로그인 뷰"""
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        messages.success(self.request, f'{form.get_user().username}님, 환영합니다!')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '아이디 또는 비밀번호가 올바르지 않습니다.')
        return super().form_invalid(form)


class UserLogoutView(LogoutView):
    """로그아웃 뷰"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, '로그아웃되었습니다.')
        return super().dispatch(request, *args, **kwargs)

