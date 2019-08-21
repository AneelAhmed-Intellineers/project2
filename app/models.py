from django.db import models


class UserAccount(models.Model):

    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, unique=True)
    reciever = models.CharField(max_length=30, blank=True)
    message = models.TextField(max_length=200, blank=True)
    password = models.CharField(max_length=30)
    inbox = models.ForeignKey('Inbox', related_name='inbox', on_delete=models.CASCADE, blank=True, null=True)
    outbox = models.ForeignKey('Outbox', related_name='outbox', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Inbox(models.Model):

    message = models.TextField(max_length=200)

    def __str__(self):
        return self.message
    
class Outbox(models.Model):

    message = models.TextField(max_length=200) 
    def __str__(self):
        return self.message
    