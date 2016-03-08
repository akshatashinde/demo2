import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
#from geography.models import ZipCode
# Create your models here.

# @python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
  
    def __str__(self):
        return self.question_text
        
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    


# @python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    
class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=100)
    def __str__(self):
        return self.instrument

class Album(models.Model):
    artist=models.ForeignKey(Musician,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date=models.DateField()
    num_stars=models.IntegerField()
    def __str__(self):
        return self.name

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    def __str__(self):
        return self.name

class Fruit(models.Model):
    fname = models.CharField(max_length=100, primary_key=True)
    def __str__(self):
        return self.fname


class Example(models.Model):
    foo_bar = models.IntegerField()
     

