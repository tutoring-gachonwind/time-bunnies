
from django.contrib import admin
from django.urls import path, include
from pybo import views as pybo_views  # pybo 앱의 views 모듈을 import
from common import views as common_views  # common 앱의 views 모듈을 import
from pybo.views import base_views

urlpatterns = [
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('signup/', common_views.signup, name='signup'),  # common 앱의 signup 뷰를 사용
]
