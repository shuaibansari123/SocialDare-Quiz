import re
from django.shortcuts import redirect, render
from .models import personOwnChart , answerModel
from django.http import HttpResponseRedirect


def send_user_first_page(request , pk , id_for_obj): 
    param={}
    obj = personOwnChart.objects.prefetch_related('answersChart').get(id=id_for_obj)
    if request.method =='GET':      
        param['id_of_url' ]= id_for_obj
        param['name_of_url' ]= pk
        request.session['id_of_url']=id_for_obj
        try:
            if request.session['url_pkk']:
                del request.session['url_pkk']
                request.session['url_pkk']=pk
        except:
            request.session['url_pkk']=pk
        print()
        request.session['url_obj']=id_for_obj
    all_answer_people = obj.answersChart.all()
    param["all_answer_people"]  = all_answer_people
    return render(request , 'advance-element/AdvanceUI-about.html' ,param)

def ajax_new_user_view(request):
    if request.method =='GET':
        param={}
        my_dare_person_name = str(request.GET.get('answer_name' , 'Stranger')).replace(' ' , '-')
        new_obj = personOwnChart.objects.create(name=my_dare_person_name)
        request.session['id_the_new'] = int(new_obj.id) 
        param['has_url_share']  = True 
        request.session['my_url'] =  f"http://127.0.0.1:8000/{new_obj.name}/dare/{new_obj.id}/"
        return render(request , 'new_user_ajax.html' , param )
        


# oser_own_informatoion giving us_________________________________________________:)
# ans1
def ajax1_url_2_new_view(request):
    if request.method == 'GET':
        answer_1 = int(request.GET.get('answer1' , 0 ))
        if answer_1 != 0 :
           request.session['owner_user_answer_1'] = answer_1
        return render(request , 'new_user_ajax_2.html' )

def ajax1_url_3_new_view(request):
    if request.method == 'GET':
        answer_2 = int(request.GET.get('answer2' , 0 ))
        if answer_2 != 0 :
           request.session['owner_user_answer_2'] = answer_2
        return render(request , 'new_user_ajax_3.html' )
    
def ajax1_url_4_new_view(request):
    if request.method == 'GET':
        answer_3 = int(request.GET.get('answer3' , 0 ))
        if answer_3 != 0 :
           request.session['owner_user_answer_3'] = answer_3
        return render(request , 'new_user_ajax_4.html' )
    

def ajax1_url_5_new_view(request):
    if request.method == 'GET':
        answer_4 = int(request.GET.get('answer4' , 0 ))
        if answer_4 != 0 :
           request.session['owner_user_answer_4'] = answer_4
        return render(request , 'new_user_ajax_5.html' )

def ajax1_url_6_new_view(request):
    if request.method == 'GET':
        answer_5 = int(request.GET.get('answer5' , 0 ))
        if answer_5 != 0 :
           request.session['owner_user_answer_5'] = answer_5
        return render(request , 'new_user_ajax_6.html' )

def ajax1_url_7_new_view(request):
    if request.method == 'GET':
        answer_6 = int(request.GET.get('answer6' , 0 ))
        if answer_6 != 0 :
           request.session['owner_user_answer_6'] = answer_6
        return render(request , 'new_user_ajax_7.html' )

def ajax1_url_8_new_view(request):
    if request.method == 'GET':
        answer_7 = int(request.GET.get('answer7' , 0 ))
        if answer_7 != 0 :
           request.session['owner_user_answer_7'] = answer_7
        return render(request , 'new_user_ajax_8.html' )

def ajax1_url_9_new_view(request):
    if request.method == 'GET':
        answer_8 = int(request.GET.get('answer8' , 0 ))
        if answer_8 != 0 :
           request.session['owner_user_answer_8'] = answer_8
        return render(request , 'new_user_ajax_9.html' )

def ajax1_url_10_new_view(request):
    if request.method == 'GET':
        answer_9 = int(request.GET.get('answer9' , 0 ))
        if answer_9 != 0 :
           request.session['owner_user_answer_9']= answer_9
        return render(request , 'new_user_ajax_10.html' )

def ajax1_url_final_view(request):
    if request.method == 'GET':
        answer_10 = int(request.GET.get('answer10' , 0 ))
        if answer_10 != 0 :
            request.session['owner_user_answer_10'] = answer_10
        
        #for saving questions like q1,q2,q3...q10 field using session data 
        person_obj = personOwnChart.objects.get( id = int(request.session['id_the_new']))
        person_obj.q1 = int(request.session['owner_user_answer_1'])
        person_obj.q2 = int(request.session['owner_user_answer_2'])
        person_obj.q3 = int(request.session['owner_user_answer_3'])
        person_obj.q4 = int(request.session['owner_user_answer_4'])
        person_obj.q5 = int(request.session['owner_user_answer_5'])
        person_obj.q6 = int(request.session['owner_user_answer_6'])
        person_obj.q7 = int(request.session['owner_user_answer_7'])
        person_obj.q8 = int(request.session['owner_user_answer_8'])
        person_obj.q9 = int(request.session['owner_user_answer_9'])
        person_obj.q10 = int(request.session['owner_user_answer_10'])
        person_obj.save()
        
        for i in range(1,11):
            
            del request.session[f'owner_user_answer_{i}']
            
        print('deleted-new-ajax-10-quesion-from-session')
        return render(request , 'new_user_ajax_final.html' )








 

