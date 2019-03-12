from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import View
# Create your views here.

def home_page(request):
    return render(request, 'academiya/home_page.html')

def test_form(request):
    return render(request, 'academiya/candidate_test_form.html')

class CandidateCreate(View):
    def get(self, request):
        form = CandidateForm()
        return render(request, 'academiya/candidate_create_form.html', context={'form': form})

    def post(self, request):
        bound_form = CandidateForm(request.POST)
        if bound_form.is_valid():
            new_candidate = bound_form.save()
            return redirect('candidate_test_url')
        return render(request, 'academiya/candidate_create_form.html', context={'form': bound_form})

def Test_tasks(request):
    tests = Test_task.objects.all()
    return render(request, 'academiya/candidate_test_form.html', context={'tests': tests})

class AnswerCreate(View):
    def get(self,request):
        form = AnswerForm()
        tests = Test_task.objects.all()
        return render(request, 'academiya/candidate_test_form.html', context={'form': form, 'tests': tests})

    def post(self, request):
        bound_form = AnswerForm(request.POST)
        if bound_form.is_valid():
            new_value = bound_form.save()
            return redirect('home_page_url')
        return render(request, 'academiya/candidate_test_form.html', context={'form': bound_form})

def MasterProfile(request):
    masters = Master.objects.all()
    return render(request, 'academiya/masters_profile.html', context={'masters': masters})

def MasterCandidate(request):
    answer =  Answers.objects.select_related().all()
    candidates = Candidate.objects.select_related().values("planet")
    candidate = Candidate.objects.select_related().values("id")
    answers = Answers.objects.select_related().values("candidate")
    masters = Master.objects.select_related("planet").values("planet")
    for candidates in masters:
            return render(request,'academiya/candidate_on_planet.html',context={'answer': answer})
    #    answers = Answers.objects.select_related().all()
    return render(request, 'academiya/candidate_on_planet.html', context={'candidates': candidates, 'masters': masters})
