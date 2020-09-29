from django.shortcuts import render, get_object_or_404
from .models import Project,Skills
# Create your views here.
def home(request):
    projects = Project.objects.all()
    skills = Skills.objects.all()
    return render(request,'portfolio/home.html',{'projects':projects,'skills':skills})


def detail(request,project_id):
    project_detail = get_object_or_404(Project,pk=project_id)
    #project_id = 2
    return render(request, 'portfolio/detail_project.html',{'project_detail': project_detail})
