from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter()

router.register('list', views.InstructorView)
#router.register('course/list', views.CourseView)


urlpatterns = [
    path('', include(router.urls)),
    # path('create/', views.CourseCreateView.as_view(), name='create'),
    # path('<int:pk>/update/', views.CourseUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', views.CourseDestroyView.as_view(), name='delete'),
]

