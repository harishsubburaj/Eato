from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Category, Banner, Product, Cart, Order, OrderItem
from .forms import BannerForm
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=email).exists():

            messages.error(
                request,
                "Account already exists. Please login."
            )

            return render(request, 'signup.html')

        User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully."
        )

        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.is_superuser:
                return redirect('admindashboard')

            return redirect('userdashboard')

    return render(request, 'login.html')

def admindashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    return render(request, "admindashboard.html", {
        "profile": profile,
        "page_title": "Dashboard"
    })

def admin_sidebar(request):
    return render(request, 'adminsidebar.html')

def admin_navbar(request):
    return render(request, 'adminnavbar.html')

def addproduct(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    products = Product.objects.all()
    return render(request, "addproduct.html", {
        "profile": profile,
        "products": products,
        "page_title": "Add Product"
    })

def addcategory(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    search = request.GET.get("search")
    categories=Category.objects.all()
    if search:
        categories = categories.filter(name__icontains=search)
    return render(request, "addcategory.html", {
        "profile": profile,
        'categories':categories,
        "page_title": "Add Category"
    })

def incomeorder(request):
    orders = Order.objects.all().order_by("-created_at")

    return render(

        request,

        "incomeorder.html",

        {

            "orders": orders

        }

    )


def acceptorder(request, id):

    order = Order.objects.get(id=id)

    order.status = "Preparing"

    order.save()

    return redirect("incomeorder")


def updateorderstatus(request, id):

    order = Order.objects.get(id=id)

    if order.status == "Pending":

        order.status = "Preparing"

    elif order.status == "Preparing":

        order.status = "Out for Delivery"

    elif order.status == "Out for Delivery":

        order.status = "Delivered"

    order.save()

    return redirect("incomeorder")


def myorders(request):

    orders = Order.objects.filter(

        user=request.user

    ).order_by("-created_at")

    return render(

        request,

        "myorders.html",

        {

            "orders": orders

        }

    )


def ordersuccess(request):

    return render(request, "ordersuccess.html")

def users (request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "users.html", {
        "profile": profile,
        "page_title": "Users"
    })

def addrestaurant(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "addrestaurant.html", {
        "profile": profile,
        "page_title": "Add Restaurant"
    })

def coupon(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "coupon.html", {
        "profile": profile,
        "page_title": "Coupon"
    })

def banner(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "banner.html", {
        "profile": profile,
        "page_title": "Banner"
    })

def settings(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request, "settings.html", {
        "profile": profile,
        "page_title": "Settings"
    })

@login_required
def edit_admin_profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":

        request.user.first_name = request.POST.get("name")
        request.user.save()

        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES["profile_image"]
            profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect("admindashboard")

    return render(request, "edit_admin_profile.html", {
        "profile": profile
    })

def add_product_form(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    categories = Category.objects.filter(status=True)

    if request.method == "POST":

        Product.objects.create(

            category_id=request.POST["category"],

            name=request.POST["name"],

            description=request.POST["description"],

            price=request.POST["price"],

            discount_price=request.POST.get("discount_price") or None,

            stock=request.POST["stock"],

            unit=request.POST["unit"],

            status=request.POST["status"] == "True",

            image=request.FILES["image"]

        )

        return redirect("addproduct")

    return render(request, "addproductform.html", {
        "profile": profile,
        "categories": categories
    })

def addcategoryform(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    return render(request,"addcategoryform.html",{
        "profile": profile,
        "page_title":"Add New Category"
    })

def addcategoryform(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == "POST":

        Category.objects.create(
            name=request.POST["name"],
            image=request.FILES["image"],
            status=request.POST["status"] == "True"
        )

        return redirect("addcategory")

    return render(request, "addcategoryform.html", {
        "profile": profile,
        "page_title": "Add New Category"
    })

def deletecategory(request, id):

    category = get_object_or_404(Category, id=id)

    category.delete()

    return redirect("addcategory")

def editcategory(request, id):

    category = Category.objects.get(id=id)

    if request.method == "POST":

        category.name = request.POST["name"]
        category.status = request.POST["status"] == "True"
        if request.FILES.get("image"):
            category.image = request.FILES["image"]
        category.save()

        return redirect("addcategory")

    return render(request, "editcategory.html", {
        "page_title": "Edit Category",
        "category": category
    })

def sidebar(request):
    return render(request, 'sidebar.html')

def navbar(request):
    return render(request, 'navbar.html')

def banner(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    banners = Banner.objects.all()

    return render(request,'banner.html',{
        "profile": profile,
        'banners':banners

    })

def addnewbanner(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method=="POST":

        form=BannerForm(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('banner')

    else:

        form=BannerForm()

    return render(request,'addnewbannerform.html',{
        "profile": profile,
        'form':form

    })

def userdashboard(request):

    banners = Banner.objects.filter(status=True)
    categories = Category.objects.filter(status=True)
    products = Product.objects.filter(status=True)

    return render(request, 'userdashboard.html', {
        'banners': banners,
        "categories": categories,
        "products": products
    })

from django.shortcuts import get_object_or_404

def addtocart(request, id):

    product = get_object_or_404(Product, id=id)

    cart_item, created = Cart.objects.get_or_create(

        user=request.user,

        product=product

    )

    if not created:

        cart_item.quantity += 1

        cart_item.save()

    return redirect('cart')


@login_required
def buynow(request, id):

    product = get_object_or_404(Product, id=id)

    # Clear existing cart and add only this product for immediate purchase
    Cart.objects.filter(user=request.user).delete()

    Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect('payment')


def cart(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    delivery = 0

    platform = 5

    grand_total = total + platform + delivery

    return render(request, 'cart.html', {

        'cart_items': cart_items,

        'total': total,

        'delivery': delivery,

        'platform': platform,

        'grand_total': grand_total

    })


def removecart(request, id):

    item = get_object_or_404(Cart, id=id, user=request.user)

    item.delete()

    return redirect('cart')


def payment(request):

    cart_items = Cart.objects.filter(user=request.user)

    total = 0

    for item in cart_items:

        total += item.product.price * item.quantity

    delivery = 0

    platform = 5

    grand_total = total + platform + delivery

    if request.method == 'POST':

        customer_name = request.POST['customer_name']
        phone = request.POST.get('phone')
        address = request.POST['address']
        payment_method = request.POST['payment_method']

        order = Order.objects.create(

            user=request.user,

            customer_name=customer_name,

            address=address,

            payment_method=payment_method,

            total=grand_total

        )

        for item in cart_items:

            OrderItem.objects.create(

                order=order,

                product=item.product,

                quantity=item.quantity,

                price=item.product.price

            )

        # clear cart
        cart_items.delete()

        return redirect('ordersuccess')

    return render(request, 'payment.html', {

        'cart_items': cart_items,

        'total': total,

        'delivery': delivery,

        'platform': platform,

        'grand_total': grand_total

    })

from .models import Banner

def editbanner(request, id):

    banner = Banner.objects.get(id=id)

    if request.method == "POST":

        banner.title = request.POST['title']
        banner.status = request.POST['status']

        if request.FILES.get('image'):
            banner.image = request.FILES['image']

        banner.save()

        return redirect('banner')

    return render(request, 'editbannerform.html', {
        'banner': banner
    })

def deletebanner(request, id):

    banner = Banner.objects.get(id=id)

    banner.delete()

    return redirect('banner')

def category(request):

    categories = Category.objects.filter(status=True)

    return render(request, "category.html", {
        "categories": categories
    })