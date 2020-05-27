from django.db import models

# Create your models here.

class Location(models.Model):
    image_location = models.CharField(max_length = 30)

    def save_location(self):
        self.save()
    
    def delete_location(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

class Image(models.Model):
    image_name = models.CharField(max_length = 30)
    image_description = models.CharField(max_length = 30)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ManyToManyField(Category)
    date_posted = models.DateTimeField(auto_now_add=True)
    image_url = models.ImageField(upload_to = 'snaps/', default = "image url")

    class Meta:
        ordering = ['date_posted']

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_single_image(cls, image_id):
        single_image = cls.objects.get(id = image_id)
        return single_image

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images
    
    @classmethod
    def filter_by_location(cls, location):
        image_location = cls.objects.filter(image_location__icontains = location)
        return location
    
    @classmethod
    def search_by_category(cls, search_term):
        search_results = Image.objects.filter(image_name__icontains = search_term)
        return search_results
            
    # @classmethod
    # def update_image_url(cls, image_id):
    #     update_image_url = cls.objects.filter(id = image_id).update(image_url)

