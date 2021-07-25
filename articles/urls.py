from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreate, ArticleUpdate, ArticleDelete

articles_patterns = ([
    path('', ArticleListView.as_view(), name='articles'),
    path('<int:pk>/<slug:slug>/', ArticleDetailView.as_view(), name='article'),
    path('create/', ArticleCreate.as_view(), name='create' ),
    path('update/<int:pk>/', ArticleUpdate.as_view(), name='update' ),
    path('delete/<int:pk>/', ArticleDelete.as_view(), name='delete' ),
],'articles')