from django.contrib import admin

from .models import Accounts, Applicant, Awarded, Student


@admin.register(Accounts)
class AccountsAdmin(admin.ModelAdmin):
  # list_display = ['tuition_fee']
  # search_fields = ('')
  pass


@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
  # list_display = ['applicant', 'eligible']
  # search_fields = ('')
  pass


@admin.register(Awarded)
class AwardedAdmin(admin.ModelAdmin):
  list_display = ['full_name', 'awarded_amount']
  # search_fields = ('')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
  list_display = ['student_id', 'last_name', 'cummulative_gpa']
  # search_fields = ('')
