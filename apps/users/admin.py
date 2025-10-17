from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# User 모델은 이미 등록되어 있으므로 커스터마이징이 필요한 경우에만 수정
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
