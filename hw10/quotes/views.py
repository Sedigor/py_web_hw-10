from django.shortcuts import render
import utils.connect
from models.models import Author, Quote
from django.core.paginator import Paginator

def main(request, page=1):
    quotes = Quote.objects()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, 'quotes/index.html', context={'quotes': quotes_on_page})
