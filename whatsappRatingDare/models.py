
from email.policy import default
from django.db import models



RATTING_CHOICE = (('1','1') , ('2' , '2') , ('3' , '3') , ('4','4') )	


class answerModel(models.Model):
    name = models.CharField(max_length=50 , blank=True , null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    answer = models.IntegerField(default=0)
    answer_for = models.CharField(max_length=50 , blank=True , null=True)
     
    def __str__(self):
        return f" {self.name} || {self.id} || {self.answer} || {self.created_time}" 
    
    class Meta:
        ordering=('created_time' , )
    
    
    
    
# Create your models here.
class personOwnChart(models.Model):
    name = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    answersChart = models.ManyToManyField(answerModel , blank=True)
    
    
    # According to this question  user ko uske friend rate denge
    q1 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q2 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q3 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q4 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q5= models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q6= models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q7 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q8 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True  )
    q9 = models.CharField(choices =  RATTING_CHOICE , max_length=50  ,blank = False , null=True  )
    q10 = models.CharField(choices =  RATTING_CHOICE , max_length=50  , blank = False , null=True )
     
    
     
    def __str__(self):
        return f" {self.name} || {self.id} || {self.created_time} " 