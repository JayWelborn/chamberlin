# Django imports
from django.conf.urls import url

# Relative imports
from .views import AudioListView

app_name = 'listen'
urlpatterns = [
    # ex: [domain]/listen/
    url(r'^$', AudioListView.as_view(), name='index'),
]
