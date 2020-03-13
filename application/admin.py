from django.contrib import admin

from .models import Job, Application

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','gender','age','position','email_address','phone')
    list_filter = ['position', 'age','gender','first_name']
    search_fields = ['first_name', 'last_name','position','experience','training','publication']

admin.site.register(Application,ApplicationAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'vacancy','job_deadline_date','details_link')
admin.site.register(Job,JobAdmin)


# admin.site.register(Job)
# admin.site.register(Application)
