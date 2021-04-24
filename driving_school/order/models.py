from django.db import models
from django.contrib.auth.models import User
from instructor.models import instructor_information
from home.models import products
# Create your models here.


# Order table to store all order details
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Lesson = models.ForeignKey(
        products, on_delete=models.CASCADE, blank=True,
        null=True
    )
    Instructor = models.ForeignKey(
        instructor_information, on_delete=models.CASCADE,
        blank=True, null=True
    )
    order_id = models.CharField(max_length=1000)
    Lesson_price = models.CharField(max_length=1000)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    zip = models.CharField(max_length=1000)
    ordered = models.BooleanField(default=False)
    instructor_cancel_order = models.BooleanField(default=False)
    customer_cancel_order = models.BooleanField(default=False)
    Completed_order = models.BooleanField(default=False)
    order_date = models.CharField(max_length=1000)

    def __str__(self):
        return self.order_id + " - " + self.user.first_name + " " + self.user.last_name


# Table for all cancelled orders in less than 24 hours
class cancel_order_for_money_back(models.Model):
    class Meta:
        verbose_name_plural = 'Refund To Cancelled Orders'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    Cancel_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " - " + self.order.order_id
