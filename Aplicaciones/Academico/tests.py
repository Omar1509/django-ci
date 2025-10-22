from django.test import TestCase
from .models import Curso

class CursoTestCase(TestCase):
    def test_creacion_curso(self):
        curso = Curso.objects.create(nombre="Matemáticas", descripcion="Curso básico")
        self.assertEqual(curso.nombre, "Matemáticas")
