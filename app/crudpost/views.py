from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Home(request):
    list_post = Post.objects.all().order_by('-created_at')
    context = {
        'posts': list_post
    }
    return render(request, 'crudpost/home.html', context)

@login_required
def PostView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'crudpost/postdetail.html', {'post':post})

@login_required
def CreatePostView(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit= False)
            post.author = request.user
            post.save()
            return redirect('Home')
    else:
        form = PostForm()
    return render(request, 'crudpost/createpost.html', {'form': form})

@login_required
def UpdatePostView(request, pk):
    return render(request, 'crudpost/postupdate.html')

@login_required
def DeletePostView(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        return redirect('Home')
    
    if request.method == 'POST':
        post.delete()

        return redirect('Profile', username = request.user.username)
    
    return render(request, 'crudpost/post_delete.html')

