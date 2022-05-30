from django.db import models

class Home(models.Model):
    
 
    login = models.CharField(max_length=20)
    
    def __str__(self):
        return self.login

class Image(models.Model):
     text = models.CharField(max_length=60)   
     image = models.ImageField()     
        
     
     def __str__(self):
        return self.text
