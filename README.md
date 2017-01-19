# hacklb


http://stackoverflow.com/questions/19703975/django-sort-by-distance


from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
p = Parcel.objects.first()

Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[0]





>>> Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')
<QuerySet [<Feature: LIVINGSTON DRIVE, park (feature)>, <Feature: BAYSHORE PLAYGROUND, park (feature)>, <Feature: LEEWAY SAILING CENTER, park (feature)>, <Feature: MARINE STADIUM, park (feature)>, <Feature: WILL ROGERS, park (feature)>, <Feature: BELMONT POOL COMPLEX, park (feature)>, <Feature: MARINA VISTA, park (feature)>, <Feature: TREASURE ISLAND, park (feature)>, <Feature: LA BELLA FONTANA DI NAPOLI, park (feature)>, <Feature: BELMONT PIER AND PLAZA, park (feature)>, <Feature: ALAMITOS HEIGHTS, park (feature)>, <Feature: THE COLONNADE, park (feature)>, <Feature: COLORADO LAGOON, park (feature)>, <Feature: MARINE PARK (MOTHER'S BEACH), park (feature)>, <Feature: JACK DUNSTER MARINE RESERVE, park (feature)>, <Feature: TROLLEY, park (feature)>, <Feature: JACK NICHOL, park (feature)>, <Feature: OVERLOOK, park (feature)>, <Feature: SIMS POND, park (feature)>, <Feature: RECREATION, park (feature)>, '...(remaining elements truncated)...']>
>>> Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[0]
<Feature: LIVINGSTON DRIVE, park (feature)>
>>> f = Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[0]
>>> f.distance
Distance(m=408.15396297)
>>> Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[2].distance
Distance(m=837.55337369)
>>> Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[3].distance
Distance(m=990.16340418)
>>> 
>>> Feature.objects.filter(feature_type='park').filter(coordinates__distance_lte=(belmont, D(m=5000))).annotate(distance=Distance('coordinates', belmont)).order_by('distance')[3].distance
Distance(m=990.16340418)
>>> Feature.objects.filter(feature_type='park').annotate(distance=Distance('coordinates', belmont)).order_by('distance')[3].distance
Distance(m=990.16340418)
>>> Feature.objects.filter(feature_type='park').annotate(distance=Distance('coordinates', belmont)).order_by('distance').first().distance
Distance(m=408.15396297)
>>> p = Parcel.objects.first()
>>> p
<Parcel: 0000881f-f50f-4182-99d2-aed032539e3c parcel>
>>> dir(p)
['DoesNotExist', 'Meta', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes', '_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model', '_check_ordering', '_check_swappable', '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', '_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'check', 'clean', 'clean_fields', 'coordinates', 'date_error_message', 'datetime_created', 'datetime_updated', 'delete', 'description', 'from_db', 'full_clean', 'geojson', 'get_absolute_url', 'get_deferred_fields', 'id', 'json', 'lat', 'lon', 'objectid', 'objects', 'pk', 'polygon', 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'source_url', 'title', 'unique_error_message', 'validate_unique']
>>> p.location
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Parcel' object has no attribute 'location'
>>> p.coordinates
<Point object at 0x108326808>
>>> p.coordinates.geojson
'{"type": "Point", "coordinates": [-118.21944726544417, 33.81139349625535]}'
>>> p.nearest('park')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Parcel' object has no attribute 'nearest'
>>> 
now exiting InteractiveConsole...
 ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                           1.55h  Wed Jan 11 01:10:25 2017
Traceback (most recent call last):
  File "./manage.py", line 22, in <module>
    execute_from_command_line(sys.argv)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/core/management/__init__.py", line 367, in execute_from_command_line
    utility.execute()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/core/management/__init__.py", line 341, in execute
    django.setup()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/__init__.py", line 27, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/apps/registry.py", line 108, in populate
    app_config.import_models(all_models)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/apps/config.py", line 199, in import_models
    self.models_module = import_module(models_module_name)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 978, in _gcd_import
  File "<frozen importlib._bootstrap>", line 961, in _find_and_load
  File "<frozen importlib._bootstrap>", line 950, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 655, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 674, in exec_module
  File "<frozen importlib._bootstrap_external>", line 781, in get_code
  File "<frozen importlib._bootstrap_external>", line 741, in source_to_code
  File "<frozen importlib._bootstrap>", line 205, in _call_with_frames_removed
  File "/Users/rogerhoward/repos-hacklb/hacklb/app/geographic/models.py", line 79
    if instance.
               ^
SyntaxError: invalid syntax
 !  ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                      1192ms  Wed Jan 11 01:10:29 2017
# Shell Plus Model Imports
from business.models import License
from crime.models import Incident
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from geographic.models import Dataset, Feature, Parcel
from legistar.models import AgendaItem, Body, Document, Meeting
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.gis.db.models.functions import Distance
>>> from django.contrib.gis.measure import D
>>> from django.contrib.gis.db.models.functions import Distance
>>> from django.contrib.gis.measure import D
>>> p = Parcel.objects.first()
>>> p
<Parcel: 0000881f-f50f-4182-99d2-aed032539e3c parcel>
>>> p.coordinates.geojson
'{"type": "Point", "coordinates": [-118.21944726544417, 33.81139349625535]}'
>>> p.title
>>> p.nearest('park')
>>> 
now exiting InteractiveConsole...
 ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                            2.1m  Wed Jan 11 01:13:01 2017
# Shell Plus Model Imports
from business.models import License
from crime.models import Incident
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from geographic.models import Dataset, Feature, Parcel
from legistar.models import AgendaItem, Body, Document, Meeting
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.gis.db.models.functions import Distance
>>> from django.contrib.gis.measure import D
>>> p = Parcel.objects.first()
>>> p.nearest('park')
park
>>> 
now exiting InteractiveConsole...
 ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                           43.2s  Wed Jan 11 01:13:45 2017
# Shell Plus Model Imports
from business.models import License
from crime.models import Incident
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from geographic.models import Dataset, Feature, Parcel
from legistar.models import AgendaItem, Body, Document, Meeting
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
>>> from django.contrib.gis.db.models.functions import Distance
>>> from django.contrib.gis.measure import D
>>> p = Parcel.objects.first()
>>> p
<Parcel: 0000881f-f50f-4182-99d2-aed032539e3c parcel>
>>> p.nearest('lbpd')
lbpd
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/rogerhoward/repos-hacklb/hacklb/app/geographic/models.py", line 116, in nearest
    return Feature.objects.filter(feature_type=kind).annotate(distance=Distance('coordinates', self.coordinates)).order_by('distance').first()
NameError: name 'Distance' is not defined
>>> 
now exiting InteractiveConsole...
 ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                            1.2m  Wed Jan 11 01:15:02 2017
# Shell Plus Model Imports
from business.models import License
from crime.models import Incident
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from geographic.models import Dataset, Feature, Parcel
from legistar.models import AgendaItem, Body, Document, Meeting
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.gis.db.models.functions import Distance
>>> from django.contrib.gis.measure import D
>>> p = Parcel.objects.first()
>>> p.nearest('lbpd')
lbpd
<Feature: POLICE STATION - WEST DIVISION, lbpd (feature)>
>>> p.nearest('park')
park
<Feature: SILVERADO, park (feature)>
>>> p.nearest('park').distance
park
Distance(m=677.00418118)
>>> p.nearest('park')
park
<Feature: SILVERADO, park (feature)>
>>> 
now exiting InteractiveConsole...
 ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                            3.6m  Wed Jan 11 01:18:41 2017
# Shell Plus Model Imports
from business.models import License
from crime.models import Incident
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from geographic.models import Dataset, Feature, Parcel
from legistar.models import AgendaItem, Body, Document, Meeting
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.contrib.gis.db.models.functions import Distance
>>> from django.contrib.gis.measure import D
>>> p = Parcel.objects.first()
>>> p.nearest('park')
<Feature: SILVERADO, park (feature)>
>>> p.nearest('park').distance
Distance(m=677.00418118)
>>> p.nearest('lbfd')
<Feature: FIRE STATION 13, lbfd (feature)>
>>> p.nearest('lbpd')
<Feature: POLICE STATION - WEST DIVISION, lbpd (feature)>
>>> p.nearest('postal')
<Feature: CABRILLO STATION, postal (feature)>
>>> p.nearest('postal').distance()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: 'Distance' object is not callable
>>> p.nearest('postal').distance
Distance(m=1466.49498663)
>>> float(p.nearest('postal').distance)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
TypeError: float() argument must be a string or a number, not 'Distance'
>>> p.nearest('postal').distance
Distance(m=1466.49498663)
>>> dir(p.nearest('postal').distance)
['ALIAS', 'LALIAS', 'STANDARD_UNIT', 'UNITS', '__add__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__div__', '__doc__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__gt__', '__hash__', '__iadd__', '__idiv__', '__imul__', '__init__', '__init_subclass__', '__isub__', '__itruediv__', '__le__', '__lt__', '__module__', '__mul__', '__ne__', '__new__', '__nonzero__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__weakref__', '_default_unit', '_get_standard', '_set_standard', 'default_units', 'm', 'standard', 'unit_attname']
>>> p.nearest('postal').distance.m
1466.49498663
>>> Parcel.objects.all()
<QuerySet [<Parcel: 87564834-d1bd-4c80-a8df-632bc5296109 parcel>, <Parcel: 4fa3f495-d898-4806-b30a-26e57175cbf5 parcel>, <Parcel: 3936bc24-6911-49fb-9399-d5af11e82f54 parcel>, <Parcel: 9b66da52-338f-41e4-877b-797b6f41968f parcel>, <Parcel: 5096d269-b0a4-4093-b47a-0528e0823b82 parcel>, <Parcel: 54fc1d00-c5c9-4e55-a41c-78567746dea4 parcel>, <Parcel: 74e2eead-f971-445d-9213-8a093b60cf6b parcel>, <Parcel: 84bfc3cf-2d78-4e4f-a2a3-c226627d5a3e parcel>, <Parcel: 523967c9-97ef-4185-b459-d5d0baeeb7b2 parcel>, <Parcel: e573bbc9-439c-493f-9bc1-dd746a0fc41b parcel>, <Parcel: d3646d17-fc08-4e36-a8b6-f2a9b25afc83 parcel>, <Parcel: b9fc6826-37af-4ef8-9f41-081927bbbc3e parcel>, <Parcel: d48cf582-e36b-422d-9bde-4b322699a423 parcel>, <Parcel: 203c38b7-4ebb-4610-83a2-3924ff2f1908 parcel>, <Parcel: 1cb796ba-26c4-4079-adde-dc975460fc32 parcel>, <Parcel: c7947c0d-29cb-4c22-8100-03132ffd3a4b parcel>, <Parcel: cea7c7a3-bf48-4d41-94ed-411632d9ee74 parcel>, <Parcel: 768d463c-6242-4efc-9236-a49abbe09434 parcel>, <Parcel: e00fa897-01c5-4d24-a964-5cdcf97f4e97 parcel>, <Parcel: 3bb286fe-b453-4e3a-8721-e180a395bb42 parcel>, '...(remaining elements truncated)...']>
>>> Parcel.objects.order_by(dist_park)
Traceback (most recent call last):
  File "<console>", line 1, in <module>
NameError: name 'dist_park' is not defined
>>> Parcel.objects.order_by('dist_park')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 232, in __repr__
    data = list(self[:REPR_OUTPUT_SIZE + 1])
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 256, in __iter__
    self._fetch_all()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 1087, in _fetch_all
    self._result_cache = list(self.iterator())
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 54, in __iter__
    results = compiler.execute_sql()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 824, in execute_sql
    sql, params = self.as_sql()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 369, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 47, in pre_sql_setup
    order_by = self.get_order_by()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 293, in get_order_by
    field, self.query.get_meta(), default_order=asc))
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 553, in find_ordering_name
    field, targets, alias, joins, path, opts = self._setup_joins(pieces, opts, alias)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 586, in _setup_joins
    pieces, opts, alias)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/query.py", line 1402, in setup_joins
    names, opts, allow_many, fail_on_missing=True)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/query.py", line 1327, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'dist_park' into field. Choices are: coordinates, datetime_created, datetime_updated, description, geojson, id, json, objectid, polygon, source_url, title
