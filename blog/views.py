from django.shortcuts import render

def favorite(request):
  context = {'name': 'Isaac', 'birth_day': 'December 14'}
  return render(request, 'blog/favorite.html', context)
