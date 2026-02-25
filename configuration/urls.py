from django.urls import path
from configuration.views import ConfigurationListView, ConfigurationCreateView, ConfigurationRebuildView, ConfigurationUpdateView, ConfigurationDeleteView, ConfigurationDetailView, ConfigurationListOrganisationView, ConfigurationListUserView
from configuration.views.graph_presets import (
    GraphPresetsListView, GraphPresetsUpdateView, GraphPresetsResetView,
    GraphPresetsRoleUpdateView, GraphPresetsLayerUpdateView, GraphPresetsAutoMapView
)


urlpatterns = [
    path('configuration/list/', ConfigurationListView.as_view(), name='configuration_list'),
    path('configuration/list/<int:user_id>/', ConfigurationListUserView.as_view(), name='configuration_list_user'),
    path('configuration/list/<uuid:organisation_id>/', ConfigurationListOrganisationView.as_view(), name='configuration_list_organisation'),
    path('configuration/create/<int:user_id>/', ConfigurationCreateView.as_view(), name='configuration_create_user'),
    path('configuration/create/<uuid:organisation_id>/', ConfigurationCreateView.as_view(), name='configuration_create'),
    path('configuration/detail/<uuid:pk>/', ConfigurationDetailView.as_view(), name='configuration_detail'),
    path('configuration/update/<uuid:pk>/', ConfigurationUpdateView.as_view(), name='configuration_update'),
    path('configuration/delete/<uuid:pk>/', ConfigurationDeleteView.as_view(), name='configuration_delete'),

    path('configuration/rebuild/<uuid:organisation_id>/', ConfigurationRebuildView.as_view(), name='configuration_rebuild'),

    # Graph presets configuration
    path('configuration/graph_presets/<uuid:organisation_id>/', GraphPresetsListView.as_view(), name='graph_presets_list'),
    path('configuration/graph_presets/<uuid:organisation_id>/update/', GraphPresetsUpdateView.as_view(), name='graph_presets_update'),
    path('configuration/graph_presets/<uuid:organisation_id>/reset/', GraphPresetsResetView.as_view(), name='graph_presets_reset'),
    path('configuration/graph_presets/<uuid:organisation_id>/role/<str:role_id>/', GraphPresetsRoleUpdateView.as_view(), name='graph_presets_role_update'),
    path('configuration/graph_presets/<uuid:organisation_id>/layer/<str:layer_id>/', GraphPresetsLayerUpdateView.as_view(), name='graph_presets_layer_update'),
    path('configuration/graph_presets/<uuid:organisation_id>/auto_map/<uuid:model_id>/', GraphPresetsAutoMapView.as_view(), name='graph_presets_auto_map'),
]