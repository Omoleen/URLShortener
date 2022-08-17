from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', shortener, name='shortener-page'),
    path('<str:code>/', shortener, name='shortener-redirect'),
    # path('/<str:code>/', shortener, name='shortener-redirect'),
    path("result/htmx/", shortenerhtmx, name='shortener-htmx')
    # path('<int:pk>/', project, name='project_page')
]

# body { height: 100%;
# }
# .parent {
#     height: 200px;
# background: #CCCCCC;
# display: flex;
# align-items: center;
# justify-content: center;
# }