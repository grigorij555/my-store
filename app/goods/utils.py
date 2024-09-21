from django.db.models import Q

from goods.models import Products

def q_search(query):
   
   if query.isdigit() and len(query)<=5:
       return Products.objects.filter(id=int(query))