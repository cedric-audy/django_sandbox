from django.shortcuts import render
from django.http import Http404

from .models import Project


def index(request):
    project_list = Project.objects.order_by('-pub_date')[:5]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project does not exist")
    return render(request, 'projects/detail.html', {'project': project})