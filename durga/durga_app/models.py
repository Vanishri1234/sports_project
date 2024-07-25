from django.db import models


class userlogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Enquiry(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    contact_no = models.CharField(max_length=20)
    parent_name = models.CharField(max_length=100)
    parent_mobile_no = models.CharField(max_length=20)
    parent_email = models.EmailField()
    parent_address = models.TextField()
    weekly_sessions = models.CharField(max_length=1)
    how_did_you_know = models.CharField(max_length=50)
    other_details = models.TextField()
    age=models.CharField(max_length=20)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# Admisssion

class Register(models.Model):
    admission_no=models.CharField(max_length=100)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    adhar = models.CharField(max_length=12)
    parentName = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    place = models.CharField(max_length=500)  # Comma-separated list of kit items
    address = models.CharField(max_length=100)
    uniformSize = models.CharField(max_length=15)
    uniformColor = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    sessions = models.CharField(max_length=100)
    totalAmount = models.CharField(max_length=100)
    invoice_ID=models.CharField(max_length=100)
    date = models.DateField()
    blood_group=models.CharField(max_length=100)
    payment=models.CharField(max_length=100)
    balance = models.CharField(max_length=100)
    batchtime=models.CharField(max_length=100)




#sessions
class Duration(models.Model):
    session = models.CharField(max_length=100)
    weekly_sessions = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.session} - {self.weekly_sessions}"

class coachReg(models.Model):
    coachname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    coachType = models.CharField(max_length=100)
    adhar=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    document=models.CharField(max_length=100)



class Coach_allocation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=10)
    session = models.CharField(max_length=10)
    batchtime = models.CharField(max_length=10)
    coachname = models.CharField(max_length=10)
    coachType= models.CharField(max_length=10)