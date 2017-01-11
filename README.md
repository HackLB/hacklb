# hacklb


http://stackoverflow.com/questions/19703975/django-sort-by-distance


from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
p = Parcel.objects.first()

Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[0]