from django.urls import path
from .views import *

urlpatterns = [
        path('', home_page, name='home_page_url'),
        path('candidate/create/', CandidateCreate.as_view(), name='candidate_create_url'),
        path('candidate/test/', AnswerCreate.as_view(), name='candidate_test_url'),
        path('master/', MasterProfile, name='master_url'),
        path('master/candidates_on_planet/', MasterCandidate, name='master_candidate_url')
]
