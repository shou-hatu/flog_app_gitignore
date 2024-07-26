from django.contrib import admin
from .models import Quiz, Player_result
# Register your models here.
# モデルをimportし、admin.site.register(モデル名)を記述することで管理者サイトにモデルを表示することができる
admin.site.register(Quiz)
admin.site.register(Player_result)
