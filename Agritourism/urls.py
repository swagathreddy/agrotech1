from django.urls import path
from django.conf import settings
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('farmer/', views.farmer_view, name='farmer'),
    path('register/', views.register_farmer, name='register_farmer'),
    path('login/', views.login, name='login'),  # URL mapping for login page
    path('logout/', LogoutView.as_view(), name='logout'),
    path('lendafarm/', views.lend_a_farm, name='lend_a_farm'),
    path('centres/', views.centres, name='centres'),
     path('blog/', views.blog_view, name='blog'),
     path('writeblog/', views.write_blog_view, name='write_blog'),
     path('courses/', views.courses_view, name='courses'),
     path('products/', views.products_view, name='products'),
      path('community/', views.community, name='community'),
      path("translate/", views.translate_text, name="translate_text"),
        path('resource/', views.resource, name='resource'),
    path('add_question/', views.add_question, name='add_question'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('add_answer/<int:question_id>/', views.add_answer, name='add_answer'),
    path('fetch_answers/<int:question_id>/', views.fetch_answers, name='fetch_answers'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from Agritourism import views




