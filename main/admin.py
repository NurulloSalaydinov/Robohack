from django.contrib import admin
from .models import *

@admin.register(Contest)
class AdminContest(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Event)
class Event(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Contact)
admin.site.register(EventRegister)
admin.site.register(ContestRegister)
admin.site.register(ContestQuestion)
admin.site.register(EventQuestion)
admin.site.register(TimeLine)
admin.site.register(TimeLineEvent)
admin.site.register(Images)
admin.site.register(HistoryImage)
admin.site.register(UsefullIconContest)
admin.site.register(UsefullIconEvent)
admin.site.register(WhoIsForEvent)
admin.site.register(WhoIsForContest)
admin.site.register(WhatTookContest)
admin.site.register(WhatTookEvent)

