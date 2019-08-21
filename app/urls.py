from django.urls import path

from .views import user_view,user_login#, send_message

app_name = 'app'

urlpatterns = [
    path('', user_view, name='user_Account'),
    path('login',user_login, name='user_login' ),
   # path('messagesent', send_message, name='user_message')
]
