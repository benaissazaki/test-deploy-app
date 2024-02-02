from django.db import models
from PIL import Image
        

class CategoryInterface(models.Model):
    name            = models.CharField(max_length=60, null=False, blank=False, unique=True)
    image           = models.ImageField(upload_to="category/", null=False, blank=False)
    description     = models.CharField(max_length=255, null=True, blank=True)
    created_at      = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        This method comes into play when using queryset with forms.
        It's the attribute being queried there.
        """
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        """
        Overriding the save method to resize the images uploaded.
        """
        self.name = self.name.capitalize() if self.name else None
        self.description = self.description.capitalize() if self.description else None

        super(CategoryInterface, self).save(*args, **kwargs)

        SIZE = (500, 500)
        image = Image.open(self.image.path)
        category_image = image.resize(SIZE)
        category_image.save(self.image.path)
    
    class Meta:
        abstract = True


class TopCategory(CategoryInterface):
    class Meta:
        ordering = ['-created_at']    
    

class MidCategory(CategoryInterface):
    top_category = models.ForeignKey(TopCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
    

class BottomCategory(CategoryInterface): 
    mid_category = models.ForeignKey(MidCategory, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']    


class Product(models.Model):
    name                = models.CharField(max_length=60, null=False, blank=False)
    description         = models.CharField(max_length=255, null=True, blank=True)
    image               = models.ImageField(upload_to="product/", null=False, blank=False)
    price               = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    stock               = models.PositiveIntegerField(null=False, blank=False)
    created_at          = models.DateTimeField(auto_now_add=True)
    available           = models.BooleanField(default=True)

    top_category        = models.ForeignKey(TopCategory, on_delete=models.CASCADE, null=False, blank=False)
    mid_category        = models.ForeignKey(MidCategory, on_delete=models.CASCADE, null=False, blank=False)
    bottom_category     = models.ForeignKey(BottomCategory, on_delete=models.CASCADE, null=True, blank=True)

    def check_availabality(self) -> 'Product':
        """
        Check whether a product is still on sale.
        """
        if self.stock == 0:
            self.available = False
            self.save()
            return self
        return self

    def decrement_stock(self, quantity_sold: int) -> None:
        """
        Decrement a set of products by one after a sale.
        """
        self.stock -= quantity_sold
        self.save()

    def save(self, *args, **kwargs) -> None:
        """
        Overriding the save method to resize the images uploaded.
        """
        super(Product, self).save(*args, **kwargs)

        SIZE = (500, 500)
        image = Image.open(self.image.path)
        product_image = image.resize(SIZE)
        product_image.save(self.image.path)


class ProductImage(models.Model):
    extra_image = models.ImageField(upload_to='product/', null=False, blank=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    product     = models.ManyToManyField(Product, related_name='images')


class Follower(models.Model):
    first_name = models.CharField(max_length=60, null=False, blank=False)
    last_name  = models.CharField(max_length=60, null=False, blank=False)
    email      = models.EmailField(null=False, blank=False, unique=True)
    category   = models.CharField(max_length=60, null=False, blank=False)


class Purchase(models.Model):
    quantity = models.PositiveIntegerField(null=False, blank=False)
    date     = models.DateTimeField(auto_now_add=True)

    product  = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs) -> None:
        """
        Overriding the save method to update the 
        product stock upon client purchase.
        """
        self.product.decrement_stock(self.quantity)
        super(Purchase, self).save(*args, **kwargs)


class Collection(models.Model):
    seasons = (
        ('Winter', 'Winter'),
        ('Summer', 'Summer'),
        ('Spring', 'Spring'),
        ('Autumn', 'Autumn')
    )
    year    = models.IntegerField(null=False, blank=False)
    season  = models.CharField(choices=seasons, null=False, blank=False)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
