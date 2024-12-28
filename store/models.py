from django.db import models
from uuid import uuid4


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey('Product',on_delete=models.SET_NULL,null =True,related_name='+')
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField((""))
    unit_price = models.DecimalField(max_digits = 6 ,decimal_places= 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection,related_name='product',on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion,related_name='products')
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']

class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold')
    ]
    first_name = models.CharField(max_length=255)
    last_naem = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1 ,choices=MEMBERSHIP_CHOICES, default = MEMBERSHIP_BRONZE)
    class Meta:
        db_table = 'store_customer'
        indexes = [
            models.Index(fields=['last_naem','first_name'])
        ]
    def __str__(self) -> str:
        return self.first_name + " " + self.last_naem

class Order(models.Model):
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETED = 'C'
    PAYMENT_FAILED = 'F'
    PAYMENTS = [
        (PAYMENT_PENDING,'Pending'),
        (PAYMENT_COMPLETED,'Completed'),
        (PAYMENT_FAILED,'Failed')
    ]
    placed_at =models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length= 1, choices=PAYMENTS,default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.PositiveBigIntegerField(default=0)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    product = models.ForeignKey(Product,on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6,decimal_places=2)

class Cart(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid4)
    created_time = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    class Meta:
        unique_together = [['cart','product']]

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
