from django.shortcuts import render  # not required anymoreHttpResponse

# Create your views here.
# import httpResponse on the top


def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
