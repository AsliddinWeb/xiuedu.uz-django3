from django.shortcuts import render, get_object_or_404
from .models import Faculty, FacultyBreadcrumb, Division, DivisionBreadcrumb, Department, Staff, DepartmentBreadcrumb


def faculty_list(request):
    breadcrumb = FacultyBreadcrumb.get_active()
    faculties = Faculty.objects.filter(is_active=True).order_by('order')

    context = {
        'page_title': 'Fakultetlar',
        'breadcrumb': breadcrumb,
        'faculties': faculties,
    }
    return render(request, 'faculties/faculty_list.html', context)


def division_list(request):
    breadcrumb = DivisionBreadcrumb.get_active()
    divisions = Division.objects.filter(is_active=True).order_by('order')

    context = {
        'page_title': "Bo'limlar",
        'breadcrumb': breadcrumb,
        'divisions': divisions,
    }
    return render(request, 'faculties/division_list.html', context)


def faculty_detail(request, slug):
    faculty = get_object_or_404(Faculty, slug=slug, is_active=True)
    departments = Department.objects.filter(
        faculty=faculty, is_active=True
    ).order_by('order')

    # --- YANGI ---
    breadcrumb = FacultyBreadcrumb.get_active()

    context = {
        'page_title': faculty.name,
        'faculty': faculty,
        'departments': departments,
        'breadcrumb': breadcrumb,  # --- YANGI ---
    }
    return render(request, 'faculties/faculty_detail.html', context)


def department_detail(request, slug):
    department = get_object_or_404(Department, slug=slug, is_active=True)
    faculty = department.faculty
    staff_members = Staff.objects.filter(department=department, is_active=True).order_by('order')
    breadcrumb = DepartmentBreadcrumb.get_active()  # YANGI

    context = {
        'page_title': department.name,
        'department': department,
        'faculty': faculty,
        'staff_members': staff_members,
        'breadcrumb': breadcrumb,  # YANGI
    }
    return render(request, 'faculties/department_detail.html', context)