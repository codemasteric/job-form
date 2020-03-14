from django.contrib import admin
from .models import Job, Application
import csv
from django.http import StreamingHttpResponse

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def some_streaming_csv_view(request, queryset):
    """A view that streams a large CSV file."""
    # Generate a sequence of rows. The range is based on the maximum number of
    # rows that can be handled by a single sheet in most spreadsheet
    # applications.
    # selected = queryset.values_list('first_name', flat=True)
    rows = ([str(idx)] for idx in queryset.values())
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="applications.csv"'
    return response

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','gender','age','position','email_address','phone')
    list_filter = ['position','gender']
    search_fields = ['first_name', 'last_name','position','experience','training','publication']

    actions = ['make_published']

    def make_published(self, request, queryset):
        response = some_streaming_csv_view(request,queryset)
        return response
    make_published.short_description = "Export to a csv File"

admin.site.register(Application,ApplicationAdmin)

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'vacancy','job_deadline_date','details_link')
admin.site.register(Job,JobAdmin)


# admin.site.register(Job)
# admin.site.register(Application)
