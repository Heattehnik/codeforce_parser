from django.test import TestCase
from users.models import User
from main.models import Problem, Theme


class ProblemCRUDTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email='test@example.com',
                                        password='testpassword')
        self.theme = Theme.objects.create(theme='Test Theme')

    def test_create_problem(self):
        problem_data = {
            'contest_id': 1,
            'index': 'F',
            'title': 'Something',
            'solve_count': 1000,
            'difficulty': 1500,
        }
        theme = Theme.objects.filter(theme__in=[self.theme])
        problem = Problem.objects.create(**problem_data)
        problem.theme.set(theme)
        self.assertEqual(Problem.objects.count(), 1)

    def test_read_problem(self):
        problem_data = {
            'contest_id': 1,
            'index': 'F',
            'title': 'Something else',
            'solve_count': 2000,
            'difficulty': 3000,
        }
        theme = Theme.objects.filter(theme__in=[self.theme])
        problem = Problem.objects.create(**problem_data)
        problem.theme.set(theme)
        read_problem = Problem.objects.get(id=problem.id)
        self.assertEqual(read_problem.title, 'Something else')

    def test_update_problem(self):
        problem_data = {
            'contest_id': 1,
            'index': 'F',
            'title': 'Something',
            'solve_count': 1000,
            'difficulty': 1500,
        }
        theme = Theme.objects.filter(theme__in=[self.theme])
        problem = Problem.objects.create(**problem_data)
        problem.theme.set(theme)
        problem.title = 'Super title'
        problem.save()
        updated_problem = Problem.objects.get(id=problem.id)
        self.assertEqual(updated_problem.title, 'Super title')

    def test_delete_habit(self):
        problem_data = {
            'contest_id': 1,
            'index': 'F',
            'title': 'Something',
            'solve_count': 1000,
            'difficulty': 1500,
        }
        theme = Theme.objects.filter(theme__in=[self.theme])
        problem = Problem.objects.create(**problem_data)
        problem.theme.set(theme)
        problem.delete()
        self.assertEqual(Problem.objects.count(), 0)
