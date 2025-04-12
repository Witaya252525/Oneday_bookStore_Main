from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category ,Book ,BookComment



def index(request):
    categ_id = request.GET.get('categoryid')  # Get the category ID from the query parameter
    print(categ_id)
    categories = Category.objects.all()  # Fetch all categories
    books = Book.objects.filter(category_id=categ_id) if categ_id else Book.objects.all()
   
    # if categ_id:
    #     books = Book.objects.filter(category_id=categ_id)
    # else:
    #     books = Book.objects.all()



    
    paginator = Paginator(books ,8)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages) 

    

    
    
    return render(request, 'book/index.html', {
        'categories': categories,
        'books': books,
        'categ_id': int(categ_id) if categ_id else None  # Pass the category ID to the template
    })





def detail(request, slug):
    # Fetch the book using the slug
    book = get_object_or_404(Book, slug=slug)
    # Fetch comments using the related_name
    comments = book.bookcomment_set.all()
    return render(request, 'book/detail.html', {'book': book , 'comments': comments})

