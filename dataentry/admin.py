from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Customer, Employee, Blog, Comment, Upload, CompressImage


admin.site.register(Student)
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Blog)
admin.site.register(Comment)

class UploadAdmin(admin.ModelAdmin):
    list_display = ['model_name', 'uploaded_at']

admin.site.register(Upload, UploadAdmin)


class CompressImageAdmin(admin.ModelAdmin):
    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.compressed_img.url}" width="40" height="40">')

    def org_img_size(self, obj):
        return format_html(f'{obj.original_img.size / (1024*1024):.2f} MB')

    def comp_img_size(self, obj):
        size_in_mb = obj.compressed_img.size / (1024*1024)
        if size_in_mb > 1:
            return format_html(f'{size_in_mb:.2f} MB')
        else:
            size_in_kb = obj.compressed_img.size/1024
            return format_html(f'{size_in_kb:.2f} KB')

    list_display = ('user', 'thumbnail', 'org_img_size', 'comp_img_size', 'compressed_at')
    
admin.site.register(CompressImage, CompressImageAdmin)