>>> Parcel.objects.order_by('dist_park')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 232, in __repr__
    data = list(self[:REPR_OUTPUT_SIZE + 1])
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 256, in __iter__
    self._fetch_all()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 1087, in _fetch_all
    self._result_cache = list(self.iterator())
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 54, in __iter__
    results = compiler.execute_sql()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 824, in execute_sql
    sql, params = self.as_sql()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 369, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 47, in pre_sql_setup
    order_by = self.get_order_by()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 293, in get_order_by
    field, self.query.get_meta(), default_order=asc))
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 553, in find_ordering_name
    field, targets, alias, joins, path, opts = self._setup_joins(pieces, opts, alias)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 586, in _setup_joins
    pieces, opts, alias)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/query.py", line 1402, in setup_joins
    names, opts, allow_many, fail_on_missing=True)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/query.py", line 1327, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'dist_park' into field. Choices are: coordinates, datetime_created, datetime_updated, description, geojson, id, json, objectid, polygon, source_url, title
>>> Parcel.objects.all().order_by('dist_park')
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 232, in __repr__
    data = list(self[:REPR_OUTPUT_SIZE + 1])
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 256, in __iter__
    self._fetch_all()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 1087, in _fetch_all
    self._result_cache = list(self.iterator())
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/query.py", line 54, in __iter__
    results = compiler.execute_sql()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 824, in execute_sql
    sql, params = self.as_sql()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 369, in as_sql
    extra_select, order_by, group_by = self.pre_sql_setup()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 47, in pre_sql_setup
    order_by = self.get_order_by()
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 293, in get_order_by
    field, self.query.get_meta(), default_order=asc))
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 553, in find_ordering_name
    field, targets, alias, joins, path, opts = self._setup_joins(pieces, opts, alias)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/compiler.py", line 586, in _setup_joins
    pieces, opts, alias)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/query.py", line 1402, in setup_joins
    names, opts, allow_many, fail_on_missing=True)
  File "/Users/rogerhoward/.virtualenvs/hacklb/lib/python3.6/site-packages/django/db/models/sql/query.py", line 1327, in names_to_path
    "Choices are: %s" % (name, ", ".join(available)))
