from django import forms
from .models import Project, Comments, Profile
from django.forms.boundfield import BoundField



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comments
        # fields = ('poster', 'comment_content',)
        exclude = ['poster', 'date_posted']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'pic']



class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['poster', 'pub_date']
        

