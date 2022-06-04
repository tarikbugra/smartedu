from django.shortcuts import get_object_or_404, render
from .models import Course, Category, Tag


# Create your views here.
def course_list(request, category_slug=None, tag_slug=None):
    category_page = None
    tag_page = None

    categories = Category.objects.all()
    tags = Tag.objects.all()
    current_user = request.user

    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        courses = Course.objects.filter(available=True, category=category_page)

    elif tag_slug != None:
        tag_page = get_object_or_404(Tag, slug=tag_slug)
        courses = Course.objects.filter(available=True, tag=tag_page)

    else:
        if current_user.is_authenticated:
            enrolled_courses = current_user.course_person.all()
            courses = Course.objects.all().order_by('-date')
            for course in enrolled_courses:
                courses = courses.exclude(id=course.id)
        else:
            courses = Course.objects.all().order_by('-date')


    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses.html', context)


def course_detail(request, category_slug, course_id):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    courses = Course.objects.all().order_by('-date')
    current_user = request.user
    if current_user.is_authenticated:
        enrolled_courses = current_user.course_person.all()
    else:
        enrolled_courses = courses

    context = {
        'categories': categories,
        'tags': tags,
        'course': course,
        'enrolled_courses': enrolled_courses
    }

    return render(request, 'course.html', context)



def search(request):
    courses = Course.objects.filter(name__contains=request.GET['search'])
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'courses': courses,
        'categories': categories,
        'tags': tags
    }

    return render(request, 'courses.html', context)

