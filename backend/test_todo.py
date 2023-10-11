import unittest
import json
from flask import url_for
from __init__ import create_app
from config import TestConfig
from database import db

app = create_app(TestConfig)
app.config['SERVER_NAME'] = 'localhost:5000'
app.config['APPLICATION_ROOT'] = '/'  # Set the application root if needed
app.config['PREFERRED_URL_SCHEME'] = 'http'  # Set the preferred URL scheme (e.g., 'http' or 'https')

class TodoAppTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_create_and_get_todo_item(self):
        with self.client:
             # Create a test todo item
            data = {
                'title': 'Buy groceries',
                'is_complete': True
            }
            response = self.client.post(url_for('todo.create_todo'), json=data)
            self.assertEqual(response.status_code, 201)

            # Get the created todo item
            response = self.client.get(url_for('todo.get_todos', todo_id=1))
            self.assertEqual(response.status_code, 200)

            todo_item = json.loads(response.data)
            self.assertEqual(todo_item[0]['title'], data['title'])
            self.assertEqual(todo_item[0]['is_complete'], data['is_complete'])


    def test_create_item(self):
        with self.client:
            data = {
                'title': 'Buy groceries',
                'is_complete': True
            }
            response = self.client.post(url_for('todo.create_todo'), json=data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('title'), 'Buy groceries')
            self.assertEqual(data.get('is_complete'), True)
            self.assertNotEqual(data.get('title'), 'Banana')
            self.assertNotEqual(data.get('is_complete'), False)

if __name__ == '__main__':
    unittest.main()
    