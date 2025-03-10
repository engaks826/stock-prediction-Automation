from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from accounts import views as UserViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)


router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('register/', UserViews.RegisterView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   

    ########## function based views ##########
    path("students/", views.studentsViews),
    path("students/<int:pk>/", views.studentDetailViews),

    ########## Router Views ##########
    path('', include(router.urls)),

    ########## Class based Views ##########
    ## option 1 or 2 or 3 or 4 from serializer.py ## <https://f8a3-102-41-55-235.ngrok-free.app/api/v1/{}/>
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetail.as_view()),
    path('blogs/', views.BlogsView.as_view()),          
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/', views.CommentsView.as_view()),  
    path('comments/<int:pk>/', views.CommentDetailView.as_view()), 

]