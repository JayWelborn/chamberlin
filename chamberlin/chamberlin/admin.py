from django.contrib import admin

from home.models import Home, About, Contact
from listen.models import AudioHome, AudioSample


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
