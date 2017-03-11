from django.db import models

# Create your models here.
class GetClient(models.Model):
    client_name = models.TextField()
    client_phone = models.CharField(max_length=10)
    client_address = models.TextField()

    def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
        return self.client_name

    def return_name(self):
        # test - tryin to extract the postgres data
        return self.client_name


