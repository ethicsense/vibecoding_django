from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import Memo
from .forms import MemoForm


class MemoListView(LoginRequiredMixin, ListView):
    """메모 목록 뷰"""
    model = Memo
    template_name = 'memos/memo_list.html'
    context_object_name = 'memos'
    paginate_by = 10
    
    def get_queryset(self):
        # 로그인한 사용자의 메모만 조회
        return Memo.objects.filter(author=self.request.user)


class MemoDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """메모 상세 뷰"""
    model = Memo
    template_name = 'memos/memo_detail.html'
    context_object_name = 'memo'
    
    def test_func(self):
        # 본인의 메모만 조회 가능
        memo = self.get_object()
        return memo.author == self.request.user


class MemoCreateView(LoginRequiredMixin, CreateView):
    """메모 작성 뷰"""
    model = Memo
    form_class = MemoForm
    template_name = 'memos/memo_form.html'
    success_url = reverse_lazy('memos:list')
    
    def form_valid(self, form):
        # 작성자를 현재 로그인한 사용자로 설정
        form.instance.author = self.request.user
        messages.success(self.request, '메모가 작성되었습니다.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '메모 작성에 실패했습니다. 입력 내용을 확인해주세요.')
        return super().form_invalid(form)


class MemoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """메모 수정 뷰"""
    model = Memo
    form_class = MemoForm
    template_name = 'memos/memo_form.html'
    success_url = reverse_lazy('memos:list')
    
    def test_func(self):
        # 본인의 메모만 수정 가능
        memo = self.get_object()
        return memo.author == self.request.user
    
    def form_valid(self, form):
        messages.success(self.request, '메모가 수정되었습니다.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, '메모 수정에 실패했습니다. 입력 내용을 확인해주세요.')
        return super().form_invalid(form)


class MemoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """메모 삭제 뷰"""
    model = Memo
    template_name = 'memos/memo_confirm_delete.html'
    success_url = reverse_lazy('memos:list')
    context_object_name = 'memo'
    
    def test_func(self):
        # 본인의 메모만 삭제 가능
        memo = self.get_object()
        return memo.author == self.request.user
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '메모가 삭제되었습니다.')
        return super().delete(request, *args, **kwargs)
