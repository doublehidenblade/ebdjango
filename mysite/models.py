from django.db import models
# import magic
# from django import forms


# Create your models here.
class person(models.Model):
    GENDER_CHOICES = {('Male','Male'),  ('Female', 'Female')}
    YEAR_CHOICES = {('freshman', 'freshman'),('sophomore', 'sophomore'),('junior', 'junior'),('senior', 'senior'),('graduate', 'graduate')}
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default="")
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, default="")
    major = models.CharField(max_length=80, default="", blank=True)
    email = models.EmailField(max_length=196, default="", blank=True)
    password = models.TextField(max_length=30, default="")

    def __str__(self):
        return self.name


class subs(models.Model):
    email = models.EmailField(max_length=196, default="")

    def __str__(self):
        return self.email


class film(models.Model):
    embedcode = models.URLField(max_length=500, default="")
    name = models.TextField(max_length=200, default="")

    def __str__(self):
        return self.name


class memory(models.Model):
    pic = models.FileField(upload_to="media", null=True, blank=True)
    name = models.TextField(max_length=200, default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.TextField(max_length=60, default="random guy")

    # def clean_image(self):
    #     image = self.get("pic", False)
    #     filetype = magic.from_buffer(image.read())
    #     if (not "jpg" in filetype) or (not "png" in filetype) or (not "jpeg" in filetype):
    #         raise forms.ValidationError("File has to end with jpg, jpeg, or png.")
    #     return image

    def __str__(self):
        return self.name