from .forms import TrainerRegistrationForm
from django.shortcuts import render,redirect
from .models import Trainer
from landing.decorators import allowed_users

# Create your views here.
@allowed_users(allowed_roles=['admin'])
def trainer_register(request):
    if request.method == "POST":
        form = TrainerRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = TrainerRegistrationForm()
    return render(request ,"register_trainer.html",{"form":form})

@allowed_users(allowed_roles=['admin','students','trainers'])
def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})

@allowed_users(allowed_roles=['admin','trainers'])
def edit_trainer(request,id):
    trainer = Trainer.objects.get(id=id)
    if request.method =="POST":
        form = TrainerRegistrationForm(request.POST,request.FILES,instance=trainer)
        if form.is_valid():
            form.save()
    else:
        form = TrainerRegistrationForm(instance=trainer)
    return render(request,"edit_trainer.html",{"form":form})

@allowed_users(allowed_roles=['admin','trainers'])
def trainer_profile(request,id):
    trainer = Trainer.objects.get(id=id)
    return render(request,"trainer_profile.html",{"trainer":trainer})

@allowed_users(allowed_roles=['admin'])
def delete_trainer(request,id):
    try:
        trainer = Trainer.objects.get(id=id)
        trainer.delete()
    except Trainer.DoesNotExist:
        trainer = None

    return redirect(trainer_list)