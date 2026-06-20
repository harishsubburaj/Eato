from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="profile_images/",
        default="profile_images/default.png"
    )

    def __str__(self):
        return self.user.username

class Category(models.Model):

    name=models.CharField(max_length=100)

    description=models.TextField(blank=True)

    image=models.ImageField(upload_to='category')

    displayorder=models.IntegerField(default=0)

    status=models.BooleanField(default=True)

    createdat=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Banner(models.Model):

    title = models.CharField(max_length=200)

    image = models.ImageField(upload_to='banner_images/')

    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="product_images/"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    stock = models.IntegerField(
        default=0
    )

    unit = models.CharField(
        max_length=30,
        default="Plate"
    )

    status = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.product.name}"


class Order(models.Model):

    STATUS = [

        ("Pending", "Pending"),

        ("Preparing", "Preparing"),

        ("Out for Delivery", "Out for Delivery"),

        ("Delivered", "Delivered"),

    ]

    PAYMENT = [

        ("Cash on Delivery", "Cash on Delivery"),

        ("UPI", "UPI"),

        ("Card", "Card"),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    customer_name = models.CharField(max_length=150)

    address = models.TextField()

    payment_method = models.CharField(
        max_length=30,
        choices=PAYMENT
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default="Pending"
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.customer_name


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.IntegerField(default=1)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return self.product.name
 