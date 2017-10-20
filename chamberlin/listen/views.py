from django.views.generic import ListView
from django.utils import timezone

from .models import AudioHome, AudioSample


class AudioListView(ListView):
    template_name = 'listen/index.html'
    context_object_name = 'sample_list'
    model = AudioSample

    def get_context_data(self, **kwargs):
        """
        return data from most recent update to Audio Home object
        """
        context = super(AudioListView, self).get_context_data(**kwargs)
        if AudioHome.objects:
            context['audio'] = AudioHome.objects.latest('pub_date')
            return context
        else:
            return []

    def get_queryset(self):
        """
        Return Audio Samples sorted by date
        """
        samples = AudioSample.objects.distinct()
        if samples:
            return samples.filter(
                pub_date__lte=timezone.now()
            ).order_by('-pub_date')
        else:
            return []
