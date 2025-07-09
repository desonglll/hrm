import json

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from employee.forms import EmployeeCreationForm


@csrf_exempt
def register(request):
    if request.method == "POST":
        body = json.loads(request.body)
        username = body.get("username")
        password = body.get("password")
        print(username, password)
        form = EmployeeCreationForm(data={"username": username, "password1": password, "password2": password})
        if form.is_valid():
            employee = form.save()
            return JsonResponse({"msg": "Success", "username": employee.username})
        else:
            return JsonResponse({"msg": "Failed", "errors": form.errors}, status=400)
    return JsonResponse({"msg": "Please use POST"}, status=405)
