from django.db import models

class Roles(models.Model):
    role_names = models.CharField(max_length=500)

    def __str__(self):
        return self.role_names
    
class Personal_Info(models.Model):
    info_name = models.CharField(max_length=500)
    info_value = models.CharField(max_length=500)

    def __str__(self):
        return self.info_name + "=" +self.info_value

class Facts_Info(models.Model):
    facts_name = models.CharField(max_length=500)
    facts_value = models.CharField(max_length=500)
    facts_description = models.CharField(max_length=500)

    def __str__(self):
        return self.facts_name + "=" + self.facts_value

class Skills_Info(models.Model):
    skill_name = models.CharField(max_length=500)
    skill_percentage = models.CharField(max_length=500)

    def __str__(self):
        return self.skill_name + "=" + self.skill_percentage

class Education_Info(models.Model):
    course_name = models.CharField(max_length=500)
    course_year = models.CharField(max_length=500)
    course_university = models.CharField(max_length=500)
    course_info = models.CharField(max_length=500)
    course_grade = models.CharField(max_length=500)

    def __str__(self):
        return self.course_name
    
class Contact_Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    message = models.TextField()

    def __str__(self):
        return self.name+" "+self.email
    
class About_Me(models.Model):
    about_info = models.CharField(max_length=5000)

    def __str__(self):
        return self.about_info
    
class Resume_Summary(models.Model):
    summary = models.CharField(max_length=5000)

    def __str__(self):
        return self.summary

class Project_Details(models.Model):
    project_name = models.CharField(max_length=5000)
    client_name = models.CharField(max_length=5000)
    duration = models.CharField(max_length=1000)
    organization = models.CharField(max_length=1000)
    technologies_used = models.CharField(max_length=5000)

    def __str__(self):
        return self.project_name

class Project_Desc(models.Model):
    description = models.TextField()
    project = models.ForeignKey(Project_Details, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.project_name + "=" + self.description

class My_Contact_Details(models.Model):
    contact_info = models.CharField(max_length=1000)
    contact_value = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.contact_info
    
    