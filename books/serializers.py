from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_date')

    def get_is_recent(self, obj):
      return obj.publication_date > datetime.date.today() - datetime.timedelta(days=30)
