# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.template.loader import render_to_string
from django.contrib.contenttypes.models import ContentType

register = template.Library()


class CommentNode(template.Node):
    """
    Helper class for handling the show_gplus_comments template tags.
    """

    def __init__(self, ctype=None, object_pk_expr=None, object_expr=None):
        if ctype is None and object_expr is None:
            raise template.TemplateSyntaxError("Comment nodes must be given either a literal object or a ctype and object pk.")
        self.ctype = ctype
        self.object_pk_expr = object_pk_expr
        self.object_expr = object_expr

    @classmethod
    def handle_token(cls, parser, token):
        """Class method to parse show_gplus_comments and return a Node."""
        tokens = token.split_contents()
        if tokens[1] != 'for':
            raise template.TemplateSyntaxError("Second argument in %r tag must be 'for'" % tokens[0])

        # {% show_gplus_comments for obj %}
        if len(tokens) == 3:
            return cls(object_expr=parser.compile_filter(tokens[2]))

        # {% show_gplus_comments for app.models pk %}
        elif len(tokens) == 4:
            return cls(
                ctype=CommentNode.lookup_content_type(tokens[2], tokens[0]),
                object_pk_expr=parser.compile_filter(tokens[3])
            )

    @staticmethod
    def lookup_content_type(token, tagname):
        try:
            app, model = token.split('.')
            return ContentType.objects.get_by_natural_key(app, model)
        except ValueError:
            raise template.TemplateSyntaxError("Third argument in %r must be in the format 'app.model'" % tagname)
        except ContentType.DoesNotExist:
            raise template.TemplateSyntaxError("%r tag has non-existant content-type: '%s.%s'" % (tagname, app, model))

    def render(self, context):
        obj = None
        if self.object_pk_expr:
            object_pk = self.object_pk_expr.resolve(context, ignore_failures=True)
            obj = self.ctype.get_object_for_this_type(pk=object_pk)
        if self.object_expr:
            obj = self.object_expr

        if obj:
            context.push()
            url = 'http://%s%s' % (Site.objects.get_current().domain, obj.get_absolute_url())
            width = getattr(settings, 'GPLUS_COMMENTS_WIDTH', '650')
            comments_html = render_to_string('gplus-comments/show_comments.html', {"url": url, "width": width}, context)
            context.pop()
            return comments_html
        else:
            return ''


@register.tag
def show_gplus_comments(parser, token):
    """
    Return the HTML code to display Google+ comments.

    Syntax::

        {% show_gplus_comments for [object] %}
        {% show_gplus_comments for [app].[model] [object_id] %}

    Example usage::

        {% show_gplus_comments for event %}
    """

    return CommentNode.handle_token(parser, token)
