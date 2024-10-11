from django.shortcuts import render
from .models import GraduateProgram
from django.db.models import Q

def program_list(request):
    language = request.GET.get('language')
    search_query = request.GET.get('search')
    
    programs = GraduateProgram.objects.all()

    # Filter by language if provided
    if language:
        programs = programs.filter(language=language)

    # Search query filtering
    if search_query:
        programs = programs.filter(
            Q(graduate_program__icontains=search_query) |
            Q(university__icontains=search_query)
        )

    return render(request, 'programs/program_list.html', {'programs': programs})

def program_detail(request, pk):
    program = GraduateProgram.objects.get(id=pk)

    # Extracting qualifications from JSONField
    qualifications = program.qualifications if program.qualifications else {}
    degree = qualifications.get('degree', 'Not specified')
    gpa = qualifications.get('GPA', 'Not specified')
    additional_requirements = qualifications.get('additional_requirements', [])

    return render(request, 'programs/program_detail.html', {
        'program': program,
        'degree': degree,
        'gpa': gpa,
        'additional_requirements': additional_requirements,
    })
