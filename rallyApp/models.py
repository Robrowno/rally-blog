from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

POST_STATUS = ((0, "Draft"), (1, "Published"))
FINISH = ((0, "DNF"), (1, "Finished"))
QUERY_TYPE = ((0, "Question"), (1, "Sponsorship"), (2, "Other"))


class Post(models.Model):
    """
    A class for my Rally Blog Application that stores
    variable names with field types for my blog posts.
    """
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=40, default="Christian Brown")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    eventName = models.CharField(max_length=150)
    associated_club = models.CharField(max_length=200)
    entry_fee = models.FloatField(blank=True)
    location = models.CharField(max_length=220, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    car = models.CharField(max_length=150)
    finish = models.BooleanField(choices=FINISH, default=0)
    class_result = models.PositiveIntegerField()
    overall_result = models.PositiveIntegerField()
    championship_result = models.PositiveIntegerField()
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    comments = models.ManyToManyField(User, related_name="post_comments", blank=True)
    shares = models.ManyToManyField(User, related_name="post_shares", blank=True)
    post_status = models.BooleanField(choices=POST_STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    A class that handles the comments section within each post.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments_section")
    name = models.CharField(max_length=70, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField(blank=False, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"



class Contact(models.Model):

    """ A class that handles the contact information fields
    that refer to the contact.html page """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    query_type = models.BooleanField(choices=QUERY_TYPE, default=0)
    textbox = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-contacted_on']

    def __str__(self):
        return f"{self.first_name} {self.last_name} contacted you."
