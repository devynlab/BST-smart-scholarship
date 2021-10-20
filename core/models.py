from datetime import date

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female')
]

STATUS_CHOICES = [
    ('freshman', 'Freshman'),
    ('sophomore', 'Sophomore'),
    ('junior', 'Junior'),
    ('senior', 'Senior')
]


class Student(models.Model):
  student_id = models.CharField(max_length=17, unique=True)
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  phone_number = PhoneNumberField()
  email_address = models.EmailField()
  gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
  date_of_birth = models.DateField()
  status = models.CharField(max_length=9, choices=STATUS_CHOICES)
  cummulative_gpa = models.FloatField()
  current_gpa = models.FloatField()
  credit_hours = models.PositiveIntegerField()

  class Meta:
    ordering = ('last_name', 'cummulative_gpa')

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Applicant(models.Model):
  student = models.OneToOneField(Student, on_delete=models.CASCADE)
  eligible = models.BooleanField(blank=True)

  def __str__(self):
    return f"{self.student.first_name} {self.student.last_name}"

  def save(self, *args, **kwargs):
    # from .utils import highest_cummulative_gpo, junior_student
    # self.eligible = self.student.cummulative_gpa == highest_cummulative_gpo()
    # print(junior_student())
    age = date.today().year - self.student.date_of_birth.year
    print(self.student.cummulative_gpa)
    print(self.student.credit_hours)
    print(age)
    if self.student.cummulative_gpa >= 3.2 and self.student.credit_hours >= 12 and age <= 23:
      self.eligible = True
    else:
      self.eligible = False
    super().save(*args, **kwargs)


class Accounts(models.Model):
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  tuition_fee = models.FloatField()

  class Meta:
    verbose_name_plural = 'Accounts'

  def __str__(self):
    return f"{self.student} - {self.tuition_fee}"


class Awarded(models.Model):
  student_id = models.CharField(max_length=10, unique=True)
  full_name = models.CharField(max_length=100)
  awarded_amount = models.FloatField()

  class Meta:
    verbose_name_plural = 'Awarded'

  def __str__(self):
    return f"{self.full_name} has been awarded {self.awarded_amount}"
