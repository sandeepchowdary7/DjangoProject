from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist


def perform_create(serializer):
    serializer.save()


class CreateView(generics.ListCreateAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
