from django.shortcuts import render
import os
import sys
#sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from test_app.documents import ProductsDocument

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search
from elasticsearch_dsl import Q

def search(request):

    return render(request, 'search.html')



def results(request):
    #title = request.GET.get('title')
    #local = request.GET.get('local')
    details = request.GET.get('details')
    cate3 = request.GET.get('cate3')
    #print('aa' + products.name)
    #print('bb' + products.site_name)
    #print('cc' + products.cate1)

    posts = []
    client = Elasticsearch()
    if details and cate3 != '모두' :
        posts = Search(using=client, index="test_app_restaurants") \
            .query("match", details=details) \
            .filter("term", cate3=cate3) \
            #.filter("term", local=local) \
            #.filter("term", title=title)

    elif details and cate3 == '모두':
        ㅎ = Search(using=client, index="test_app_restaurants") \
            .query("match", details=details) \
            #.filter("term", local=local) \
            #.filter("term", title=title)
    else:
        posts = ''

    # scoreing 부분 추가

    if not posts:
        response = posts.execute()
        h = response.hits[0]
        print('/%s/%s/%s returned with score %f' % (
            h.meta.index, h.meta.doc_type, h.meta.id, h.meta.score))

    return render(request, 'results.html', {'posts': posts})




# from elasticsearch import Elasticsearch
# from elasticsearch_dsl import Search
#
# client = Elasticsearch()
#
# s = Search(using=client, index="test_products") \
#     .filter("term", name="데코빈") \
#     .filter("term", site_name="gsshop") \
#     .filter("term", cate1="10x10") \
#     #.query("match", pid="12536377" )   \
#     #.exclude("match", description="beta")
#
# s.aggs.bucket('per_tag', 'terms', field='tags') \
#     .metric('max_lines', 'max', field='lines')
#
# response = s.execute()
# #print(response)
# for hit in response:
#     print(hit.name, hit.cate1)
#
# for tag in response.aggregations.per_tag.buckets:
#     print(tag.key, tag.max_lines.value)
