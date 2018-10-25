The user @{{ validation.user }} validate your site template "{{ validation.site.base_url }}" and found these accessibility errors:
{% autoescape off %}{% for page in pages %}
* Page {{ page.page_url }}:
{% for issue in page.issuepage_set.all %}
  * Issue *{{ issue.uuid }}*:
    * **Type**: {{ issue.get_issue_type_display }}
    * **Code**: {{ issue.code }}
    * **Message**: {{ issue.message }}
    * **Selector**: `{{ issue.selector }}`
    * **Context**: `{{ issue.context }}`
{% endfor %}
{% endfor %}{% endautoescape %}
You can check these accessibility errors using [pa11y](https://github.com/pa11y/pa11y).
