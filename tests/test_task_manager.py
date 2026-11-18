import unittest
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task('Study Git')
        self.assertEqual(task['title'], 'Study Git')
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task('Finish lab')
        self.assertTrue(self.manager.complete_task(task['id']))
        self.assertTrue(self.manager.list_tasks()[0]['completed'])

    def test_delete_task(self):
        task = self.manager.add_task('Remove me')
        self.assertTrue(self.manager.delete_task(task['id']))
        self.assertEqual(self.manager.list_tasks(), [])

    def test_empty_title_rejected(self):
        with self.assertRaises(ValueError):
            self.manager.add_task('   ')


if __name__ == '__main__':
    unittest.main()
