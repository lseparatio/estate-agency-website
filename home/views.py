from django.shortcuts import render
from store.models import Product, Category, Subcategory

# Create your views here.


from accounts.forms import CustomSignupForm
from accounts.forms import CustomLoginForm

sales_category = Category.objects.get(name="sales")
sales_products = Product.objects.all().filter(category=sales_category)
lettings_category = Category.objects.get(name="lettings")
lets_products = Product.objects.all().filter(category=lettings_category)
holiday_lets_category = Category.objects.get(name="holiday_lets")
holiday_lets_products = Product.objects.all().filter(category=holiday_lets_category)

form_singup = CustomSignupForm()
form_login = CustomLoginForm()



def index(request):
    """A view to return the index page"""


    context = {
        'form': form_singup,
        'form_login': form_login,
        'sales_products' : sales_products,
        'lets_products' : lets_products,
        'holiday_lets_products' : holiday_lets_products
    }

    return render(request, 'home/index.html', context)
