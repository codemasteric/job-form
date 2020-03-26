from django.contrib import admin
from .models import Job, Application
import csv
from django.http import HttpResponse

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')
        
        writer = csv.writer(response)
        if header:
            writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','gender','age','position','email_address','phone')
    list_filter = ['position','gender']
    search_fields = ['first_name', 'last_name','position','experience','training','publication']

    actions = [export_as_csv_action("Export selected objects as CSV file", fields=['first_name', 'last_name','gender','age','position','email_address','phone'], header=True),]

admin.site.register(Application,ApplicationAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'vacancy','job_deadline_date','details_link')
admin.site.register(Job,JobAdmin)


# admin.site.register(Job)
# admin.site.register(Application)
