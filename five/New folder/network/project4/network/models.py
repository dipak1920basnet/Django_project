from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class User(AbstractUser):
    pass

#Create a post
class Create_posting(models.Model):

    post_creator = models.ForeignKey(User,on_delete=models.CASCADE, related_name="post_creator")
    post = models.CharField(max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)

    def serialize(self):
        return {
            "post_creator":self.post_creator,
            "post":self.post,
            "timestamp":self.timestamp,
        }
    
    def __str__(self):
        return f"{self.id} {self.post}"

#Give a like
class Like(models.Model):

    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liker")
    on_post = models.ForeignKey(Create_posting, on_delete=models.CASCADE, related_name="on_post")

    def serialize(self):
        return {"liker":self.liker,
        "on_post":self.on_post,
        }

    def __str__(self):
        return f"{self.id} {self.liker} liked {self.on_post}"

class Followers(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name="following_user", blank=True, null=True)
    follower = models.ForeignKey(User, on_delete=models.CASCADE,related_name="followed_user", blank=True, null=True)

    class Meta:
        unique_together = ["user","follower"]

    def clean(self):
        if self.user == self.follower:
            raise ValidationError("A user cannot follow themselves")
        
    def serialize(self):
        return {
            "user":self.user,
            "follower":self.follower,
        }
        
    def __str__(self):
        return f"{self.user} is followed by {self.follower}"
    

# Make a comment
class Comment(models.Model):

    comment_maker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_maker") ## Connect this with user
    comment_made_on_post = models.ForeignKey(Create_posting, on_delete=models.CASCADE, related_name="comment_made_on_post") ## Connect this with post
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.comment}"

