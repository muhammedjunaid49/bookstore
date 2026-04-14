def cart_count(request):
    cart = request.session.get('cart', {})
    return {'itc': sum(cart.values()) if cart else 0}