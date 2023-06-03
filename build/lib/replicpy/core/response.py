from jinja2 import Template
import json



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



def JsonResponse(dic_value:dict):
    def inner_return_json():
        return json.dumps(dic_value)
    return inner_return_json