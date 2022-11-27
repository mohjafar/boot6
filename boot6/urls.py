from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('single/<int:id>',views.single),
    path('login/',views.loginPage),
    path('logout/',views.logoutPage),
    path('signup/',views.signup),
    path('profile/',views.profile),
    path('update-profile/',views.updateProfilePage),
    path('add-to-cart/<int:id>/',views.addToCart),
    path('cart/',views.cartPage),
    path('delete-cart/<int:pid>',views.deleteCart),
    path('update-cart/<int:pid>/<str:op>/',views.updateCart),
    path('add-to-wishlist/<int:pid>/',views.addToWishlist),
    path('delete-wishlist/<int:pid>/',views.deleteWishlist),
    path('checkout/',views.checkoutPage),
    path('order/',views.orderPage),
    path('confirmation/',views.confirmationPage),
    path('contact/',views.contactPage),
    path('search/',views.searchPage),
    path('forget-username/',views.forgetUsername),
    path('forget-otp/',views.forgetOTP),
    path('forget-password/',views.forgetPassword),
    path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/',views.paymentSuccess),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
