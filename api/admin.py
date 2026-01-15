from django.contrib import admin
from .models import (
    User, UserInterest, Item,
    UserSearch, UserView, UserLike, UserSave, UserSettings
)

admin.site.register(User)
admin.site.register(UserInterest)
admin.site.register(Item)
admin.site.register(UserSearch)
admin.site.register(UserView)
admin.site.register(UserLike)
admin.site.register(UserSave)
admin.site.register(UserSettings)
