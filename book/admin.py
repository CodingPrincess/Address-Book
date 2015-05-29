from django.contrib import admin
from book.models import PhoneNumber, Email_Add, Pin, SocialNetwork, Website

# Register your models here.
admin.site.register(PhoneNumber)
admin.site.register(SocialNetwork)
admin.site.register(Website)
admin.site.register(Email_Add)
admin.site.register(Pin)
