from django.shortcuts import render
from .models import CourseReview


def course_reviews(request):
    """ View to return course reviews page """
    reviews = CourseReview.objects.all()

    template = 'course_reviews/course_reviews.html'

    context = {
        'reviews': reviews,
    }

    return render(request, template, context)
