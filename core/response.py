from jinja2 import Template



def Response(template,context={}):
    '''
    this function return render template
    '''
    with open(f"templates/{template}") as file:
        open_template = Template(file.read())

    render_template = open_template.render(context)
    def response():
        return render_template
    return response