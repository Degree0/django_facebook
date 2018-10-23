from django.shortcuts import render, redirect

from facebook.models import Article
from facebook.models import Comment

# Create your views here.

def play(request):
    return render(request, 'play.html')



def play2(request):
    a = '정도영'
    age = 20

    if age > 19:
        status = '성인'
    else :
        status = '청소년'


    diary = ['보람찬 하루였다','준수네 집에서 놀았다', '치과가 싫다', '파이썬을 사용해 반복~']


    return render(request, 'play2.html',{'name': a , 'age':status, 'diary':diary })


def profile(request):
    return render(request,'profile.html')

count = 0
def event(request):
    a = '정도영'
    age = 20
    res = ['꽝...','당첨!']

    global count
    count = count + 1

    if count == 7:
        res = res[1]
    else:
        res = res[0]

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    return render(request,'event.html', {'name': a , 'count':count, 'age':status, 'res':res})

def fail(request):
    return render(request,'fail.html')

def help(request):
    return render(request,'help.html')

def warn(request):
    return render(request,'warn.html')

def newsfeed(request):
    # 모든 뉴스피드 글을 불러오는 작업
    # 데이터베이스에서 꺼내오는 것 (모델링한 데이터로부터 가져오는 것)
    articles = Article.objects.all()
    return render(request,'newsfeed.html', {'articles_html':articles})


def detail_feed(request, pk): # request 뒤에 'pk'라는 New parameter 추가!

    #pk번 글을 불러오기
    article_views = Article.objects.get(pk=pk)

    #코멘트를 저장하라
    if request.method=='POST':
        Comment.objects.create(
            article = article_views,
            author = request.POST['nickname'],
            text = request.POST['reply'],
            password = request.POST['password']
        )
        return redirect('/feed/' + str(pk))
    #return redirect('/feed/' + str(article.pk))
    #return redirect(f'/feed/ {pk}')



    return render(request,'detail_feed.html',{'feed': article_views})

def new_feed(request):
    # html폼에서 보내는 데이터를 받아서 처리해야 함.
    ps = '추신: 감사합니다'

    if request.method == 'POST':
        Article.objects.create(
            author = request.POST['nickname'],
            title = request.POST['title'],
            text = request.POST['content'] + ps,
            password = request.POST['password']
        )


    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' :
        article.author  = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()

        return redirect('/feed/' + str(article.pk)) # article.pk는 숫자이므로 문자열로 변환해주는 것.
        # 또는
        # return redirect(f'/feed/{article.pk}')

    return render(request, 'edit_feed.html',{'feed': article})



def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password: #글 수정에서 입력한 비밀번호
            article.delete()
            return redirect('/')

    return render(request, 'remove_feed.html',{'feed': article})