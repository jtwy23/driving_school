from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
import hashlib
from instructor.models import instructor_information
# Create your models here.


# Sends generated activation link
class EmailConfirmed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=500)
    email_confirmed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'Email-Confirmed Users'


@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirmed_instance = EmailConfirmed(user=instance)
        user_encoded = f'{instance.email}-{dt}'.encode()
        activation_key = hashlib.sha224(user_encoded).hexdigest()
        email_confirmed_instance.activation_key = activation_key
        email_confirmed_instance.save()


# Category lesson table
class Categories(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    category_name = models.CharField(max_length=500)

    def __str__(self):
        return self.category_name


# Lesson table
class products(models.Model):
    class Meta:
        verbose_name_plural = 'Products'

    product_name = models.CharField(max_length=2000)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    Intructor = models.ForeignKey(
        instructor_information,
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    product_price = models.CharField(max_length=2000)
    image = models.ImageField(
        upload_to='uploads/product_image', blank=True, default='')
    image2 = models.ImageField(
        upload_to='uploads/product_image', blank=True, default='')
    image3 = models.ImageField(
        upload_to='uploads/product_image', blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.product_name

    def avarege_review(self):
        filter_product_reviews = reviews.objects.filter(product=self)
        filter_product_reviews_qty = reviews.objects.filter(product=self).count()

        # making average rating
        total_ratings = 0
        for i in filter_product_reviews:
            total_ratings = total_ratings + int(i.ratings)
            # print(total_ratings)
        if filter_product_reviews_qty == 0:
            average_rating = 0
        else:
            average_rating = total_ratings / filter_product_reviews_qty
            print(average_rating)
        average_rating = "%0.1f" % average_rating
        return average_rating

    def product_reviews_qty(self):
        filter_product_reviews_qty = reviews.objects.filter(product=self).count()
        return filter_product_reviews_qty


# Customer more details
class customer_more_information(models.Model):
    class Meta:
        verbose_name_plural = 'More Customer Information'

    Customer = models.ForeignKey(User, on_delete=models.CASCADE)
    Phone_number = models.CharField(max_length=200)
    Postcode = models.CharField(max_length=200, default='')
    Address = models.CharField(max_length=200)


class reviews(models.Model):
    class Meta:
        verbose_name_plural = 'Products Review'
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    ratings = models.CharField(max_length=1)
    review_text = models.TextField()
    review_time = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.customer.first_name + " - "+self.ratings

    