from Project2_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SelectField

class userInformation(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    source_api = RadioField("Source",
                            choices=[('all', 'ALL Articles'),
                                     ('nyt', "New York Times"),
                                     ('inyt', "International New York Times")])
    section_api = SelectField("Section",
                              choices=[('arts', "Arts"),
                                       ('automobiles', "Automobiles"),
                                       ('books', "Books"),
                                       ('business', 'Business'),
                                       ('fashion', "Fashion"),
                                       ('food', "Food"),
                                       ('health', 'Health')])


def APIcall(source_api, section_api):
    api_key_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/api_key.json")
    api_key = api_key_dict["my_key"]
    url = "https://api.nytimes.com/svc/news/v3/content/" + source_api + "/" + section_api + ".json?api-key=" + api_key
    response = requests.get(url).json()
    main_functions.save_to_file(response, "Project2_Flask/JSON_Files/response.json")

    response_dict = main_functions.read_from_file("Project2_Flask/JSON_Files/response.json")
    return_list = []
    for i in response_dict["results"]:
        title = i["title"]
        url = i["url"]
        return_list.append((title, url))
    return return_list




















