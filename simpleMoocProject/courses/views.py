from django.shortcuts import render, get_object_or_404
from .models import Course
from .forms import ContactCourse


# view para a lista de cursos.
def index(request):
    courses = Course.objects.all()
    template_name = 'courses/index.html'
    context = {
        'courses': courses
    }
    return render(request, template_name, context)


# View para a página detalhada de um curso
def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {}
    if request.method == 'POST':
        form = ContactCourse(request.POST)
        if form.is_valid():
            context['is_valid()'] = True
            form.send_mail(course)
            form = ContactCourse()
    else:
        form = ContactCourse()
    context['form'] = form,
    context['course'] = course
    template_name = 'courses/details.html'
    return render(request, template_name, context)
