from django.db import models

# Create your models here.



# lesson Category table
class Categories(models.Model):
    category_name=models.CharField(max_length=500)

    def __str__(self):
        return self.category_name

# lesson table
class products(models.Model):
    product_name = models.CharField(max_length=2000)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_price = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='uploads/product_image')
    image2 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image3 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image4 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    image5 = models.ImageField(upload_to='uploads/product_image', null=True, blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.product_name
