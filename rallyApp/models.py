from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django_extensions.db.fields import AutoSlugField

POST_STATUS = ((0, "Draft"), (1, "Published"))
FINISH = ((0, "DNF"), (1, "Finished"))
QUERY_TYPE = ((0, "Question"), (1, "Sponsorship"), (2, "Other"))


class Post(models.Model):
    """
    A class for my Rally Blog Application that stores
    variable names with field types for my blog posts.
    """
    title = models.CharField(max_length=150)
    slug = AutoSlugField(max_length=150, populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    event_name = models.CharField(max_length=150)
    associated_club = models.CharField(max_length=200, null=True, blank=True)
    entry_fee = models.FloatField(null=True, blank=True)
    location = models.CharField(max_length=220, blank=True)
    content = models.TextField()
    featured_image = CloudinaryField(
        'image', default='placeholder', null=False
        )
    car = models.CharField(max_length=150)
    finish = models.BooleanField(choices=FINISH, default=0)
    class_result = models.PositiveIntegerField(null=True, blank=True)
    overall_result = models.PositiveIntegerField(null=True, blank=True)
    championship_result = models.PositiveIntegerField(null=True, blank=True)
    likes = models.ManyToManyField(
        User,  related_name="post_likes", blank=True
        )
    comments = models.ManyToManyField(
        User, related_name="post_comments", blank=True
        )
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

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments_section"
        )
    name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    email = models.EmailField(blank=True, null=True)
    body = models.TextField(blank=False, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Like(models.Model):
    """
    A class to handle liking a post.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction = models.CharField(default='Liked', max_length=10)
    reacted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-reacted_on']

    def __str__(self):
        return f"{self.user} liked your post: {self.post}"


class Contact(models.Model):

    """ A class that handles the contact information fields
    that refer to the contact.html page """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField()
    query_type = models.CharField(max_length=11, choices=QUERY_TYPE, default=0)
    textbox = models.TextField()
    contacted_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-contacted_on']

    def __str__(self):
        return f"{self.first_name} {self.last_name} contacted you."


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
