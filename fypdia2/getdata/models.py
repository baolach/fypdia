from django.db import models

# Create your models here.
class GetClient(models.Model):
    client_name = models.TextField(default=None)
    client_phone = models.CharField(default=None,max_length=10)
    client_address = models.TextField(default=None)
    log_no = models.TextField(default=None, max_length = 9)
    driver_no = models.TextField(default=None, max_length = 5)
    dob = models.TextField(default=None)
    no_of_lessons = models.CharField(default=None, max_length =     def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
3)
    balance_due = models.CharField(default=None, max_length = 3)
    comments = models.TextField(default=None)

        return self.client_name
        #return models.getdata_getclient.objects.all()

class GetLesson(models.Model):
    lesson_name = models.TextField(default=None,)
    lesson_date = models.DateField(default=None)
    lesson_time = models.TimeField(default=None)
    lesson_location = models.TextField(default=None)
    lesson_comments = models.TextField(default=None)


    def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
        return self.lesson_date
        #return models.getdata_getclient.objects.all()



class GetLocation(models.Model):
    type = models.TextField(default=None)
    coordinates = models.TextField(default=None)
    x = models.CharField(default=None, max_length=30)
    y = models.CharField(default=None, max_length=30)

    def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
        return self.type
        #return models.getdata_getclient.objects.all()



#
# class GetExpenses(models.Model):
#     expense_name = models.TextField(default=None,)
#     expense_amount = models.CharField(default=None, max_length=6)
#     expense_date = models.DateField(default=None)
#
#     def __str__(self):  # rather than just saying post object, we can name the posts for the admin page
#         return self.expense_name
#         #return models.getdata_getclient.objects.all()