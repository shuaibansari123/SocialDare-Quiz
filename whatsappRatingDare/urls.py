from django.contrib import admin
from django.urls import path , include
#from .views import send_user_first_page , ajax1_url_2_new_view , ajax_1 , ajax_2 , ajax_3 , ajax_4 , ajax_5 , ajax_6 , ajax_7 , ajax_8 , ajax_9 , ajax_10 , ajax_11 , ajax_new_user_view
from .views import *

urlpatterns = [
    path('<str:pk>/dare/<int:id_for_obj>/' , send_user_first_page , name="send-user-first-page") , 
    path('answer-ajax-1/ninja-technique' , ajax_1 , name='ajax1_url_1'),
    path('answer-ajax-2/ninja-technique' , ajax_2 , name='ajax1_url_2'),
    path('answer-ajax-3/ninja-technique' , ajax_3 , name='ajax1_url_3'),
    path('answer-ajax-4/ninja-technique' , ajax_4 , name='ajax1_url_4'),
    path('answer-ajax-5/ninja-technique' , ajax_5 , name='ajax1_url_5'),
    path('answer-ajax-6/ninja-technique' , ajax_6 , name='ajax1_url_6'),
    path('answer-ajax-7/ninja-technique' , ajax_7 , name='ajax1_url_7'),
    path('answer-ajax-8/ninja-technique' , ajax_8 , name='ajax1_url_8'),
    path('answer-ajax-9/ninja-technique' , ajax_9 , name='ajax1_url_9'),
    path('answer-ajax-10/ninja-technique' , ajax_10 , name='ajax1_url_10'),
    #path('answer-ajax-11/ninja-technique' , ajax_11 , name='ajax1_url_11'),
    
    
    path('ajax_new_user/create/select/choice' , ajax_new_user_view , name="ajax_new_user_url" ), 
    # it firts below
    path('ajax_1_new_user' , ajax1_url_2_new_view ,    name="ajax1_url_2_new"),
    #2nd aanswer
    #path('ajax1_url_2_new_view_1' , ajax1_url_2_new_view_1 ,    name="ajax1_url_2_new_1"),
    
    path('ajax_2_new_user' , ajax1_url_3_new_view ,    name="ajax1_url_3_new"),
    path('ajax_3_new_user' , ajax1_url_4_new_view ,    name="ajax1_url_4_new"),
    path('ajax_5_new_user' , ajax1_url_5_new_view ,    name="ajax1_url_5_new"),
    path('ajax_6_new_user' , ajax1_url_6_new_view ,    name="ajax1_url_6_new"),
    path('ajax_7_new_user' , ajax1_url_7_new_view ,    name="ajax1_url_7_new"),
    path('ajax_8_new_user' , ajax1_url_8_new_view ,    name="ajax1_url_8_new"),
    path('ajax_9_new_user' , ajax1_url_9_new_view ,    name="ajax1_url_9_new"),
    path('ajax_10_new_user' , ajax1_url_10_new_view ,    name="ajax1_url_10_new"),
    path('final' , ajax1_url_final_view ,    name="ajax1_url_final"),
    
    path('mytest' , testview ,    name="test-view"),
    
]
