import datetime
from haystack import indexes
import geographic.models


class DatasetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    title = indexes.CharField(model_attr='title', null=True, )

    def get_model(self):
        return geographic.models.Dataset

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
