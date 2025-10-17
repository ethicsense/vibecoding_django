from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    """메모 작성/수정 폼"""
    
    class Meta:
        model = Memo
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '메모 제목을 입력하세요'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': '메모 내용을 입력하세요'
            }),
        }
