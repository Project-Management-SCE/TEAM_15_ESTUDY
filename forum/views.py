from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views import View
from forum.form import PostForumForm, CommentForm
from forum.models import Post
from accounts.models import User

class forumView(View):
    def get(self, request):
        form_post = PostForumForm()
        return render(
            request,
            "fourm.html",
            {
                "form_post": form_post,
            },
        )
    def post(self, request, user_id):
        form = PostForumForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=user_id)
            post = Post.objects.create(
                user=user, title="", message=form.cleaned_data["message"]
            )
            post.save()
        return redirect("Forum:forum-main")

    
def PostComments(request, user_id, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = User.objects.get(pk=user_id)
            post = Post.objects.get(pk=post_id)
            comment = Comment.objects.create(
                user=user, post=post, message=form.cleaned_data["message"]
            )
            comment.save()
    return redirect("Forum:forum-main")



@user_passes_test(is_lecturer_or_is_superuser)
def DeletePost(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect("Forum:forum-main")


@user_passes_test(is_lecturer_or_is_superuser)
def DeleteComment(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect("Forum:forum-main")
