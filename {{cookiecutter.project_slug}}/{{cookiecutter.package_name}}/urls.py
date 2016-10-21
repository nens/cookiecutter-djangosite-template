# (c) Nelen & Schuurmans.  Proprietary, see LICENSE file.
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from {{ cookiecutter.package_name }} import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^something/',
    #     views.some_method,
    #     name="name_it"),
    # url(r'^something_else/$',
    #     views.SomeClassBasedView.as_view(),
    #     name='name_it_too'),
]
urlpatterns += staticfiles_urlpatterns()
