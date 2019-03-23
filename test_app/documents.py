from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl import DocType, Index, fields

#from .models import Ad, Category, Car, Manufacturer, Products
from .models import Restaurants
# car = Index('test_cars')
# car.settings(
#     number_of_shards=1,
#     number_of_replicas=0
# )

restaurants = Index('test_app_restaurants')
restaurants.settings(
    number_of_shards=1,
    number_of_replicas=0
)



nori_korean = analyzer(
    'nori_korean',
    tokenizer= "nori_tokenizer",
    filter=["lowercase", "stop"],
)

keyword = analyzer(
    'keyword',
    tokenizer= "keyword",
)

class RestaurantsDocument(DocType):
    details = fields.TextField(
        analyzer=nori_korean,
        fields={'raw': fields.KeywordField()}
    )
    cate3 = fields.TextField(
        analyzer=keyword,
        fields={'raw': fields.KeywordField()}
    )

    class Meta:
        model = Restaurants
        index = 'test_app_restaurants'
        fields = [
            'title',
            'cate1',
            'cate2',
            'local',
            'city',
        ]


