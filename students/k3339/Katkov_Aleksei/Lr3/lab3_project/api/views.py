from rest_framework import generics
from .models import Category, Task
from .serializers import (
    CategorySerializer,
    TaskSerializer,
    TaskNestedSerializer,
    CategoryNestedSerializer,
)
from rest_framework.permissions import IsAuthenticated


# ---------- CATEGORY ----------

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryWithTasksView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryNestedSerializer
    permission_classes = [IsAuthenticated]


# ---------- TASK ----------

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get("status")
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


class TaskFullInfoView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskNestedSerializer
    permission_classes = [IsAuthenticated]
