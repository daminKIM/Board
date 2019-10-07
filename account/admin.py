from django.contrib import admin

from account.models import User
from board.models import Board,Comment
# Register your models here.

admin.site.register(User)
admin.site.register(Board)
admin.site.register(Comment)

