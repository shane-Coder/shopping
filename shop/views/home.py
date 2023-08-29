from django.shortcuts import render, redirect, HttpResponseRedirect
from shop.models.product import Products
from shop.models.category import Category
from django.views import View

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')
    
    def get(self, request):
        return HttpResponseRedirect(f'/shop{request.get_full_path()[1:]}')

def shop(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    CategoryID = request.GET.get('category')
    if CategoryID:
        products = Products.get_all_products_by_categoryid(CategoryID)
    else:
        products = Products.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories

    print('You are : ', request.session.get('email'))
    return render(request, 'index.html', data)