from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def result(request):
    entered_text = request.GET['fulltext']  # 요청이 들어오면 fulltext를 가져와라
    word_list = entered_text.split()    # entered_text를 공백 기준으로 문자열을 나누겠다
    
    word_dictionary = {}
    
    for word in word_list:      # {word:출현 횟수}로 만들어줌
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    
    return render(request, 'result.html',{'alltext': entered_text, 'dictionary':word_dictionary.items()})   # result.html에 변수 전달하기
