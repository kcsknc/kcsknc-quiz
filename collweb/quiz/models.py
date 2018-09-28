from django.db import models

# Create your models here.

YEAR_CHOICE = (
    ('firstyear','I'),
    ('secondyear', 'II'),
    ('thirdyear','III'),
)



class dbms_questions(models.Model):
    class Meta:
        verbose_name_plural = "dbms_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)



class dbms_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)


class os_questions(models.Model):
    class Meta:
        verbose_name_plural = "os_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)



class os_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)

class dm_questions(models.Model):
    class Meta:
        verbose_name_plural = "dm_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)



class dm_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)


class ca_questions(models.Model):
    class Meta:
        verbose_name_plural = "ca_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)

class ca_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)



class vb_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)

class vb_questions(models.Model):
    class Meta:
        verbose_name_plural = "vb_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)



class cpp_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)

class cpp_questions(models.Model):
    class Meta:
        verbose_name_plural = "cpp_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)



class c_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)

class c_questions(models.Model):
    class Meta:
        verbose_name_plural = "c_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)



class java_score(models.Model):
    name = models.CharField(max_length=264,null=True)
    regno = models.CharField(max_length=264,unique=True)
    year = models.CharField(max_length=26,choices=YEAR_CHOICE, default='third')
    Score=models.CharField(max_length=10,null=True)
    def __str__(self):
        return (self.regno)

class java_questions(models.Model):
    class Meta:
        verbose_name_plural = "java_questions"
    question = models.CharField(max_length = 1000)
    a = models.CharField(max_length = 1000)
    b = models.CharField(max_length = 1000)
    c = models.CharField(max_length = 1000)
    d = models.CharField(max_length = 1000)
    answer = models.CharField(max_length=1)


    def __str__(self):
        return (self.question)
