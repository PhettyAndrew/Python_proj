from django.urls import path
from . import views

app_name='app1'
urlpatterns=[
    path('',views.MemberListView.as_view(),name='index'),
    path('add-member',views.MemberCreateView.as_view(),name='add-member'),
    path('<int:pk>/update',views.MemberUpadateView.as_view(),name='update-member'),
    path('<int:pk>/delete',views.MemberDeleteView.as_view(),name='delete-member'),
]