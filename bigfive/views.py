from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseBadRequest
from accounts.models import User
from accounts.forms import UserCreationForm
from .models import Test, Score, Adjective
import random

# serailizers
from .serializers import TestSerializer, SearchTestSerializer, SearchTestTypeSerializer, SearchUserTestSerializer, ScoreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


def qtol(query) :
    result_list = []
    for q in query :
        result_list.append(q)
    return result_list

def choicetest(test_num) :
    label_set = ['N', 'E', 'O', 'A', 'C']

    # 50개는 각 특성별 key별 5개씩 총 50개
    # 100개는 각 특성별 key별 10개씩 총 100개
    testlists = []
    
    for label in label_set :
        plus_tests = Test.objects.filter(testname=test_num, label=label, key=1).exclude(question_ko='').order_by('?')[:(test_num/10)]
        minus_tests = Test.objects.filter(testname=test_num, label=label, key=-1).exclude(question_ko='').order_by('?')[:(test_num/10)]
        testlists += qtol(plus_tests) + qtol(minus_tests)
        print(len(testlists))

    return testlists

def testchoice(test_num) :
    label_set = ['N', 'E', 'O', 'A', 'C']
    facets = [['Anxiety', 'Anger', 'Depression', 'Self-Consciousness', 'Immoderation', 'Vulnerability'],
                ['Friendliness', 'Gregariousness', 'Assertiveness', 'Activity-Level', 'Excitement-Seeking', 'Cheerfulness'],
                ['Imagination', 'Artistic-Interests', 'Emotionality', 'Adventurousness', 'Intellect', 'Liberalism'],
                ['Trust', 'Morality', 'Altruism', 'Cooperation', 'Modesty', 'Sympathy'],
                ['Self-Efficacy', 'Orderliness', 'Dutifulness', 'Achievement-Striving', 'Self-Discipline', 'Cautiousness']]
    if test_num == 120 :
        label_count = [[(4, 0), (3, 1), (3, 1), (3, 1), (1, 3), (3, 1)],
                        [(3, 1), (2, 2), (3, 1), (3, 1), (4, 0), (4, 0)],
                        [(4, 0), (2, 2), (2, 2), (1, 3), (1, 3), (2, 2)],
                        [(3, 1), (0, 4), (2, 2), (0, 4), (0, 4), (2, 2)],
                        [(4, 0), (1, 3), (2, 2), (2, 2), (2, 2), (0, 4)]]
    elif test_num == 240 :
        label_count = [[(4, 4), (5, 3), (6, 2), (5, 3), (4, 4), (3, 5)],
                        [(6, 2), (4, 4), (4, 4), (5, 3), (6, 2), (4, 4)],
                        [(3, 5), (5, 3), (5, 3), (3, 5), (5, 3), (3, 5)],
                        [(5, 3), (3, 5), (5, 3), (3, 5), (4, 4), (6, 2)],
                        [(5, 3), (3, 5), (6, 2), (5, 3), (4, 4), (5, 3)]]
    elif test_num == 300 :
        label_count = [[(5, 5), (5, 5), (7, 3), (6, 4), (5, 5), (5, 5)],
                        [(5, 5), (5, 5), (5, 5), (5, 5), (8, 2), (8, 2)],
                        [(6, 4), (5, 5), (5, 5), (4, 6), (5, 5), (3, 7)],
                        [(6, 4), (2, 8), (5, 5), (3, 7), (4, 6), (4, 6)],
                        [(6, 4), (5, 5), (5, 5), (7, 3), (5, 5), (3, 7)]]
    
    testlists= []
    for label in label_set :
        leng = 0
        idx = label_set.index(label)
        for facet in facets[idx] :
            idxx = facets[idx].index(facet)
            p = label_count[idx][idxx][0]
            q = label_count[idx][idxx][1]
                
            plus_tests = Test.objects.filter(testname=test_num, label=label, facet=facet, key=1).order_by('?')[:p]
            minus_tests = Test.objects.filter(testname=test_num, label=label, facet=facet, key=-1).order_by('?')[:q]
            leng += len(plus_tests) + len(minus_tests)
            testlists += qtol(plus_tests) + qtol(minus_tests)
        print(leng, '-------------------')
    print(len(testlists), testlists)
    return testlists

