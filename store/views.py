from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Book
from django.db.models import Q
from .models import  Cart


def home(request):
    offer_books = Book.objects.filter(is_offer=True)
    kids = Book.objects.filter(is_kids=True)
    trending_books = Book.objects.filter(is_trending=True)
    new_arrival = Book.objects.filter(is_new=True)
    best_seller = Book.objects.filter(is_best_seller=True)
    anime = Book.objects.filter(is_anime=True)
    pack = Book.objects.filter(is_pack=True)

    return render(request, 'home.html', {
        'offer_books': offer_books,
        'kids': kids,
        'trending_books': trending_books,
        'new_arrival': new_arrival,
        'best_seller': best_seller,
        'anime': anime,
        'pack': pack,
    })


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # check if user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'registration.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, email=email, password=password)

        return redirect('login')

    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def all_trendingbooks(request):
    trendingbooks = Book.objects.filter(is_trending=True)
    return render(request, 'all_trendingbook.html', {'trendingbooks': trendingbooks})

def all_offerbooks(request):
    offerbooks=Book.objects.filter(is_offer=True)
    return render(request,'allofferpage.html', {'offerbooks':offerbooks})

def all_newbooks(request):
    newbooks=Book.objects.filter(is_new =True)
    return render(request,'all_new_arrival.html',{'newbooks':newbooks})

def all_best(request):
    bestseller=Book.objects.filter(is_best_seller =True)
    return render(request,'all_best.html',{'bestseller':bestseller})

def all_anime(request):
    anime=Book.objects.filter(is_anime =True)
    return render (request,'all_anime.html',{'anime':anime})

def all_pack(request):
    pack=Book.objects.filter(is_pack =True)
    return render(request,'all_pack.html',{'pack':pack})

def all_kids(request):
    kids=Book.objects.filter(is_kids =True)
    return render(request,'all_kids.html',{'kids':kids})

def search_books(request):
    query = request.GET.get('q')

    results = []

    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, 'search_results.html', {
        'query': query,
        'results': results
    })


def product_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'product_page.html', {'book': book})

def cart_view(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for book_id, qty in cart.items():
        book = Book.objects.get(id=book_id)
        subtotal = book.price * qty
        total += subtotal

        items.append({
            'book': book,
            'qty': qty,
            'subtotal': subtotal
        })

    return render(request, 'add_to_cart.html', {
        'items': items,
        'total': total
    })

def update_cart(request, id):
    qty = int(request.POST.get('qty'))

    cart = request.session.get('cart', {})
    cart[str(id)] = qty

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')  

def add_to_cart(request, id):
    if request.method == "POST":
        cart = request.session.get('cart', {})

        qty = int(request.POST.get('qty', 1))

        cart[str(id)] = cart.get(str(id), 0) + qty

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('cart')   

def cart_count(request):
    cart = request.session.get('cart', {})
    count = 0

    for qty in cart.values():
        count += qty

    return {'itc': count}

def remove_from_cart(request, id):
    cart = request.session.get('cart', {})

    if str(id) in cart:
        del cart[str(id)]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')  

def payment(request):
    cart = request.session.get('cart', {})
    total = 0

    

    for book_id, qty in cart.items():
        book = Book.objects.get(id=book_id)
        total += book.price * qty

    return render(request, 'payment.html', {'total': total})
def buy_now(request, id):
    from .models import Book

    try:
        book = Book.objects.get(id=id)
        total = book.price
    except Book.DoesNotExist:
        book = None
        total = 0

    return render(request, 'singlepayment.html', {
        'book': book,
        'total': total
    })
