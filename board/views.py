from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import get_object_or_404, render, redirect
from .models import Board
from .forms import BoardForm

# Create your views here.
def board(request):
    boards = Board.objects
    return render(request, 'board.html', {'boards':boards})

def boardform(request, board=None):
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.pub_date = timezone.now()
            board.save()
            return redirect('board')
    else:
        # instance=blog는 없어도 되는데 뒤에 edit에서 사용하기 위함
        form = BoardForm(instance=board)
        return render(request, 'boardform.html', {'form': form})

def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return boardform(request, board)

def remove(request, pk):
    board = get_object_or_404(Board, pk=pk)
    board.delete()
    return redirect('board')

# def joinResult(request, board_id):
#     board_detail = get_object_or_404(board, pk = board_id)
#     return render(request, 'joinResult.html', {'board':{'lat': -34.397, 'lng': 150.644}})

def joinResult(request):
    return render(request, 'joinResult.html', {'board':{'lat': -34.397, 'lng': 150.644}})

def signup(request):
    # user = User()
    # user.name = request.POST.get('username')
    # user.password = request.POST.get('password')
    # user.email = request.POST.get('email')
    # user.school = request.POST.get('school')
    # user.save()

    # return render(request, 'signup.html')
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            User.objects.create(username=username, email=email, password=password)
            return redirect('board')
    else:
        form = AccountForm()
        return render(request, 'signup.html', {'form':form})

