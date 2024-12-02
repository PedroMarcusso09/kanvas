from rest_framework.exceptions import NotFound
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from contents.serializers import ContentSerializer
from courses.models import Course
from .models import Content
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAdminUser, IsOwnerOrAdmin
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema_view(
    post=extend_schema(
        tags=['Conteúdos'],
        summary='Criar conteúdo para um curso',
        description='Cria um novo conteúdo associado a um curso específico. Apenas super usuários têm permissão para criar conteúdos'
    )
)
class ContentCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'course_id'

    def perform_create(self, serializer):
        course = get_object_or_404(Course, id=self.kwargs['course_id'])
        serializer.save(course=course)


@extend_schema_view(
    get=extend_schema(
        tags=['Conteúdos'],
        summary='Obter detalhes de um conteúdo',
        description='Retorna as informações detalhadas de um conteúdo associado a um curso.'
    ),
    patch=extend_schema(
        tags=['Conteúdos'],
        summary='Atualização somente do conteúdo',
        description='Atualiza o conteúdo desejado.'
    ),
    delete=extend_schema(
        tags=['Conteúdos'],
        summary='Excluir conteúdo',
        description='Exclui um conteúdo específico associado a um curso. Apenas o proprietário ou um administrador pode realizar esta operação.'
    )
)
class ContentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'content_id'

    http_method_names = ['get', 'patch', 'delete']

    def get_object(self):
        course_exists = Course.objects.filter(
            id=self.kwargs['course_id']).exists()
        if not course_exists:
            raise NotFound(detail='course not found.')      
        try:
            return super().get_object()
        except Http404:
            raise NotFound(detail='content not found.')
