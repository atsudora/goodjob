from django.views.generic import ListView, CreateView
from .models import Post

''' 投稿表示機能 '''
class PostListView(ListView):
    model = Post
    template_name = "wortalk/index.html"
    context_object_name = 'posts'                   # listview一個一個につける名前
    ordering = ['-date_posted']                     # -(マイナス)つけることで新しい順に並べる。timezone.nowの逆順
    paginate_by = 10                                # １ページに表示する投稿数

''' 新規投稿機能 '''
class PostCreateView(CreateView):
    model = Post
    fields = ['content']                            # 投稿を作る時にmodelsからcontentを使う
    template_name = 'wortalk/post_create.html'
    success_url = '/'                               # 投稿完了後、/に戻る