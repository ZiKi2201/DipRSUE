from django.contrib import admin
from .models import Reviews
from .models import Applications

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name_org', 'name', 'position', 'date', 'publication')
    search_fields = ('name', 'name_org', 'date')

class AppAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile')
    search_fields = ('name', 'email', 'mobile')


admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Applications, AppAdmin)

admin.site.site_title = 'Админ-панель сайта ИП.Семёнова'
admin.site.site_header = 'Админ-панель сайта ИП.Семёнова'
