from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api import views as UserViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)



router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    ########## Registration & Token ##############################
    path('register/', UserViews.RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ########## VIEWS (Router based) ##########
    path('', include(router.urls)),
    ########## VIEWS (Function based) ##########
    path("students/", views.studentsViews),
    path("students/<int:pk>/", views.studentDetailViews),
     ########## VIEWS (Class based) ##########
    path('blogs/', views.BlogsView.as_view()),          
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/', views.CommentsView.as_view()),  
    path('comments/<int:pk>/', views.CommentDetailView.as_view()), 

]