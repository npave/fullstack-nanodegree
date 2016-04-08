class Resource():
    """Class to define the attribute of a resource.

    Attributes:
        name (str): the name of the resource. 
        description (str): description of the resource.
        style (str): the kind of resource it is, Online-class, contest,
                     list of problems, and so on.
        technologies (str): the different programming languages that you
                            can use or practice in this resource. 
        url (str): homepage of the resource.
        
    """
    def __init__(self, name, description, style, technologies, language, url):
        self.name = name
        self.description = description
        self.style = style
        self.technologies = technologies
        self.language = language
        self.url = url