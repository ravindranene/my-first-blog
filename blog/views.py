from django.shortcuts import render


# https://www.pythonanywhere.com/forums/topic/2246/#id_post_34665

# Create your views here.
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{})



