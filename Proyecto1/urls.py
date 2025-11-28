from django.contrib import admin
from django.urls import path
from mascoteros import views
from mascoteros.views import AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('registro/', views.registro, name="registro"),
    path('mascota/', views.mascota, name="mascota"),
    path('estadia/', views.estadia, name="estadia"),
    path('estadia/<int:id_estadia>/', views.estadia, name="modificar_estadia"),
    path('estadia/eliminar/<int:id_estadia>/', views.eliminar_estadia, name='eliminar_estadia'),
    path('about/', AboutView.as_view(), name="about"),
    path('editar_dueño/<int:pk>/', views.editar_dueño, name="editar_dueño"),
    path('eliminar_dueño/<int:pk>/', views.eliminar_dueño, name="eliminar_dueño"),
    path('mascota/modificar/<int:mascota_id>/', views.mascota, name="modificar_mascota"),
    path('mascota/eliminar/<int:mascota_id>/', views.eliminar_mascota, name="eliminar_mascota"),
]
