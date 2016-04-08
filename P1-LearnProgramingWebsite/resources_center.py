import data_structure
import fun_list

# Instances of class Resource for each resource we show in the website.

coursera = data_structure.Resource("Coursera - Algorithms: Design and " 
								   "Analysis, Part 1",
								   "In this course you could learn the "
								   "fundamentals of algorithm design.",
								   "Online class",
								   "C, Python, Java",
								   "English",
								   "https://www.coursera.org/course/algo")

code_chef = data_structure.Resource("Code chef",
									"Programming community that host contest "
									"and training for programmers.",
									"Practice",
									"C++, Python, Java",
									"English, Mandarin Chinese, Russian",
									"https://www.codechef.com/")

coding_bat = data_structure.Resource("Coding bat",
									 "Web site with a list of coding problems "	
                                     "to improves skill in Java and Python.",
                                     "Practice",
                                     "Python, Java",
                                     "English",
                                     "http://codingbat.com/")     

omegaup = data_structure.Resource("Omega Up",
                                  "Web project help improve skill of software "
                                  "developers through problems solving.",
                                  "Practice",
                                  "C++, Python, Java",
                                  "Spanish",
                                  "https://omegaup.com/")

# List that include all the resources that we want to show in the website.  
resources = [coursera, code_chef, coding_bat, omegaup]

# Create Web page with the list of resources.
fun_list.open_resources_page(resources)
