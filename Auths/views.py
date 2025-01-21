from django.shortcuts import render
from allauth.account.forms import LoginForm,SignupForm
from allauth.account.views import login

# Create your views here.
def CustomLogin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            is_logined = form.login()
            if is_logined:
                print("passed")
            else:
                print("failed")
        print(dir(form))
    else:
        form = LoginForm()

    return render(request,"login.html",{"form":form})


