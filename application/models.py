from django.db import models

class Job(models.Model):
    # Job Fields
    job_title = models.CharField(max_length=255)
    job_deadline_date = models.DateField(auto_now=False, auto_now_add=False)
    details_link = models.URLField(max_length=255)
    vacancy = models.IntegerField()
    def __str__(self):
        return self.job_title


class Application(models.Model):
    # Application Fiels
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=100,choices=GENDER)
    age = models.IntegerField()
    date_of_birth = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField(max_length=254)
    educ_background = models.TextField("Educational Background")
    position = models.CharField(max_length=255)
    phone = models.CharField(' Phone Contact', max_length=100, null=True)
    experience = models.TextField()
    publication = models.TextField(blank=True)
    training = models.TextField('Training or Certifications', blank=True)

    def __str__(self):
        return self.first_name
    
    



