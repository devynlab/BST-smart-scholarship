from django.shortcuts import render

from .forms import ApplicationForm
from .models import Applicant, Student


def index(request):
  student_qs = Student.objects.all().values_list()
  print(student_qs)
  cummulative_gpo = [student_gpo[-3] for student_gpo in student_qs]
  print(cummulative_gpo)
  print(max(cummulative_gpo))
  context = {
      'cummulative_gpo': cummulative_gpo
  }
  return render(request, 'index.html', context)


def application_view(request):
  form = ApplicationForm()
  if request.method == 'POST':
    form = ApplicationForm(request.POST)
    if form.is_valid():
      form.save()
  context = {
      'form': form,
  }
  return render(request, 'application.html', context)
