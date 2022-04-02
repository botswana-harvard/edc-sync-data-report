from rest_framework import serializers

from edc_sync_data_report.models import ClientSyncSummary


class ClientSyncSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSyncSummary
        fields = ['name', 'data', 'created_date']