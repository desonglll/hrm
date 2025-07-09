from django.shortcuts import render

from django.shortcuts import render, redirect

from employee.forms import EmployeeCreationForm
from django.contrib.auth.models import Permission


def register(request):
    if request.method == "POST":
        print(request.POST)
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()

            view_employee_permission = Permission.objects.get(codename="view_employee")
            change_employee_permission = Permission.objects.get(
                codename="change_employee"
            )
            user.user_permissions.add(view_employee_permission)
            user.user_permissions.add(change_employee_permission)

            return redirect("login")
    else:
        form = EmployeeCreationForm()
    return render(request, "registration/register.html", {"form": form})
