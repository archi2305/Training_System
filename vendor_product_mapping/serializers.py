from rest_framework import serializers
from .models import VendorProductMapping


class VendorProductMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = VendorProductMapping
        fields = '__all__'

    def validate(self, data):

        if data.get("primary_mapping"):

            vendor = data.get("vendor")

            if VendorProductMapping.objects.filter(
                vendor=vendor,
                primary_mapping=True
            ).exists():

                raise serializers.ValidationError(
                    "This vendor already has a primary product mapping."
                )

        return data