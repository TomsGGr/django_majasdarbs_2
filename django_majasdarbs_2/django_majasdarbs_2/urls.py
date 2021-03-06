"""django_majasdarbs_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import uzdevumi.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('add-user', uzdevumi.views.md3_skats_db_forma),
    path('', uzdevumi.views.md3_skats_db_saraksts),
    path('user/<int:user_id>', uzdevumi.views.md4_skats_viens_juzeris, name='viens_juzeris'),

    path('add-user-vecais', uzdevumi.views.django_md2_skats_1),
    path('user-list-vecais', uzdevumi.views.django_md2_skats_saraksts),
    path('user-list-vecais-2', uzdevumi.views.django_md_skats_saraksts_b),

    path('add-file', uzdevumi.views.upload_csv_to_db),

]
