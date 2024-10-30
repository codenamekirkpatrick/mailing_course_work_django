from django.views.decorators.cache import cache_page

# from mailing.views import HomePageView, ContactsView, ProductListView, ProductDetailView, ProductCreateView, \
#     ProductUpdateView, ProductDeleteView, CategoryListView

from django.urls import path
from mailing.apps import MailingConfig


app_name = MailingConfig.name


# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),
#     path('contacts/', ContactsView.as_view(), name='contacts'),
#     path('catalog/', ProductListView.as_view(), name='product_list'),
#     path('catalog/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
#     path('catalog/create/', ProductCreateView.as_view(), name='product_create'),
#     path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
#     path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
#     path('category/', CategoryListView.as_view(), name='category_list'),