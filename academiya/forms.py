from django import forms
from .models import Candidate, Planet, Answers

class CandidateForm(forms.Form):
        name = forms.CharField(max_length=100,)
        planet = forms.ModelChoiceField(queryset=Planet.objects.all())
        age = forms.IntegerField()
        email = forms.EmailField(max_length=50)

        name.widget.attrs.update({'class': 'form-control'})
        planet.widget.attrs.update({'class': 'form-control'})
        age.widget.attrs.update({'class': 'form-control'})
        email.widget.attrs.update({'class': 'form-control'})

        def save(self):
            new_candidate = Candidate.objects.create(
                name = self.cleaned_data['name'],
                planet = self.cleaned_data['planet'],
                age = self.cleaned_data['age'],
                email = self.cleaned_data['email'],
            )
            return new_candidate

class AnswerForm(forms.Form):
    value = forms.CharField(max_length=50)

    value.widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_value = Answers.objects.create(
            value = self.cleaned_data['value'],
        )
        return new_value
