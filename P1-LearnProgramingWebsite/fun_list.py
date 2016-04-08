import webbrowser


# Styles and scripting for the page.
main_page_head = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset = "utf-8">
        <title>Learn programming</title>
         <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
         <style type="text/css" media="screen">
            .container{
                width: 75%;
                margin-left: auto;
                margin-right: auto;
                background: #f7fdff;
            }
            .container ul{
                list-style: none;
            }
            .title-page{
                color: #365674;
                font-weight: bold;
                text-align: center;
                font-size: 2.3em;
            }
            .head a{
                font-size: 1.3em;
            }
            .resources{
                margin-top: 1%;
            }
            
             .resource-row li a {
                display: inline-block;
             }
             .left-row{
                float:left;
                width: 30%;
                margin-top: 3%;
                font-size:.9em;
                
             }
             .right-row{
                float:right;
                width: 70%;
               
             }
             .one-resource{
                overflow: hidden;
                font-size: 1.3em;
                
             }
             .title-resource{
                font-size: 1.5em;
                color: #f9654a;
             }

             .topic a{
                font-weight: bold;
                font-style: italic;
             }

             .description{
                margin-top: 15px;
             }
         </style>
         
         <script type="text/javascript" charset="utf-8">
            $(document).on('click', '.topic a', function(event){
                var url = $(this).attr('id');
                window.open(url, '_blank');
            });
         
         </script>
    </head>
"""

# The main page layout and title bar.
main_page_content = """
    <body>
        <div class="container">
            <div class="head">
                <p class="title-page">Learn Programming</p>
                <a>If you want to learn programming you should practice, practice and practice.
                Here are a list of resources that can help you in this journey.</a>
            </div>
            <div class="resources">
                {resource_row}
            </div>
        </div>
    </body>
    </html>
"""

# A single resource entry html template.
resource_row = """
    <div class="one-resource">
        <div class="left-row">
            <ul class="resource-row">
                <li>Type of resource: <a> {resource_type}</a></li>
                <li>Technologies: <a> {resource_technologies}</a></li>
                <li>Languages: <a>{resource_language}</a></li>
            </ul>
        </div>
        <div class="right-row">
            <ul class="resource-row">
                <li><a class="title-resource">{resource_title}</a></li>
                <li class="topic">View the <a id={resource_url}> resource </a></li>
                <li><a class="description">{resource_information}</a></li>
            </ul>
        </div>
    </div>
"""

def create_resources_content(resources):
	# The HTML content for this section of the page.
    content = ''
    for resource in resources:
	# Append the title for the resource with its content filled in.
        content += resource_row.format(
            resource_title = resource.name,
            resource_information = resource.description,
            resource_type = resource.style,
            resource_technologies = resource.technologies,
            resource_language = resource.language,
            resource_url = resource.url
        )
    return content
    

def open_resources_page(resources):
	# Create or overwrite the output file.
    output_file = open('learn_programming.html', 'w')

	# Replace the resource titles place holder generated content.
    rendered_content = main_page_content.format(
        resource_row = create_resources_content(resources))

	# Output the file.
    output_file.write(main_page_head + rendered_content)
    output_file.close()
