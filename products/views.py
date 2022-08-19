from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q
from decimal import Decimal

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm
from profiles.models import UserProfile

# Create your views here.


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ Returns details for selected product """
    current_url = request.META.get('HTTP_REFERER')
    product = get_object_or_404(Product, pk=product_id)
    comming_from = ''
    if 'deals' in current_url:
        comming_from = 'deals'
    elif 'products' in current_url:
        comming_from = 'products'

    context = {
        'product': product,
        'comming_from': comming_from
    }
    return render(request, 'products/product_detail.html', context)


@login_required()
def add_product(request):
    """ Add products to the store """
    if not request.user.is_superuser:
        messages.warning(request, 'Only admins are allowed there...')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        product = form.save()
        if form.is_valid():
            messages.success(request, f'Successfully created product, {product.name}')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    context = {
        'form': form,
    }
    return render(request, 'products/add_product.html', context)


@login_required()
def edit_product(request, product_id):
    """ Form to edit products """
    if not request.user.is_superuser:
        messages.warning(request, 'Only admins are allowed there...')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {product.name}.')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are currently editing product: {product.name}')
    context = {
        'form': form,
        'product': product
    }
    return render(request, 'products/edit_product.html', context)


@login_required()
def delete_product(request, product_id):
    """ Deletes product from the store """
    if not request.user.is_superuser:
        messages.warning(request, 'Only admins can do that...')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'Product {product.name} was deleted')
    return redirect(reverse('products'))


def calc_rating(product):
    num_of_reviews = Review.objects.filter(product=product)
    total_score = 0
    for review in num_of_reviews:
        total_score += review.user_rating
    final_rating = total_score / num_of_reviews.count()
    return final_rating


def product_review(request, product_id):
    """ Returns review form to leave reviews """
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(UserProfile, user=request.user)
    if Review.objects.filter(user=user, product=product).exists():
        messages.info(request, "You've already rated this product.")
        return redirect(reverse('profile'))
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        user_rating = request.POST['user_rating']
        if form.is_valid():
            Review.objects.create(
                user=user,
                product=product,
                user_rating=user_rating,
            )
            product.rating = calc_rating(product)
            product.save()
            messages.success(request, f'Successfully rated {product.name} {user_rating}/5')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(request, 'Failed to review product. Please ensure the form is valid.')
    form = ReviewForm()            
    context = {
        'form': form,
        'product': product,
    }
    
    return render(request, 'products/product_review.html', context)

