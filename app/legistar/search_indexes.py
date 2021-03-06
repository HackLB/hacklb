import datetime
from haystack import indexes
import legistar.models


class BodyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    name = indexes.CharField(model_attr='name', null=True, )

    def get_model(self):
        return legistar.models.Body

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class DocumentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    name = indexes.CharField(model_attr='name', null=True, )

    def get_model(self):
        return legistar.models.Document

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class MeetingIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    name = indexes.CharField(model_attr='name', null=True, )

    def get_model(self):
        return legistar.models.Meeting

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class AgendaItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    name = indexes.CharField(model_attr='name', null=True, )

    def get_model(self):
        return legistar.models.AgendaItem

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()