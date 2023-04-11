from django.test import TestCase
from django.urls import reverse
from . models import Book

# Create your tests here.

class BookTests(TestCase):
    """Tests for the books app"""
    @classmethod
    def setUpTestData(cls):
        """set test dummy data"""
        cls.book = Book.objects.create(
            title="A good title",
            subtitle="An excellent subtitle",
            author="Tom Christie",
            isbn="1234567890123",
        )

    def test_book_content(self):
        """test that book content equals dummy data"""
        self.assertEqual(self.book.title,"A good title")
        self.assertEqual(self.book.subtitle,"An excellent subtitle")
        self.assertEqual(self.book.author,"Tom Christie")
        self.assertEqual(self.book.isbn,"1234567890123")

    def test_book_listview(self):
        """test various bookListView parameters"""
        response=self.client.get(reverse("home"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"An excellent subtitle")
        self.assertTemplateUsed(response,"books/book_list.html")



