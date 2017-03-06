from django.db import models
from django.utils.timezone import datetime

from.model_fields import AudioFileField


class AudioHome(models.Model):

    class Meta:
        verbose_name_plural = 'Audio Sample Page'

    header = models.CharField(max_length=40)
    pub_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.header


class AudioSample(models.Model):

    title = models.CharField(max_length=40)
    audio_track = AudioFileField(upload_to='media/audio/%Y/%m/%d', max_upload_size=2621440)
    sample_image = models.ImageField(upload_to='media/images/%Y/%m/%d')
    pub_date = models.DateField(default=datetime.now)
    home = models.ForeignKey(AudioHome, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
