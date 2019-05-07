from django.shortcuts import render
from .models import Member
from django.views.generic import ListView,CreateView,UpdateView,DeleteView

# Create your views here.
class MemberListView(ListView):
    model = Member
    template_name = 'app1/index.html'
    context_object_name = 'profiles'

class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'

class MemberUpadateView(UpdateView):
    model = Member
    fields = '__all__'

class MemberDeleteView(DeleteView):
    model = Member
    success_url = '/'