def ajax_1(request):
    if request.method == 'GET':
       
        answer_name = str(request.GET.get('answer_name' , 'NotFound'))
        answer_1 = int(request.GET.get('answer1' , 0))
        ids = request.GET.get('hidden_pk' , 'NotFound')
        obj = personOwnChart.objects.prefetch_related('answersChart').get(id=int(ids))
        if  answer_1 != 0:
            
            name_answer_person = answer_name
            answer_obj = answerModel.objects.create(name = name_answer_person )
            obj.answersChart.add(answer_obj)
            obj.save()
            
            request.session['answer1'] = answer_1
            request.session['my_real_id'] = obj.id
            request.session['child_real_id'] = answer_obj.id
        
        return render(request , 'ajax1.html' )

def ajax_2(request):
    if request.method == 'GET':
        answer_2 = int(request.GET.get('answer2' , 0))
        if answer_2 != 0 :
            request.session["answer2" ] = answer_2
        return render(request , 'ajax2.html' )

def ajax_3(request):
    if request.method == 'GET':
        answer_3 = int(request.GET.get('answer3' , 0))
        if answer_3 != 0:
            request.session["answer3" ] = answer_3         
        return render(request , 'ajax3.html' )
    
def ajax_4(request):
    if request.method == 'GET':
        answer_4 = int(request.GET.get('answer4' , 0))
        if answer_4 != 0:
            request.session["answer4" ] = answer_4  
        return render(request , 'ajax4.html' )
    
def ajax_5(request):
    if request.method == 'GET':
        answer_5 = int(request.GET.get('answer5' , 0 ))
        if answer_5  != 0 :
            request.session["answer5" ] = answer_5    
        return render(request , 'ajax5.html' )  
    
def ajax_6(request):
    if request.method == 'GET':
        answer_6 = int(request.GET.get('answer6' , 0 ))
        if answer_6 != 0 :
            request.session["answer6" ] = answer_6
        return render(request , 'ajax6.html' )
    
def ajax_7(request):
    if request.method == 'GET':
        answer_7 = int(request.GET.get('answer7' , 0 ))
        if answer_7 != 0 :
            request.session["answer7" ] = answer_7  
        return render(request , 'ajax7.html' )
    
def ajax_8(request):
    if request.method == 'GET':
        answer_8 = int(request.GET.get('answer8' , 0 ))
        if answer_8 !=  0 :
            request.session["answer8" ] = answer_8
        return render(request , 'ajax8.html' )
    
def ajax_9(request):
    if request.method == 'GET':
        answer_9 = int(request.GET.get('answer9' , 0 ))
        if answer_9 != 0 :
            request.session["answer9" ] = answer_9
        return render(request , 'ajax9.html' )
    
import random  
def ajax_10(request):
    
            
    if request.method == 'GET':
        answer_10 = int(request.GET.get('answer10' , 0 ))
        if answer_10 != 0 :
            request.session["answer10" ] = answer_10
        
        print(request.session["answer1" ] , request.session["answer2" ] , request.session["answer3" ] , 
                  request.session["answer4" ] , request.session["answer5" ] , request.session["answer6" ] ,  
                  request.session["answer7" ] , request.session["answer8" ] , request.session["answer9" ] ,
                  request.session["answer10" ]
                  )
        total_rate = 0 
           
        parent_user_id = int(request.session.get('my_real_id' ))
        child_user_id = int(request.session.get('child_real_id'))
        parent = personOwnChart.objects.prefetch_related('answersChart').get(id = parent_user_id)
        child = parent.answersChart.get(id = child_user_id )
       
         #_________:)()
        # rate some think based on session['answer1....10'] and person real question
        try:
        
            if int(request.session.get('answer1')) == int(parent.q1):
                
                total_rate +=10
            if int(request.session.get('answer2')) == int(parent.q2):
                total_rate +=10
            if int(request.session.get('answer3')) == int(parent.q3):
                total_rate +=10
            if int(request.session.get('answer4')) == int(parent.q4):
                total_rate +=10
            if int(request.session.get('answer5')) == int(parent.q5):
                total_rate +=10
            if int(request.session.get('answer6')) == int(parent.q6):
                total_rate +=10
            if int(request.session.get('answer7')) == int(parent.q7):
                total_rate +=10
            if int(request.session.get('answer8')) == int(parent.q8):
                total_rate +=10
            if int(request.session.get('answer9')) == int(parent.q9):
                total_rate +=10
            if int(request.session.get('answer10')) == int(parent.q10):
                total_rate +=10
                
            child.answer = total_rate 
            child.save()
            
        except  Exception as e:
            child.answer = total_rate 
            child.save()
            
            
        for i in range(1,11):
            del request.session[f'answer{i}']
        del request.session['child_real_id']
        del request.session['my_real_id']
        print('deleted-all-session-data')
        param={'your_score' : total_rate  , 'your_name': child.name}
        return render(request , 'ajax10.html' , param )
    
    
    
    
def testview(request):
    
    return render(request , 'gafla-inspenct.html')