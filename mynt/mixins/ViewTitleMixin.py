from django.shortcuts import render


class ViewTitleMixin: 
    title = ""
    def get_title(self):
        return self.title
    def render(self, request, template_name, context):
        context["title"] = self.get_title()
        return render(request, template_name, context)