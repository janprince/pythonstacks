from django.shortcuts import render
from .forms import ReviewForm
from .models import *
from blog.models import Post


def index(request):
    context = {
        'categories': Category.objects.all(),
        'popular_books': Book.objects.filter(popular=True),
        'top_posts': Post.objects.filter(mostly_viewed=True)[:6]  # 6 most_viewed posts;
    }
    return render(request, "books/index.html", context)


def category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    context = {
        'category': category,
        'categories': Category.objects.all()
    }
    return render(request, "books/category.html", context)


def detail(request, book_slug):
    book = Book.objects.get(slug=book_slug)    # slug
    reviews = book.reviews.filter(active=True)
    new_review = None

    # related book
    book_cat = book.categories.first()             # first category
    related = book_cat.books.all().order_by("?")[:10]               # 10 random related book

    # Comment posted
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)  # pass in the data received to the CommentForm
        if review_form.is_valid():
            # Create a review but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the review
            new_review.book = book
            # Save the review to the database
            new_review.save()

    else:
        review_form = ReviewForm()

    context = {
        'book': book,
        'reviews': reviews,
        'related_books': related,
        'review_form': review_form,
        'new_review': new_review,
        'top_posts': Post.objects.filter(mostly_viewed=True)[:6]  # 6 most_viewed posts;
    }
    return render(request, "books/detail.html", context)
