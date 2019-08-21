from django.contrib import admin

from app.models import UserAccount,Outbox,Inbox

admin.site.register(UserAccount)
admin.site.register(Outbox)
admin.site.register(Inbox)