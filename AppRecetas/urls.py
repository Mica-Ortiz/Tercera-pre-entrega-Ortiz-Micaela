from django.urls import path
from AppRecetas import views, class_views

##ver urls viejos

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('categorias/', views.categorias, name="Categorías"),
    path('comentarios/', views.comentarios, name="Comentarios"),
    path('formulario_receta/',views.RecetaFormulario, name="Formulario-Receta"),
    path('formulario_categoria/',views.CategoriaFormulario, name="Formulario-Categoría"),
    path('formulario_usuario/',views.UsuarioFormulario, name="Formulario-Usuario"),
    path('busqueda_receta/',views.BusquedaReceta, name="Formulario-Buscar-Receta"),
    path('busqueda_categoria/',views.BusquedaCategoria, name="Formulario-Buscar-Categoria"),
    path('busqueda_usuario/',views.BusquedaUsuario, name="Formulario-Buscar-Usuario")
]

urlpatterns += [
    path('recetas-list/', class_views.RecetaListView.as_view(), name="Recetas"),
    path('recetas-detalle/<pk>/', class_views.RecetaDetailView.as_view(), name="Detalle"),
    path('recetas-crear/', class_views.RecetaCreateView.as_view(), name="Crear"),
    path('recetas-update/<pk>/', class_views.RecetaUpdateView.as_view(), name="Update"),
    path('recetas-delete/<pk>/', class_views.RecetaDeleteView.as_view(), name="Delete"),
    path('categorias-crear/', class_views.CategoriaCreateView.as_view(), name="CrearC"),
    path('categorias-list/', class_views.CategoriaListView.as_view(), name="Categorias"),
    path('categorias-update/<pk>/', class_views.CategoriaUpdateView.as_view(), name="UpdateC"),
     path('categorias-delete/<pk>/', class_views.CategoriaDeleteView.as_view(), name="DeleteC"),
]