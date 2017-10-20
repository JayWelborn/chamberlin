from django.contrib import admin

from home.models import Home, About, Contact
from listen.models import AudioHome, AudioSample
from blog.models import Tag, Entry


# Add blog entries
class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Publication Date', {'fields': ['pub_date']}),
        ('Video', {'fields': ['youtube_video']}),
        ('Entry', {'fields': ['body', 'tags']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SampleInline(admin.TabularInline):
    model = AudioSample
    extra = 0


class AudioAdmin(admin.ModelAdmin):
    model = AudioHome
    inlines = (SampleInline,)


# Customizes header on admin site
class MyAdminSite(admin.AdminSite):
    site_header = 'Mike Chamberlin Administration'


chamberlin_admin = MyAdminSite(name='admin')

# register models to chamberlin_admin
chamberlin_admin.register(Home)
chamberlin_admin.register(About)
chamberlin_admin.register(Contact)
chamberlin_admin.register(AudioHome, AudioAdmin)
chamberlin_admin.register(Entry, BlogAdmin)
chamberlin_admin.register(Tag, TagAdmin)
