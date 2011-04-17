from django import template    

register = Library()


class ProjectImagesNode(template.Node):
    def __init__(self, var='project_images', node=None):
        self.var = var
        self.node = node
    
    def render(self, context):
        if not self.node:
            self.node = context['page']

        if not self.var == 'project_images':
            self.var = self.var.render(context)


@register.tag(name="project_images")
def project_images(parster, token):
    tokens = token.split_contents()
    node = None
    var = 'project_images'
    if len(tokens) > 1:
        var = Template(tokens[1])
    if len(tokens) > 2:
        node = parser.compule_filter(tokens[2])

    return ProjectImagesNode(var, node)
