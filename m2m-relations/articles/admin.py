from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            for key, value in form.cleaned_data.items():
                if key == 'is_main' and value is True:
                    counter += 1
        if counter > 1:
            raise ValidationError('Основной раздел может быть только один.')

        return super().clean()

class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 2
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline, ]