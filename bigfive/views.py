from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from accounts.models import User
from accounts.forms import UserCreationForm
from .models import Test, Score, Adjective

# Create your views here.
# 1. main
def index(request) :
    return render(request, 'bigfive/main.html')

# 2. 유저 정보 받기(getuser.html)) - account.create


# 3. 설문 고르기(selecttest.html)
def select(request) :
    return render(request, 'bigfive/select.html')

# query set > list
def makefor(q) :
    q_list = []
    for i in q :
        print(i)
        q_list.append(i)
    return q_list


# 4. 각 설문에 해당하는 질문 넘기기
def gettest(request, test_num) :
    print(test_num, type(test_num))

    # db test에 OCEAN을 저장해놓고 불러와서 score랑 매칭
    # 1) TEST 모두 저장 
    # 2) pk별로 저장 될 model(test_pk, score, user_pk)

    # 12문항
    if test_num == 12 :
        tests = Test.objects.filter(testname=12)
        print(tests)
        testlists = makefor(tests)
    # 50, 100개 랜덤으로 뽑기 문항
    elif test_num == 50 or test_num == 100 :
        testlists = []
    # 120, 300개 랜덤으로 뽑기 문항
    elif test_num == 120 or test_num == 300 :
        testlists = []

    
    context = {'test_lists' : testlists}
    return render(request, 'bigfive/test.html', context)

# 4. 각 설문 문항 저장
def savescore(request, test_pk, score_grade, user_pk) :
    # 저장 True/False 결과만 보내주면 됨.
    # 즉, serializers.data
    if request.is_ajax() :
        test = get_object_or_404(Test, pk=test_pk)
        user = get_object_or_404(User, pk=user_pk)
        if len(Score.objects.filter(test=test, users=user)) == 0 :
            score = Score(test=test, users=user, grade=score_grade)
        else :
            score = Score.objects.get(test=test, users=user)
            score.grade = score_grade
        score.save()
        return JsonResponse({'is_save_ok' : True})
    else :
        return HttpResponseBadRequest


# 5. 결과 보여주기
def result(request, user_pk, test_num) :
    # test_num = test 번호
    # scores = get_object_or_404(User, pk=user_pk).score_sets
    # print(scores)

    context = {}
    return render(request, 'bigfive/result.html', context)