from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1=User.objects.create_user(
            username='omen', password='0010'
        )
        testuser1.save()

        test_post=Post.objects.create(
            author=testuser1, title="Blog title",  content="Body content..."
        )
        test_post.save()


    def test_blog_content(self):
        post=Post.objects.get(id=1)
        author=f"{post.author}"
        title=f"{post.title}"
        content=f"{post.content}"
        
        self.assertEqual(author, 'omen')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(content, 'Body content')