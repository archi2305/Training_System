from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductCourseMapping
from .serializers import ProductCourseMappingSerializer


class ProductCourseMappingListCreateAPIView(APIView):

    def get(self, request):
        mappings = ProductCourseMapping.objects.all()
        serializer = ProductCourseMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductCourseMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCourseMappingDetailAPIView(APIView):

    def get(self, request, pk):
        mapping = ProductCourseMapping.objects.get(pk=pk)
        serializer = ProductCourseMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, pk):
        mapping = ProductCourseMapping.objects.get(pk=pk)
        serializer = ProductCourseMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        mapping = ProductCourseMapping.objects.get(pk=pk)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)