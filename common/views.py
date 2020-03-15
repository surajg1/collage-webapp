from django.shortcuts import render
# from common.models import Admin
from  .models import Teacher
from  .models import Admin
from .models import Slink
from .models import Notice
from .models import Ebook

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

# Create your views here.

class HomeView:
    def home(request):
        notice = Notice.objects.all()
        return render(request,'home/main.html',{
            'notice' : notice
        })
        
    def login(request):
            return render(request,'auth/login.html')

    def dashboard(request):
        return render(request,'dashborad.html')

    def about(request):
        return render(request,'home/About_us.html')

    def staff(request):
        return render(request,'home/Staff.html')

    def contact(request):
        return render(request,'home/contact.html')

    def course(request):
        return render(request,'home/course.html')

    def ebook(request):
        ebooks = Ebook.objects.all()
        return render(request,'student-corner/ebook.html',{
            'ebooks' : ebooks
        })

    def slinkcourse(request):
        slink_list = Slink.objects.all()
        return render(request,'student-corner/s-link-course.html',{
            "slink_list" : slink_list
        })

    def teachers_manage(request):
        return render(request,'teachers_dashboard/dashborad.html')        

# Changes in Admin Dashboard 


class AdminView:
    def teachers_list(request):
        teacher_list = Teacher.objects.all()
        return render(request,'admin_dashboard/teacher_list.html',{
            "teacher_list" : teacher_list
        })

    def teachers_create(request):
        return render(request,'admin_dashboard/teachers_create.html')

    @csrf_exempt
    def add_teachers(request):
        name = request.POST['name']
        email= request.POST['email']
        password= request.POST['password']
        qualification= request.POST['qualification']
        admin_id = Admin.objects.get(id= 1);
        result = Teacher.objects.create(teacher_name = name,teacher_email = email, teacher_password = password, teacher_qualification = qualification, admin = admin_id)
        return HttpResponseRedirect("/teachers_list")    

    def manage_d(request):
        return render(request,'admin_dashboard/admin_dashboard.html')  

    @csrf_exempt
    def delete_teacher(request,id):
        Teacher.objects.get(id= id).delete()
        return HttpResponseRedirect("/teachers_list")    

    def edit_teacher(request, id):
        tach = Teacher.objects.filter(pk = id)
        return render(request,'admin_dashboard/teachers_edit.html',{
            "Teachear" : tach
                }) 
      
    @csrf_exempt  
    def update_teacher(request):
        name = request.POST['name']
        t_id = request.POST['t_id']
        email= request.POST['email']
        password= request.POST['password']
        qualification= request.POST['qualification']
        Teacher.objects.filter(id = t_id).update(teacher_name = name, teacher_email = email, teacher_password = password, teacher_qualification = qualification)
        return HttpResponseRedirect("/teachers_list") 
    
    @csrf_exempt
    def add_slink(request):
        link_name = request.POST['slink_name']
        link = request.POST['link']            
        admin_id = Admin.objects.get(id= 1);
        Slink.objects.create(link_name = link_name,link = link, admin = admin_id)
        return HttpResponseRedirect("slink_list") 
    
    def slink_create(request):
        return render(request,'admin_dashboard/slink_create.html')
    
    def slink_list(request):
        slink_list = Slink.objects.all()
        return render(request,'admin_dashboard/slink_list.html',{
            "slink_list" : slink_list
        })
    
    @csrf_exempt   
    def delete_slink(request, id):
        Slink.objects.get(id= id).delete()
        return HttpResponseRedirect("/slink_list")
    

# Changes in Teacher Dashboard 
    
class TeachersView:
    def notice_create(request):
       return render(request,'teachers_dashboard/notice_create.html')
   
    @csrf_exempt
    def add_notice(request):
        title = request.POST['notice_title']
        link = request.POST['notice_link']
        discription = request.POST['notice_dis']
        teachers_id = Teacher.objects.get(id= 1);
        result = Notice.objects.create(title = title,link = link, discription = discription, teacher = teachers_id)
        return HttpResponseRedirect("/notice_list")


    def notice_list(request):
        notice_list = Notice.objects.all()
        return render(request,'teachers_dashboard/notice_list.html',{
            "notice_list" : notice_list
        })
        
    def delete_notice(request, id):
        Notice.objects.get(id= id).delete()
        return HttpResponseRedirect("/notice_list")

    def edit_notice(request, id):
        noti = Notice.objects.filter(pk = id)
        return render(request,'teachers_dashboard/edit_notice.html',{
            "Notice" : noti
                })
        
    def update_notice(request):
        n_id = request.POST['n_id']
        title = request.POST['title']
        link = request.POST['link']
        discription = request.POST['discription']    
        Notice.objects.filter(id = n_id).update(title = title, link = link, discription = discription)
        return HttpResponseRedirect("/notice_list")
    
    def ebook_list(request):
         ebook_list = Ebook.objects.all()
         return render(request,'teachers_dashboard/ebook_list.html',{
            "ebook_list" : ebook_list
         })
          
    def ebook_create(request):
        return render(request,'teachers_dashboard/ebook_create.html')
    
    @csrf_exempt
    def add_ebook(request):
        name = request.POST['ebook_name']
        link = request.POST['link']
        teachers_id = Teacher.objects.get(id= 1);
        result = Ebook.objects.create(ebook_name = name,link = link, teacher = teachers_id)
        return HttpResponseRedirect("/ebook_list")
    
    def delete_ebook(request, id):
        Ebook.objects.get(id= id).delete()
        return HttpResponseRedirect("/ebook_list")
