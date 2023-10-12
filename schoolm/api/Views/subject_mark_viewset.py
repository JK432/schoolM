# from rest_framework import viewsets, status
# from rest_framework.response import Response
# from ..models import Mark, Subject, User
# from ..Serializers import *
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import action
#
#
# def get_queryset(request):
#     user = request.user
#     return Mark.objects.filter(student=user)
#
#
# class SubjectViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated]
#
#     def list(self, request):
#
#         if request.user.is_superuser:
#             teacher = request.user
#             subjects = teacher.teacher_subjects.all()
#             subject_average_marks = []
#
#             for subject in subjects:
#                 marks = Mark.objects.filter(subject=subject)
#                 total_marks = sum(mark.mark for mark in marks)
#                 num_marks = marks.count()
#                 average_mark = total_marks / num_marks if num_marks > 0 else 0
#                 subject_average_marks.append({
#                     'subject_id': subject.id,
#                     'subject_name': subject.name,
#                     'average_mark': average_mark
#                 })
#
#             serializer = SubjectAverageMarkSerializer(subject_average_marks, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         if not request.user.is_superuser:
#             queryset = get_queryset(request)
#             serializer = SubjectMarkSerializer(queryset, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def create(self, request):
#         serializer = SubjectSerializer(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def update(self, request, pk=None):
#
#         try:
#             subject = Subject.objects.get(pk=pk)
#         except Subject.DoesNotExist:
#             return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         if not request.user.is_superuser and subject not in request.user.teacher_subjects.all():
#             return Response({"message": "You do not have permission to update this subject"}, status=status.HTTP_403_FORBIDDEN)
#
#         serializer = SubjectSerializer(subject, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk=None):
#         try:
#             subject = Subject.objects.get(pk=pk)
#         except Subject.DoesNotExist:
#             return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         if not request.user.is_superuser and subject not in request.user.teacher_subjects.all():
#             return Response({"message": "You do not have permission to delete this subject"},
#                             status=status.HTTP_403_FORBIDDEN)
#
#         subject.delete()
#         return Response({"message": "Subject deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#
#     @action(detail=True, methods=['post'])
#     def post_mark(self, request, pk=None):
#         try:
#             subject = Subject.objects.get(pk=pk)
#         except Subject.DoesNotExist:
#             return Response({"message": "Subject not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         if request.user not in subject.teachers.all():
#             return Response({"message": "You do not have permission to post marks for this subject"}, status=status.HTTP_403_FORBIDDEN)
#
#         student_id = request.data.get('student')
#         mark_value = request.data.get('mark')
#
#         try:
#             student = User.objects.get(id=student_id)
#         except User.DoesNotExist:
#             return Response({"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
#
#         if student not in subject.students.all():
#             return Response({"message": "Student is not enrolled in this subject"}, status=status.HTTP_400_BAD_REQUEST)
#
#         # Create a new mark entry
#         mark = Mark.objects.create(
#             mark=mark_value,
#             student=student,
#             subject=subject
#         )
#
#         serializer = StudentMarkSerializer(mark)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
