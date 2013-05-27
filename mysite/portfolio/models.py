# $Id: $
# Derek Frank (dmfrank@gmx.com)
#
# NAME
#   models.py - portfolio
#
# DESCRIPTION
#   A  portfolio models definition for mysite derekmfrank.com.
#

from django.db import models
from django.contrib import admin


## PORTFOLIO

PROFILE_CHOICES = (
    ('SE', 'StackExchange'),
    ('LI', 'LinkedIn'),
    ('FM', 'Flavors.me'),
    ('BY', 'Beyond'),
    ('FB', 'Facebook'),
    ('PR', 'Profile'),
)


REPO_CHOICES = (
    ('GH', 'GitHub'),
    ('BB', 'BitBucket'),
    ('RE', 'Repo'),
)


LANGUAGE_TYPES = (
    ('scr', 'Scripting'),
    ('prgm', 'Programming'),
)


LANGUAGE_CHOICES = (
    ('c', 'C'),
    ('cpp', 'C++'),
    ('css', 'CSS'),
    ('java', 'Java'),
    ('js', 'Javascript'),
    ('clisp', 'Common Lisp'),
    ('html', 'HTML'),
    ('htmlcss', 'HTML/CSS'),
    ('lua', 'Lua'),
    ('m', 'Matlab'),
    ('oc', 'OCaml'),
    ('oct', 'Octave'),
    ('pl', 'Perl'),
    ('prolog', 'Prolog'),
    ('py', 'Python'),
    ('pydj', 'Python/Django'),
    ('scm', 'Scheme'),
    ('st', 'Smalltalk'),
)


FRAMEWORK_CHOICES = (
    ('dj', 'Django'),
)


DB_CHOICES = (
    ('sql', 'MySQL'),
    ('pgs', 'PostgreSQL'),
    ('pgsp', 'PostgreSQL Psycopg2'),
    ('lite', 'SQLite'),
    ('orac', 'Oracle'),
)


DEPARTMENT_CHOICES = (
    (u'CS', u'Computer Science'),
    (u'CE', u'Computer Engineering'),
    (u'CGD', u'Computer Game Design'),
    (u'EE', u'Electrical Engineering'),
    (u'RE', u'Robotics Engineering'),
    (u'TIM', u'Technology and Information Management'),
    (u'AMS', u'Applied Mathematics and Statistics'),
    (u'Math', u'Mathematics'),
    (u'AM', u'Applied Mathematics'),
    (u'Stat', u'Statistics'),
    (u'Phys', u'Physics'),
    (u'Econ', u'Economics'),
    (u'Psyc', u'Psychology'),
    (u'Musc', u'Music'),
    (u'Lit', u'Literature'),
    (u'Writ', u'Writing'),
    (u'Stev', u'Stevenson'),
    (u'MC', u'Miscellaneous'),
)


# Source
class Source(models.Model):
    priority = models.IntegerField()
    title = models.CharField(max_length=127)
    repository_name = models.CharField(max_length=4, choices=REPO_CHOICES, blank=True, null=True)
    profile_name = models.CharField(max_length=4, choices=PROFILE_CHOICES, blank=True, null=True)
    url = models.URLField(verify_exists=True)

    def __unicode__(self):
        return self.title


# Language Choice
class LanguageChoice(models.Model):
    language = models.CharField(max_length=8, blank=True, null=True, choices=LANGUAGE_CHOICES)
    type = models.CharField(max_length=4, blank=True, null=True, choices=LANGUAGE_TYPES)
    language_version = models.CharField(max_length=16, blank=True, null=True)
    framework = models.CharField(max_length=8, blank=True, null=True, choices=FRAMEWORK_CHOICES)
    framework_version = models.CharField(max_length=16, blank=True, null=True)
    database = models.CharField(max_length=4, blank=True, null=True, choices=DB_CHOICES)
    database_version = models.CharField(max_length=16, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        if self.framework:
            if self.database:
                return self.get_language_display() + self.language_version + '/' + self.get_framework_display() + self.framework_version + '/' + self.get_database_display() + self.database_version
            return self.get_language_display() + self.language_version + '/' + self.get_framework_display() + self.framework_version
        return self.get_language_display() + self.language_version


# Project
class Project(models.Model):
    title = models.CharField(max_length=127)
    description = models.TextField()
    date = models.DateField()
    url = models.URLField(blank=True, null=True, verify_exists=True)
    language = models.ManyToManyField(LanguageChoice, blank=True, null=True)
    repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES)

    def __unicode__(self):
        return self.title


# Education
class Education(models.Model):
    name = models.CharField(null=True, max_length=127)
    acronym = models.CharField(blank=True, null=True, max_length=8)
    DEGREE_CHOICES = (
        (u'BS', u'Bachelor of Science'),
        (u'BA', u'Bachelor of Arts'),
        (u'MS', u'Master of Science'),
        (u'MA', u'Master of Arts'),
        (u'HD', u'High School Diploma'),
        (u'GED', u'G.E.D.'),
    )
    degree = models.CharField(max_length=3, choices=DEGREE_CHOICES)
    major = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    minor = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    graduation_date = models.DateField()
    coursework_repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    coursework_repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES) 

    def __unicode__(self):
        return self.acronym or self.name


# Course
class Course(models.Model):
    education_institution = models.ForeignKey(Education)
    department = models.CharField(max_length=4, choices=DEPARTMENT_CHOICES, default=u'MC')
    name = models.CharField(max_length=127)
    number = models.CharField(max_length=8, null=True)
    lab_letter = models.CharField(max_length=4, blank=True, null=True)
    course_url = models.URLField(blank=True, null=True, verify_exists=True)
    lab_url = models.URLField(blank=True, null=True, verify_exists=True)
    repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES)
    description = models.TextField()

    def __unicode__(self):
        if self.lab_letter:
            return  self.name + ' (' + self.department + ' ' + self.number + '/' + self.lab_letter + ')' 
        return  self.name + ' (' + self.department + ' ' + self.number + ')' 


# Assignment
class Assignment(models.Model):
    course = models.ForeignKey(Course)
    name = models.CharField(max_length=127)
    identification = models.CharField(max_length=16)
    programming_language = models.CharField(max_length=8, blank=True, null=True, choices=LANGUAGE_CHOICES)
    assignment_url = models.URLField(blank=True, null=True, verify_exists=True)
    repository_url = models.URLField(blank=True, null=True, verify_exists=True)
    repository_name = models.CharField(blank=True, null=True, max_length=2, choices=REPO_CHOICES)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        if self.course.lab_letter:
            return self.course.department + self.course.number + '/' + self.course.lab_letter + ' - ' + self.identification + ' - ' +  self.name
        return self.course.department + self.course.number + ' - ' + self.identification + ' - ' +  self.name


## PORTFOLIO ADMIN

class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'repository_name', 'profile_name')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'repository_name', 'date')

class LanguageChoiceAdmin(admin.ModelAdmin):
    list_display = ('language', 'language_version', 'type', 'framework', 'framework_version', 'database', 'database_version')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('name', 'acronym', 'degree', 'major', 'graduation_date')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'number', 'lab_letter', 'education_institution')

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'identification', 'programming_language', 'course')

## REGISTER
admin.site.register(Source, SourceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(LanguageChoice, LanguageChoiceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)
