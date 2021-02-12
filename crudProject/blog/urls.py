from django.urls import path
from . import views

urlpatterns = [
    path("blog_list/",views.blog_list,name="view1"),
    path("create/",views.create,name="view2"),
    path('delete/<int:pk>',views.blog_delete,name="view3"),
    path("home",views.test,name="homepage"),
    path("logout",views.logout,name="logout"),
    path("aboutUs",views.aboutUs,name="about"),
    path("test",views.test,name="test")

]
