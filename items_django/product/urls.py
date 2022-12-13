from django.urls import path, include 

from product import views

urlpatterns = [
  path('latest-products/', views.LatestProductsList.as_view()),
  path('recomendation-products/<int:input_id>', views.RecomendationList.as_view()),
  path('products/search/', views.search),
  path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
  path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
  path('products2/<str:username>/<int:input_id>/', views.TetsDetails.as_view()),
  path('addreview/', views.addReview,name='addReview' )
]