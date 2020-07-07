from django.shortcuts import render

from .models import Project


def index(request):
    project_list = Project.objects.order_by('-pub_date')[:5]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html', context)
