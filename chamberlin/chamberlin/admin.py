from django.contrib import admin

from home.models import Home, About, Contact


# Customizes header on admin site
class MyAdminSite(admin.AdminSite):
    site_header = 'Mike Chamberlin Administration'


chamberlin_admin = MyAdminSite(name='admin')

# register models to chamberlin_admin
chamberlin_admin.register(Home)
chamberlin_admin.register(About)
chamberlin_admin.register(Contact)
