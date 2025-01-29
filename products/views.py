
from django.shortcuts import render
from .models import Product
from django.views.generic.list import ListView
from sabad.forms import NewsabadForm
from django.shortcuts import render, get_object_or_404




def product_view(request):

    products=Product.objects.all()
    context={

    'products_list':products

    }
    return render(request,'product_list.html',context)


class ProductsView(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'

    def get_context_data(self,*args,object_list=None,**kwargs):
        context=super(ProductsView,self).get_context_data(*args,**kwargs)
        return context








def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    new_sabad_form = NewsabadForm(request.POST or None, initial={'product_id': product_id})
    context = {
        'product': product,
        'new_sabad_form': new_sabad_form
    }

    return render(request, 'product_detail.html', context)
