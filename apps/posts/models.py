from django.db.models.signals import pre_save
from django.utils import timezone
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User',default=1, on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank = True, unique = True )
    image = models.ImageField(upload_to='blog-img/', null = True, blank = True, default = 'default.jpg')
    text = RichTextUploadingField()
    published_date = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title



    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug':self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)