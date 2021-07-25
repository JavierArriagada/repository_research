from django import template
from articles.models import Article

register = template.Library()

@register.simple_tag
def get_article_list():
    articles = Article.objects.all()
    return articles