django.core.exceptions.FieldError: Cannot resolve keyword 'dist_park' into field. Choices are: coordinates, datetime_created, datetime_updated, description, geojson, id, json, objectid, polygon, source_url, title
>>> Parcel.objects.all()
<QuerySet [<Parcel: 87564834-d1bd-4c80-a8df-632bc5296109 parcel>, <Parcel: 4fa3f495-d898-4806-b30a-26e57175cbf5 parcel>, <Parcel: 3936bc24-6911-49fb-9399-d5af11e82f54 parcel>, <Parcel: 9b66da52-338f-41e4-877b-797b6f41968f parcel>, <Parcel: 5096d269-b0a4-4093-b47a-0528e0823b82 parcel>, <Parcel: 54fc1d00-c5c9-4e55-a41c-78567746dea4 parcel>, <Parcel: 74e2eead-f971-445d-9213-8a093b60cf6b parcel>, <Parcel: 84bfc3cf-2d78-4e4f-a2a3-c226627d5a3e parcel>, <Parcel: 523967c9-97ef-4185-b459-d5d0baeeb7b2 parcel>, <Parcel: e573bbc9-439c-493f-9bc1-dd746a0fc41b parcel>, <Parcel: d3646d17-fc08-4e36-a8b6-f2a9b25afc83 parcel>, <Parcel: b9fc6826-37af-4ef8-9f41-081927bbbc3e parcel>, <Parcel: d48cf582-e36b-422d-9bde-4b322699a423 parcel>, <Parcel: 203c38b7-4ebb-4610-83a2-3924ff2f1908 parcel>, <Parcel: 1cb796ba-26c4-4079-adde-dc975460fc32 parcel>, <Parcel: c7947c0d-29cb-4c22-8100-03132ffd3a4b parcel>, <Parcel: cea7c7a3-bf48-4d41-94ed-411632d9ee74 parcel>, <Parcel: 768d463c-6242-4efc-9236-a49abbe09434 parcel>, <Parcel: e00fa897-01c5-4d24-a964-5cdcf97f4e97 parcel>, <Parcel: 3bb286fe-b453-4e3a-8721-e180a395bb42 parcel>, '...(remaining elements truncated)...']>
>>> 
now exiting InteractiveConsole...
 ◰³ hacklb  ~/r/hacklb   master *…  app  djmigrate                                                                                                                         9.15h  Wed Jan 11 10:28:06 2017
