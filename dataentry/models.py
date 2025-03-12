from django.db import models
from django.contrib.auth.models import User



class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.customer_name


class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=25)
    designation = models.CharField(max_length=25)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    retirement = models.DecimalField(max_digits=10, decimal_places=2)
    other_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_benefits = models.DecimalField(max_digits=10, decimal_places=2)
    total_compensation = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.employee_name+' - '+self.designation
    

class Blog(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_body = models.TextField()

    def __str__(self):
        return self.blog_title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment
    

class Upload(models.Model):
    file = models.FileField(upload_to='data_imported/')
    model_name = models.CharField(max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name
    

class CompressImage(models.Model):
    QUALITY_CHOICES = [(i, i) for i in range(10, 101, 10)]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_img = models.ImageField(upload_to='images/original/')
    quality = models.IntegerField(choices=QUALITY_CHOICES, default=80)
    compressed_img = models.ImageField(upload_to='images/compressed/')
    compressed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username