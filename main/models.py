from django.db import models
from datetime import datetime as dt


class New(models.Model):
    header = models.CharField(max_length=300)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')
    date_published = models.DateTimeField(default=dt.now)

    def get_upload_to(self, filename):
        folder_name = 'images'
        filename = self.file.field.storage.get_valid_name(filename)
        return os.path.join(folder_name, filename)


class Portfolio(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    img = models.ImageField(upload_to='portfolio/')

    def get_upload_to(self, filename):
        folder_name = 'portfolio'
        filename = self.file.field.storage.get_valid_name(filename)
        return os.path.join(folder_name, filename)