No changes detected
Operations to perform:
  Apply all migrations: admin, auth, business, contenttypes, crime, geographic, legistar, sessions
Running migrations:
  No migrations to apply.
 ◰³ hacklb  ~/r/hacklb   master *…  app  djshell                                                                                                                          2845ms  Wed Jan 11 10:28:12 2017
# Shell Plus Model Imports
from business.models import License
from crime.models import Incident
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from geographic.models import Dataset, Feature, Parcel
from legistar.models import AgendaItem, Body, Document, Meeting
# Shell Plus Django Imports
from django.core.cache import cache
from django.conf import settings
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
Python 3.6.0 (default, Dec 24 2016, 08:01:42) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> Parcel.objects.all().order_by('dist_park')
<QuerySet [<Parcel: dd77e7ac-3e1c-4015-a578-5b327613b3e3 parcel>, <Parcel: 2662b2c9-fd05-4c07-8337-560d3e74e799 parcel>, <Parcel: 5e519060-77bc-4ba5-ab1f-4020d9b0c249 parcel>, <Parcel: d6d0ca11-9ee8-4d6c-b849-d3a8abeae52c parcel>, <Parcel: c3ec2a44-9b80-48ec-8c23-4c17d12b1a0b parcel>, <Parcel: 294d5b93-78b6-43f6-b583-2dcc4b307a93 parcel>, <Parcel: c6853106-937f-4594-bd39-87f709a8fdbb parcel>, <Parcel: ac5635f9-6f1c-461b-9445-a1f8bf74a6db parcel>, <Parcel: a43d2a7c-f1fa-4391-88dc-f01b9284e788 parcel>, <Parcel: c7c3022d-aec5-4457-90b6-0ab91608e868 parcel>, <Parcel: 07f61ae3-012a-4f6f-8bde-e657a779d69a parcel>, <Parcel: 8b090eec-0035-45bd-a18d-bf1a063ea666 parcel>, <Parcel: 5f0284dc-7b10-4fc4-8ecc-fd7b9ed2110d parcel>, <Parcel: d2a8946f-71f5-40f5-aafb-35e07aeb1956 parcel>, <Parcel: 768d463c-6242-4efc-9236-a49abbe09434 parcel>, <Parcel: 7c7b2286-c9e6-40cf-96d5-90f9ebc85332 parcel>, <Parcel: f505a5eb-c8ee-4a1b-9494-41edc8039d97 parcel>, <Parcel: ae59b8ff-f5d5-4654-a5d9-67c036f96b5e parcel>, <Parcel: 68229a34-8bdb-4609-ba82-a57d80638d81 parcel>, <Parcel: 7251b4dd-1478-48cf-b826-68b8d729e868 parcel>, '...(remaining elements truncated)...']>
>>> Parcel.objects.all().order_by('-dist_park')
<QuerySet [<Parcel: 9ed5ae9b-3281-4468-8287-a6b8ee0098cc parcel>, <Parcel: 19abe006-ffcd-4f07-8cb2-f3c8da6a29c5 parcel>, <Parcel: 27eb70b9-9220-48a9-9bd3-ab4ec11761fa parcel>, <Parcel: 39d70170-908b-4e88-b860-e24f2ba85f12 parcel>, <Parcel: e2b523e4-7373-475f-82ef-f27db6b6a41f parcel>, <Parcel: c5974305-3ee8-45ec-a528-32732ced3f6b parcel>, <Parcel: 50005615-0a0c-4b6b-a96c-818a61364f49 parcel>, <Parcel: 35f39a6b-6888-4c52-b195-67d5b9aeb982 parcel>, <Parcel: 005e53a0-6584-44e4-a90d-7f9176b983ad parcel>, <Parcel: 9f2e19fa-5590-4d81-90de-1e3c24c01c00 parcel>, <Parcel: 6148892b-4b53-4603-b5e8-4ef0ab6572b9 parcel>, <Parcel: 907793a3-a44e-4af0-ab12-00fb9fe4eca1 parcel>, <Parcel: 46cbb4ad-b088-4d06-84bd-4365f39fc1e1 parcel>, <Parcel: 7c22f387-a7b1-4e49-a377-7f5848b93d80 parcel>, <Parcel: c10ab104-d5e0-40f7-ad3c-32bd5894ad6b parcel>, <Parcel: 9d2d30db-dc38-421a-a7ea-fdaa31544051 parcel>, <Parcel: db576b86-1726-43b5-a987-9a30f64fd48b parcel>, <Parcel: 8d1c2731-4c83-4708-8755-f6c6ba805a06 parcel>, <Parcel: b6bc8a5c-8bc9-4f43-9c59-cde374c5f845 parcel>, <Parcel: ad1fbe13-1fd2-4481-a549-f546ea77d4d8 parcel>, '...(remaining elements truncated)...']>
>>> Parcel.objects.all().order_by('-dist_park').first().dist_park
>>> Parcel.objects.all().order_by('dist_park').first().dist_park
0.00116275
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().dist_park
1094.00138878
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().coordinates.geojson
'{"type": "Point", "coordinates": [-118.16887023561357, 33.859874310407776]}'
>>> Parcel.objects.filter(dist_park__isnull=True).count()
102181
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().dist_park
2071.45123699
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().dist_park
2071.45123699
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().dist_park
2071.45123699
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().dist_park
2071.45123699
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').first().coordinates.geojson
'{"type": "Point", "coordinates": [-118.15584210507771, 33.81002767140383]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').[2].coordinates.geojson
  File "<console>", line 1
    Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park').[2].coordinates.geojson
                                                                          ^
SyntaxError: invalid syntax
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[2].coordinates.geojson
'{"type": "Point", "coordinates": [-118.15710637771741, 33.81047469358227]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[1].coordinates.geojson
'{"type": "Point", "coordinates": [-118.15655192953933, 33.80950011511355]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[3].coordinates.geojson
'{"type": "Point", "coordinates": [-118.1557680914353, 33.80908846942296]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[4].coordinates.geojson
'{"type": "Point", "coordinates": [-118.1572032832831, 33.80999377781068]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[5].coordinates.geojson
'{"type": "Point", "coordinates": [-118.1571776138966, 33.80793385959237]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[10].coordinates.geojson
'{"type": "Point", "coordinates": [-118.157780828376, 33.81056339782638]}'
>>> Parcel.objects.filter(dist_park__isnull=False).order_by('-dist_park')[100].coordinates.geojson
'{"type": "Point", "coordinates": [-118.09583524838645, 33.75690019577267]}'
>>> 
