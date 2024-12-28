from rest_framework import serializers
from store.models import Product,Collection,Review,Cart,CartItem


class ColectionSerializer1(serializers.ModelSerializer):
   class Meta:
       model = Collection
       fields = ['id','title'] 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','slug','inventory','unit_price','collection']
    #collection = serializers.HyperlinkedRelatedField(queryset = Collection.objects.all(),view_name = 'collection-detail')

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id','title','product_count']
    product_count = serializers.SerializerMethodField(method_name = 'get_count' )
    def get_count(self,obj):
        return obj.product.count()
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','date','product','name','description']
        
class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','unit_price']
class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    def get_total_price(self,obj):
        return obj.product.unit_price * obj.quantity
    class Meta:
        model = CartItem
        fields = ['id','product','quantity','total_price']
    
class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many = True,read_only= True)
    total_cart_price = serializers.SerializerMethodField(method_name='get_total')
    def get_total(self,cart):
        return sum([item.quantity * item.product.unit_price for item in cart.items.all()])
    class Meta:
        model = Cart
        fields = ['id','items','total_cart_price'] 

