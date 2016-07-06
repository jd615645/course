from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_protect 
from django.template import RequestContext #this import is for csrf-token
from django.core.context_processors import csrf
from apps.course.models import Course_of_user, Course
from django.utils import timezone # auto generate create time.
import json
from django.contrib.auth.decorators import login_required 
# Create your views here.
def course(request):
    return render_to_response('course/course.html',locals())

@login_required
def course_zh_TW(request):
    userDept_from_request = request.user.major
    userGrade_from_request = request.user.grade
    userDegree_from_request = request.user.m_career
    email = request.user.email
    CourseUser, created = Course_of_user.objects.get_or_create(user_name=request.user.email,defaults={
            'hadSaved':False,
            'user_dept':userGrade_from_request,
            'create':timezone.localtime(timezone.now())
        }
    )
    ##########################################
    #  hadSaved可以知道使用者是不是已經存過課程了 #
    ##########################################
    hadSaved_from_request = CourseUser.hadSaved
    if request.POST:
        data = request.POST #all element of QuerySet is type of list, i dont know why but turn it into diction can disassembler its list into its origin type.
        data=data.dict()# turn Querydict into python's dict
        idList=json.loads(data['idList'])
        save_idList_for_user(idList,data,CourseUser)
        return render_to_response('course/course_zh_TW.html',locals())
    elif 'name' in request.GET and request.GET['name']!='':
        # CourseUser = Course_of_user.objects.get(user_name=request.GET['name'])    
        user_name = CourseUser.user_name
        user_dept = CourseUser.user_dept
        returnarr = CourseUser.returnarr
        time_table = CourseUser.time_table
        booklist = CourseUser.idList.all()
        return render_to_response('course/course_zh_TW.html',locals())
    else:    
        test=[12,23,45,6]
        return render_to_response('course/course_zh_TW.html',RequestContext(request,locals()))
def course_en_US(request):
    return render_to_response('course_en_US.html',locals())

def book_of_course(request):
    if request.POST:
        data = request.POST #all element of QuerySet is type of list, i dont know why but turn it into diction can disassembler its list into its origin type.
        data=data.dict()# turn Querydict into python's dict
        ####Build default dict, if find data already exitst, than update the info. #####
        default = {}
        default['courseID'] = data['courseID']
        default['book'] = data['book']
        default['name'] = data['name']
        default['create'] = timezone.localtime(timezone.now())
        obj, created = Course.objects.update_or_create(courseID = data['courseID'], defaults=default)
        # update_or_create will update exist data or create a new one if not.
        return render_to_response('course/course_zh_TW.html',RequestContext(request,locals()))
def save_idList_for_user(idList,data,CourseUser):
    #Build default dict, if find data already exitst, than update the info.
    default = {   
        'time_table':data['time_table'],
        'returnarr':data['returnarr'],
        'hadSaved':True,
        'create':timezone.localtime(timezone.now())
    }
    # u, created = Course_of_user.objects.update_or_create(user_name = data['user_name'], defaults=default)
    # update_or_create will update exist data or create a new one if not.
    Course_of_user.objects.filter(pk=CourseUser.pk).update(**default)
    CourseUser.idList.clear()#Remove all ManytoMany Relation.
    for i in idList.keys():
        c, created = Course.objects.update_or_create(courseID=i,defaults={'courseID': i,'name':idList[i],'create':timezone.localtime(timezone.now())})
        CourseUser.idList.add(c)#obj is an instance of Model Course! Course_of_User has a manyToMany key of Course

def supply_book_info(request):
    return render_to_response('course/supply_book_info.html',RequestContext(request,locals()))