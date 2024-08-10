from django.core.paginator import Paginator
from django.shortcuts import render
from article_module.models import Article_List, Article_Category
# from jalali_date import datetime2jalali, date2jalali

# Create your views here.


def articles_list(request):
    object_list = Article_List.objects.filter(is_active=True)
    paginator = Paginator(object_list, 1)  # 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # jalali_join = date2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    context = {
        # 'articles': articles,
        'page_objs': page_obj,
        # 'date': jalali_join
    }
    return render(request, 'Articles/articles_list.html', context)


