from django.contrib import admin
from .models import Member, GroupChat, Message

# Register your models here.

admin.site.register(Member)
admin.site.register(GroupChat)
admin.site.register(Message)
