from django.contrib import admin
from .models import Memo


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    """메모 관리자 페이지"""
    list_display = ['title', 'author', 'created_at', 'updated_at']
    list_filter = ['created_at', 'updated_at', 'author']
    search_fields = ['title', 'content']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at', 'updated_at']
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
