from rest_framework import serializers
from store.models import Product,Collection,Review,Cart


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
        
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id'] 
