from Project2_Flask import app, forms
from flask import request, render_template


@app.route('/', methods=['GET', 'POST'])
def search():
    userInformation_form = forms.userInformation(request.form)

    if request.method == 'POST':
        first_name_post = request.form["first_name"]
        last_name_post = request.form["last_name"]
        source_api = request.form["source_api"]
        print("source", source_api)
        section_api = request.form["section_api"]
        print("section", section_api)
        source_api_post_data = forms.APIcall(source_api, section_api)

        

        response = [first_name_post, last_name_post]



        return render_template('result.html', form=userInformation_form, result=source_api_post_data, response=response)





    return render_template('search.html', form=userInformation_form)