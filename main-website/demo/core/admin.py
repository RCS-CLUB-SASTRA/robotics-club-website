from django.contrib import admin
from .models import (
    UserProfile,
    Event,
    Course,
    BlogPost,
    Achievement,
    Meeting,
)

admin.site.register(UserProfile)
admin.site.register(Event)
admin.site.register(Course)
admin.site.register(BlogPost)
admin.site.register(Achievement)
admin.site.register(Meeting)
