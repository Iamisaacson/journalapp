from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django import forms
from .models import Post

class ContactForm(forms.Form):
  name = forms.CharField(max_length=100)
  email = forms.EmailField()
  message = forms.CharField(widget=forms.Textarea)

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['title', 'content']
  
  def clean_title(self):
    title = self.cleaned_data.get('title')
    if "badword" in title.lower():
      raise forms.ValidationError("Inappropriate title not allowed.")
    return title
  

# class CreatePostView(LoginRequiredMixin, CreateView):
#   model = Post
#   fields = ['title', 'content', 'author']
#   template_name = 'pages/post_form.html'
#   success_url = '/blog/'