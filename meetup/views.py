from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import Board
from .forms import BoardForm, AccountForm
from .forms import BoardForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
# from django.views.generic import TemplateView
# from django.views.generic.edit import CreateView
# #from .forms import CreateUserForm
# from django.core.urlresolvers import reverse_lazy

#class CreateUserView(CreateView): 
  #  template_name = 'registration/signup.html'
   # form_class =  CreateUserForm
    #success_url = reverse_lazy('create_user_done')


#class RegisteredView(TemplateView):
 #   template_name = 'registration/signup_done.html'

def main(request):
    
    return render(request, 'meetup/main.html')

def makepage(request):
    return render(request, 'meetup/makepage.html')

def login(request):
    return render(request, 'meetup/login.html')

def signup(request):
    return render(request, 'meetup/signup.html')

def postlist(request):
    boards = Board.objects
    return render(request, 'meetup/postlist.html',{'boards':boards})

def mypage(request):
    return render(request, 'meetup/mypage.html')

def board(request):
    boards = Board.objects
    return render(request, 'meetup/board.html', {'boards':boards})

def boardform(request, board=None):
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            board.save()
            return joinResult(request)
    else:
        # instance=blog는 없어도 되는데 뒤에 edit에서 사용하기 위함
        form = BoardForm(instance=board)
        return render(request, 'meetup/boardform.html', {'form': form})

def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return boardform(request, board)

def remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('postlist')


def result_page(request):
    return render(request, 'meetup/result_page.html', {'board':{'lat': 37.50611, 'lng': 127.0616346}})

def joinResult(request):
    return render(request, 'meetup/result_page.html', {'board':{'lat': 37.50611, 'lng': 127.0616346}})

def attend(request, pk):
    board = get_object_or_404(Board, pk=pk)
    name = request.GET['name']
    board.join_list.append(name)
    return joinResult(request, pk)

@csrf_exempt
def signup(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create(username=username, email=email, password=password)
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            return redirect('postlist')
    else:
        form = AccountForm()
        print("##############################################################")
        return render(request, 'meetup/signup.html', {'form':form})
