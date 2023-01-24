from django.urls import path
from . import views

app_name = 'todoapp'
urlpatterns = [

    path('', views.index, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cvhome/', views.Tasklistview.as_view(), name='cvhome'),
    path('cvdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cvdetail'),
    path('cvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cvupdate'),
    path('cvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cvdelete'),

]
