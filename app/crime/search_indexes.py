import datetime
from haystack import indexes
import crime.models


class IncidentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, )
    name = indexes.CharField(model_attr='name', null=True, )

    def get_model(self):
        return crime.models.Incident

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
