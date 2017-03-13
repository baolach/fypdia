from django.db import models


# Create your models here.
class GetClient(models.Model):
    client_name = models.TextField(default=None)
    client_phone = models.CharField(default=None,max_length=10)
    client_address = models.TextField(default=None)

    def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
        return self.client_name
        # return models.getdata_getclient.objects.all()




