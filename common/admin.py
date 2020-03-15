from django.contrib import admin

# Register your models here.
from  .models import Admin
from  .models import Teacher
from .models import Slink
from .models import Notice
from .models import Ebook

admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Slink)
admin.site.register(Notice)
admin.site.register(Ebook)

