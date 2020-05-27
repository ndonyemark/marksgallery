from django.test import TestCase
from .models import Category, Image, Location

# Create your tests here.

class CategoryTestCase(TestCase):

    def setUp(self):
        self.image_category = Category(category = 'hawaii')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image_category, Category))
    
    def test_save_method(self):
        self.image_category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
    
    def test_delete_method(self):
        self.image_category.save_category()
        categories = Category.objects.all()
        self.image_category.delete_category()
        self.assertTrue(len(categories) < 1)

class LocationTestCase(TestCase):
    
    def setUp(self):
        self.image_location = Location(image_location = 'localhost')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.image_location, Location))
    
    def test_save_method(self):
        self.image_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)
    
    def test_delete_method(self):
        self.image_location.save_location()
        location = Location.objects.all()
        self.image_location.delete_location()
        self.assertTrue(len(location) < 1)

# class ImageTestCase(TestCase):

#     def setUp(self):
#         self.image_instance = Image(image_name = "The summer holiday", image_description = "The best summer holiday I ever had", image_location = Image.image_location.image_location, image_category = Image.image_category.category)
    
#     def test_instance(self):
#         self.assertTrue(isinstance(self.image_instance, Image))