from django.db import models

# Create your models here.
books = [{'id': 1, 'title': 'Fluent Python', 'released_year': 2015, 'description': 'Python’s simplicity lets you '
                                                                                   'become productive quickly, '
                                                                                   'but this often means you aren’t '
                                                                                   'using everything it has to offer. '
                                                                                   'With this hands-on guide, '
                                                                                   'you’ll learn how to write '
                                                                                   'effective, idiomatic Python code '
                                                                                   'by leveraging its best—and '
                                                                                   'possibly most neglected—features. '
                                                                                   'Author Luciano Ramalho takes you '
                                                                                   'through Python’s core language '
                                                                                   'features and libraries, '
                                                                                   'and shows you how to make your '
                                                                                   'code shorter, faster, '
                                                                                   'and more readable at the same '
                                                                                   'time.', 'author_id': 1},
         {'id': 2,
          'title': 'My title - Python',
          'released_year': 2022,
          'description': 'My description',
          'author_id': 2},
         {
             'id': 3,
             'title': 'Learn django',
             'released_year': 2022,
             'description': 'Django - pro', 'author_id': 1}]
authors = [{'id': 1, 'first_name': "Luciano", 'last_name': 'Ramalho', 'age': 51},
           {'id': 2, 'first_name': 'Puchino', 'last_name': 'Alpachino', 'age': 22}]


class Authors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    age = models.IntegerField()

    @staticmethod
    def create_author():
        for i in authors:
            author = Authors(first_name=i['first_name'], last_name=i['last_name'], id=i['id'], age=i['age'])
            author.save()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Books(models.Model):
    title = models.CharField(max_length=100)
    released_year = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    author_id = models.ForeignKey(Authors, on_delete=models.CASCADE)
    description = models.TextField()

    @staticmethod
    def create_book():
        for i in books:
            book = Books(title=i['title'], released_year=i['released_year'], id=i['id'], author_id=Authors.objects.get(id=i['author_id']),
                         description=i['description'])
            book.save()

    def __str__(self):
        return f'{self.title}'

class Profile(models.Model):
    tel = models.CharField(max_length=10)
    author = models.OneToOneField(Authors, on_delete=models.SET_NULL, blank=True, null=True)


class Member(models.Model):
    nickname = models.CharField(max_length=100)
