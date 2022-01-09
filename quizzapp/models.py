from django.db import models

# Create the tables needed in the data base
class Images(models.Model):
    image_name = models.IntegerField()
    description = models.TextField()
    microscopy = models.CharField(max_length=40)
    cell_type = models.CharField(max_length=45)
    component = models.CharField(max_length=35)
    doi = models.CharField(max_length=25)
    organism = models.CharField(max_length=35)

class Answers(models.Model):
    question_id = models.IntegerField()
    answer = models.CharField(max_length=40)
    definition = models.TextField()

class Questions(models.Model):
    question = models.CharField(max_length=70)
    category = models.CharField(max_length=10)
    imagefield = models.CharField(max_length=15)
    points = models.IntegerField()
    n_answer = models.IntegerField()
    n_image = models.IntegerField()
    image = models.ManyToManyField(Images,related_name='question',blank=True)
    answer = models.ForeignKey(Answers,on_delete=models.CASCADE,null=True)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'

class Profile(models.Model):
    user_id = models.IntegerField()
    score = models.IntegerField()