from django.db import models
from requests import request


class Example(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _get_page(self, url):
        return request('GET', url)

    def name_in_page(self, url):
        resp = self._get_page(url)
        return self.name in resp.content
