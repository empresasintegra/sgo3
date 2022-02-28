"""Contratos urls."""

# Django
from django.urls import path
from django.contrib.auth import views as auth_views
from contratos import views


urlpatterns = [
    path(
        route='plantilla/list/',
        view=views.PlantillaListView.as_view(),
        name="list-plantilla"
    ),
    path(
        route='plantilla/create/',
        view=views.create_plantilla,
        name="create-plantilla"
    ),
    path(
        route='<int:plantilla_id>/plantilla/update/',
        view=views.update_plantilla,
        name="update-plantilla"
    ),
    path(
        route='<int:object_id>/plantilla/delete/',
        view=views.delete_plantilla,
        name="delete-plantilla"
    ),
    path(
        route='list/',
        view=views.ContratoListView.as_view(),
        name="list"
    ),
    path(
        route='create/',
        view=views.create,
        name="create"
    ),
    # path(
    #     route='<int:requerimiento_id>/create_requerimiento',
    #     view=views.RequerimientoIdView.as_view(),
    #     name='create_requerimiento'
    # ),
    path(
        # route='<int:requerimiento_user_id>/create_contrato/',
        route='<int:requerimiento_user_id>/create_contrato/',
        view=views.ContratoIdView.as_view(),
        name="create_contrato"
    ),
    path(
        route='miscontratos/',
        view=views.ContratoMis.as_view(),
        name="miscontratos"
    ),
    path(
        route='<int:pk>/detail/',
        view=views.ContratoDetailView.as_view(),
        name="detail"
    ),
    path(
        route='<int:contrato_id>/generar_firma/',
        view=views.generar_firma_contrato,
        name='generar_firma'
    ),
    path(
        route='<int:id>/firmar/',
        view=views.ContratoFirmarView.as_view(),
        name='firmar'
    ),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(
        route='<slug:id>/generar_firma/firmarr/',
        view=auth_views.PasswordResetDoneView.as_view(),
        name='generar_firma_done'
    ),
    
]
