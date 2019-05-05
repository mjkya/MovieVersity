import sys
sys.path.insert(0, 'workspace/Newbie_6/board/models.py')
from django.shortcuts import render, redirect, get_object_or_404
import board


# def joinResult(request, board_id):
#     board_detail = get_object_or_404(board, pk = board_id)
#     return render(request, 'joinResult.html', {'board':{'lat': -34.397, 'lng': 150.644}})

def joinResult(request):
    return render(request, 'joinResult.html', {'board':{'lat': -34.397, 'lng': 150.644}})
