from django.urls import path

from dataentry import views


urlpatterns = [
    path('import-data/', views.import_data, name='import_data'),
    path('export-data/', views.export_data, name='export_data'),
    path('image-compression/compress/', views.compress, name='compress'),
]