# 4. 각 설문에 해당하는 질문 넘기기
@api_view(['GET'])
def gettest(request, test_num) :
    print(test_num, type(test_num))
    # db test에 OCEAN을 저장해놓고 불러와서 score랑 매칭
    # 0) 해당 테스트에 결과값이 있으면 지우기

    # 1) TEST 모두 저장 
    # 2) pk별로 저장 될 model(test_pk, score, user_pk)

    # 12문항
    if test_num == 12 :
        tests = Test.objects.filter(testname=12)
        testlists = makefor(tests)

    # 50, 100개 랜덤으로 뽑기 문항
    elif test_num == 50 or test_num == 100 :
        testlists = choicetest(test_num)
    
    # 120, 300개 랜덤으로 뽑기 문항
    elif test_num == 120 or test_num == 240 or test_num == 300 :
        testlists = testchoice(test_num)

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
    resultlists = []
    user = get_object_or_404(User, pk=user_pk)
    # tests = Test.objects.filter(testname=test_num)
    scores = Score.objects.filter(users=user)
    # 해당 설문에 대한 object 저장
    for score in scores :
        if score.test.testname == test_num :
            resultlists.append(score)
    print(resultlists)

    # 해당 설문에 대한 점수 계산한 결과 저장
    if test_num == 12 :
        label_score_set = [0]*5
        label_set = ['N', 'E', 'O', 'A', 'C']
        for score in resultlists :
            print(score.test.label, score.grade)
            idx = label_set.index(score.test.label)
            print(idx)
            if score.test.key == 1 :
                label_score_set[idx] += score.grade
            else :
                label_score_set[idx] += (6-score.grade)
            print('22', label_score_set)
        print(label_score_set)
    
        # 검사 결과 [https://persket.com/319]
        # E, N, C 
        # 2~4점 낮음, 5~6점 중간 7~8점 중상 9~10 높음
        # A(남성) 9점이하 낮음, 10~11점 중하 12~13점 중상 14~15점 높음
        # A(여성) 11점이하 낮음, 12~13점 중하 14점 중상 15점 높음
        # O
        # 8점이하 낮음 9~10점 중하 11~12점 중상 13~15점 높음

    else :
        label_score_set = [0]*5
        label_set = ['N', 'E', 'O', 'A', 'C']
        for score in resultlists :
            print(score.test.label, score.grade)
            idx = label_set.index(score.test.label)
            print(idx)
            if score.test.key == 1 :
                label_score_set[idx] += score.grade
            else :
                label_score_set[idx] += (6-score.grade)
            print('22', label_score_set)
        print(label_score_set)
   

    context = {'resultlists' : resultlists, 'score_set':label_score_set}
    return render(request, 'bigfive/result.html', context)




# API
@api_view(['GET'])
def TestGetSerializer(request) :
    tests = Test.objects.all()
    print(tests)
    serializer = TestSerializer(tests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TestInfoSerializer(request, test_pk):
    test = Test.objects.filter(pk=test_pk)
    print(test)
    serializer = SearchTestSerializer(test, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def TestTypeGetSerializer(request, test_num):
    tests = Test.objects.filter(testname=test_num)
    serializer = SearchTestTypeSerializer(tests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ScoreGetSerializer(request, user_pk, test_num) :
    # test = get_object_or_404(Test, testname=test_num)
    user = get_object_or_404(User, pk=user_pk)
    scores = Score.objects.filter(users=user)
    print('1', scores)
    for score in scores :
        if score.test.testname == test_num :
            score.grade = 0
            score.save()
    print('2', scores)
    serializer = ScoreSerializer(scores, many=True)
    return Response(serializer.data)