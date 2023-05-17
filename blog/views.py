from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm, CustomerForm, TGUserForm, ProductForm, OrderFrom
from .models import TGUser, Product, Category
from django.contrib.auth.decorators import login_required
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator

@login_required(login_url="/users/login/")
def all_categories(request):
    categories = Category.objects.all()
    return render(request, "blog/all_cats.html", {"cats": categories})

@login_required(login_url="/users/login/")
def add_user(request):
    form = TGUserForm()
    if request.method == "POST":
        form = TGUserForm(request.POST)
        if form.is_valid():
            TGUser.objects.create(
                tg_id = form.cleaned_data.get('tg_id'),
                first_name = form.cleaned_data.get('first_name'),
                last_name = form.cleaned_data.get('last_name'),
                user_name = form.cleaned_data.get('user_name'),
                about = form.cleaned_data.get('about'),
            )
            return redirect('index')
    return render(request, "blog/create_user.html", {'form': form})

@login_required(login_url="/users/login/")
def index(request):
    products = Product.objects.all()
    cats = Category.objects.all()
    if request.GET.get('cat'):
        cat = Category.objects.get(title=request.GET.get("cat"))
        products = Product.objects.filter(category=cat.id)

    print(products)
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {'products': products, "cats": cats, "page": page})

@login_required(login_url="/users/login/")
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    return render(request, "blog/product_detail.html", {"product": product})
@login_required(login_url="/users/login/")
def add_product(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "blog/add_product.html", {"form": form})
@login_required(login_url="/users/login/")
def add_book(request):
    form = BookForm()
    return render(request, "blog/create.html", {"form":form})
@login_required(login_url="/users/login/")
def add_order(request):
    form = OrderFrom()
    if request.method == "POST":
        form = OrderFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "blog/add_order.html", {"form": form})
@login_required(login_url="/users/login/")
def add_customer(request):  #shu blogda oshibka bor
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "blog/add_customer.html", {"form": form})
@login_required(login_url="/users/login/")
def update_user(request, pk):
    user = TGUser.objects.get(id=pk)
    form = TGUserForm(instance=user)
    if request.method == "POST":
        form = TGUserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, "blog/update_user.html", {"form": form})
@login_required(login_url="/users/login/")
def delete_user(request, pk):
    user = TGUser.objects.get(id=pk)
    user.delete()
    return redirect('index')