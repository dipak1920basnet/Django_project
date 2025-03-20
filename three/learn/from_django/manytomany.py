from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publication = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline

p1 = Publication(title = "The python Journal")

p1.save()

p2 = Publication(title = "Science News")

p2.save()

p3 = Publication(title="Science Weekly")

p3.save()

a1 = Article(headline = "Django lets you build web apps easily")

a1.save()

a1.publication.add(p1)

a2 = Article(headline="NASA uses Python")

a2.save()
a2.publication.add(p1,p2)

a2.publication.add(p3)