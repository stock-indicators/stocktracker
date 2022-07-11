from django.contrib import admin


from .models import Assets, TwitterFollows, Message, Topic

admin.site.register(Assets)
admin.site.register(TwitterFollows)
admin.site.register(Message)
admin.site.register(Topic)