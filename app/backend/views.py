from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
import logging

from django.db.models import Min , Q
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

from django.utils.encoding import uri_to_iri
from collections import Counter

logger = logging.getLogger(__name__)

def transform_vn(name):
    INTAB = "ạảãàáâậầấẩẫăắằặẳẵóòọõỏôộổỗồốơờớợởỡéèẻẹẽêếềệểễúùụủũưựữửừứíìịỉĩýỳỷỵỹđ"

    OUTTAB = "a"*17 + "o"*17 + "e"*11 + "u"*11 + "i"*5 + "y"*5 + "d"

    r = re.compile("|".join(INTAB))
    replaces_dict = dict(zip(INTAB, OUTTAB))

    return r.sub(lambda m: replaces_dict[m.group(0)], name)

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    
    products_serializer = ProductSerializer(products, many=True)
    return JsonResponse(products_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    # 'safe=False' for objects serialization

def keys_list(request):
    keys = Key.objects.all()
    
    keys_serializer = KeySerializers(keys, many=True)
    return JsonResponse(keys_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

def product_detail(request, id):
    # find product by id 
    try: 
        product = Product.objects.get(pk = id) 
        product_serializer = ProductSerializer(product) 
        return JsonResponse(product_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    except product.DoesNotExist: 
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 


def products_by_key_id(request, key_id):
    try:
        # find key by id 
        key = Key.objects.get(pk = key_id)
        
        # find products related to that key
        products = key.products.all().order_by('price_sale')

        product_serializer = ProductSerializer(products, many = True) 
        return JsonResponse(product_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    except key.DoesNotExist: 
        return JsonResponse({'message': 'The Key does not exist'}, status=status.HTTP_404_NOT_FOUND) 

def keys_by_name(request, key_name):
    # find product by name
    parsed = uri_to_iri(key_name)
    words = transform_vn(parsed).split('+')
    keys = []
    for word in words:
        try:
            keys_serializer = KeySerializers(Key.objects.filter(transformed_name__icontains = word), many=True)
            keys = keys + keys_serializer.data
        except:
            pass

    counter = Counter(map(lambda x:x['id'], keys))
    filtered_keys = []
    for i in counter:
        if counter[i] > len(words)-1:
            for key in keys:
                if key['id'] == i:
                    print(key)
                    filtered_keys.append(key)
                    break
    # logger.error(*words)
    return JsonResponse(filtered_keys, safe=False, json_dumps_params={'ensure_ascii': False})

# def keys_by_name(request, key_name):
#     # find product by name
#     parsed = uri_to_iri(key_name)
#     words = parsed.split('+')
#     keys = []
    
#     try:
#         keys_serializer = KeySerializers(Key.objects.filter(transformed_name__icontains = words, many=True))
#     except:
#         pass

#     # counter = Counter(map(lambda x:x['id'], keys))
#     # filtered_keys = []
#     # for i in counter:
#     #     if counter[i] > len(words)-1:
#     #         for key in keys:
#     #             if key['id'] == i:
#     #                 print(key)
#     #                 filtered_keys.append(key)
#     #                 break
    
#     return JsonResponse(keys_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

# def keys_by_name(request, key_name):
#     # query transformed_names
#     keys = Key.objects.all()
#     transformed_key_name = []
#     for i, key in enumerate(keys):
#         transformed_key_name.append((i,key.transformed_name.lower()))
#     # find product by name
#     parsed = uri_to_iri(key_name)
#     words = transform_vn(parsed).lower().split('+')
#     res = []
#     for word in words:
#         for name_index in range(len(transformed_key_name)):
#             if word in transformed_key_name[name_index][1]:
#                 res.append(keys[transformed_key_name[name_index][0]])
#     try:
#         keys_serializer = KeySerializers(res, many=True)
#     except:
#         pass

#     counter = Counter(map(lambda x:x['id'], keys_serializer.data))
#     filtered_keys = []
#     for i in counter:
#         if counter[i] > len(words)-1:
#             for key in keys_serializer.data:
#                 if key['id'] == i:
#                     print(key)
#                     filtered_keys.append(key)
#                     break
    
#     return JsonResponse(filtered_keys, safe=False, json_dumps_params={'ensure_ascii': False})

def keys_hot(request, key_name):
    # find product by name
    parsed = uri_to_iri(key_name).replace('+',' ')
    keys_hot = Key.objects.filter(name__icontains = parsed)
    try:
        keys_serializer = KeySerializers(Key.objects.filter(name__icontains = parsed), many=True)
        return JsonResponse(keys_serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    except keys_hot.DoesNotExist:
        return JsonResponse({'message': 'Sai bỏ mẹ rồi'}, status=status.HTTP_404_NOT_FOUND) 
    
    