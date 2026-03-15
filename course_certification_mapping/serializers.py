from rest_framework import serializers
from .models import CourseCertificationMapping


class CourseCertificationMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseCertificationMapping
        fields = '__all__'

    def validate(self, data):

        if data.get("primary_mapping"):

            course = data.get("course")

            if CourseCertificationMapping.objects.filter(
                course=course,
                primary_mapping=True
            ).exists():

                raise serializers.ValidationError(
                    "This course already has a primary certification mapping."
                )

        return data