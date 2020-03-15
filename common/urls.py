from django.urls import path
from . import views

urlpatterns = [
    
    # Home main routes
    
    path('', views.HomeView.home, name='home'),
    path('dashboard', views.HomeView.dashboard, name='dashboard'),
    path('about', views.HomeView.about, name='about'),
    path('staff', views.HomeView.staff, name='staff'),
    path('teachers_manage', views.HomeView.teachers_manage, name='teachers_manage'),
    path('contact', views.HomeView.contact, name='contact'),
    path('course', views.HomeView.course, name='course'),
    path('ebook', views.HomeView.ebook, name='ebook'),
    path('slinkcourse', views.HomeView.slinkcourse, name='slinkcourse' ),
    path('user_login', views.HomeView.login, name='login'),
    
    # Admin dashboard routes
    
    path('teachers_list', views.AdminView.teachers_list, name='teachers_list'),
    path('teachers_create', views.AdminView.teachers_create, name='teachers_create'),
    path('manage_d', views.AdminView.manage_d, name='manage_d'),
    path('add_teachers', views.AdminView.add_teachers, name='add_teachers'),
    path('delete_teacher/<int:id>', views.AdminView.delete_teacher, name="delete_teacher"),
    path('edit_teacher/<int:id>', views.AdminView.edit_teacher, name="edit_teacher"),
    path('update_teacher', views.AdminView.update_teacher, name = 'update_teacher'),
    path('add_slink', views.AdminView.add_slink, name = 'add_slink'),
    path('slink_create', views.AdminView.slink_create, name = 'slink_create'),
    path('slink_list', views.AdminView.slink_list, name = 'slink_list'),
    path("delete_slink/<int:id>", views.AdminView.delete_slink, name = "delete_slink"),
    
    # Teachers Dashboard routes
    
    path('notice_create', views.TeachersView.notice_create, name='notice_create'),
    path('add_notice', views.TeachersView.add_notice, name="add_notice"),
    path('notice_list', views.TeachersView.notice_list, name='notice_list'),
    path('delete_notice/<int:id>', views.TeachersView.delete_notice, name='delete_notice'),
    path('edit_notice/<int:id>', views.TeachersView.edit_notice, name='edit_notice'),
    path('update_notice', views.TeachersView.update_notice, name='update_notice'),
    path('ebook_list', views.TeachersView.ebook_list, name='ebook_list'),
    path('ebook_create', views.TeachersView.ebook_create, name='ebook_create'),
    path('add_ebook', views.TeachersView.add_ebook, name = 'add_ebook'),
    path('delete_ebook/<int:id>', views.TeachersView.delete_ebook, name='delete_ebook')
    
]