from rest_framework import serializers
from .models import ProductCourseMapping


class ProductCourseMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCourseMapping
        fields = '__all__'

    def validate(self, data):

        if data.get("primary_mapping"):

            product = data.get("product")

            if ProductCourseMapping.objects.filter(
                product=product,
                primary_mapping=True
            ).exists():

                raise serializers.ValidationError(
                    "This product already has a primary course mapping."
                )

        return data