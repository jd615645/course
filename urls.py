from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import patterns, url
import apps.course

urlpatterns = patterns('apps.course.views',
    url(r'^course_zh_TW/$','course_zh_TW',name="course_zh_TW"),
	url(r'^book_of_course/$','book_of_course'),
	url(r'^supply_book_info/$','supply_book_info'),
	

	# url(r'^data/course/$', 'data_source_dispatcher')
	

)