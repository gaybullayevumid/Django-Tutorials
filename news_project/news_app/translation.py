from modeltranslation.translator import register, TranslationOptions, translator
from .models import Category, News

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')

# 2-usul
# translator.register(News, NewsTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)