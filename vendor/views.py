from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vendor
from .serializers import VendorSerializer


class VendorListCreateAPIView(APIView):

    def get(self, request):
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VendorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VendorDetailAPIView(APIView):

    def get(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)

    def put(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        serializer = VendorSerializer(vendor, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request, pk):
        vendor = Vendor.objects.get(pk=pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)