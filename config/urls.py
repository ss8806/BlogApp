from django.contrib import admin
from django.urls import path, include   #includeを追加

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('management/', admin.site.urls),  #URI 変更
    path('blog/', include('blog.urls')),  #追加
]
