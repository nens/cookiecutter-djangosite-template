# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.urls import path

from {{ cookiecutter.package_name }} import views


urlpatterns = [
    path(r'admin/', include(admin.site.urls)),
    # path('something/',
    #     views.some_method,
    #     name="name_it"),
    # path('something_else/',
    #     views.SomeClassBasedView.as_view(),
    #     name='name_it_too'),
]
urlpatterns += staticfiles_urlpatterns()
