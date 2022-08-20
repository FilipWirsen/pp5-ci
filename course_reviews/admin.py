from django.contrib import admin
from .models import CourseReview


@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug': ('name',)}
