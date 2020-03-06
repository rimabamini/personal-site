from django.shortcuts import render
from projects.models import Project

# index view will show a snippet of information about each project 
def project_index(request):
    # perform query to retrieve all objcts in projects table 
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

# detail view will show more information on a particular topic 
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)