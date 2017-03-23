from django.db import models


# Create your models here.
class GetClient(models.Model):
    client_name = models.TextField(default=None)
    client_phone = models.CharField(default=None,max_length=10)
    client_address = models.TextField(default=None)
    # log_no = models.TextField(default=None)
    # driver_no = models.TextField(default=None)
    # dob = models.TextField(default=None)
    # no_of_lessons = models.CharField(default=None, max_length=2)
    # comments = models.TextField(default=None)
    # balance = models.CharField(default=None, max_length=6)

    def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
        return self.client_name
        # return models.getdata_getclient.objects.all()




