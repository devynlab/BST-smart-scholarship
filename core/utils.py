from .models import Student

student_qs = Student.objects.all().values_list()


def highest_cummulative_gpo():
  return max(student_gpo[-3] for student_gpo in student_qs)


def highest_current_gpo():
  return max(student_gpo[-2] for student_gpo in student_qs)


def junior_student():
  return max(age[-5] for age in student_qs)
