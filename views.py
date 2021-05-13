from django.shortcuts import render

from django.shortcuts import render

# Create your views here.
def home(request):
  return render(request, "home.html")

def result(request):
  groupnr = int(request.GET['group'])
  if groupnr == 5:
    result = "우리는 5조"

  else:
    result = ":)"

  return render(request, "result.html", {"result": result})
