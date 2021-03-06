"""
Haystack settings for HackLB project.
"""

# --------------------------------------------------
# Haystack settings
# --------------------------------------------------

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': PROJECT_NAME,
    },
}

HAYSTACK_SEARCH_RESULTS_PER_PAGE = 100