from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView, ListView

from .models import Education, Experience, Project, Skill


def home(request):
    featured_projects = Project.objects.filter(featured=True)[:3]
    skills = Skill.objects.all()
    recent_experience = Experience.objects.first()
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'recent_experience': recent_experience,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills_by_category = {}
    
    for skill in Skill.objects.all():
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context = {
        'experiences': experiences,
        'education': education,
        'skills_by_category': skills_by_category,
    }
    return render(request, 'portfolio/about.html', context)

class ProjectListView(ListView):
    model = Project
    template_name = 'portfolio/projects.html'
    context_object_name = 'projects'
    paginate_by = 6

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'