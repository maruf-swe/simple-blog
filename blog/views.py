from django.shortcuts import render

# Create your views here.
posts = [
    {'author': 'maruf',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'August 27, 2018'
     },
    {'author': 'robel',
     'title': 'Blog Post 2',
     'content': 'second post content',
     'date_posted': 'August 27, 2018'
     }
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
