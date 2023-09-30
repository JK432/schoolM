from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Mark, Subject
from ..Serializers import SubjectAverageMarkSerializer, SubjectSerializer
from rest_framework.permissions import IsAuthenticated
from ..Permissions import IsSuperUser


class TeacherSubjectAverageMarkViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]

    def list(self, request):
        teacher = request.user
        subjects = teacher.teacher_subjects.all()
        subject_average_marks = []

        for subject in subjects:
            marks = Mark.objects.filter(subject=subject)
            total_marks = sum(mark.mark for mark in marks)
            num_marks = marks.count()
            average_mark = total_marks / num_marks if num_marks > 0 else 0
            subject_average_marks.append({
                'subject_id': subject.id,
                'subject_name': subject.name,
                'average_mark': average_mark
            })

        serializer = SubjectAverageMarkSerializer(subject_average_marks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)