from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Memo(models.Model):
    """메모 모델"""
    title = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='memos',
        verbose_name='작성자'
    )
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    class Meta:
        verbose_name = '메모'
        verbose_name_plural = '메모 목록'
        ordering = ['-created_at']  # 최신순 정렬
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('memos:detail', kwargs={'pk': self.pk})
