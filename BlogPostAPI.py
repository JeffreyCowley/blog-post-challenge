from flask import Flask, request
from flask_restful import Api, Resource, abort
import BlogPost
import configparser
import json

app = Flask(__name__)
api = Api(app)

blog_post_app = BlogPost.BlogPostApp()


class GetEntries(Resource):

    def get(self):
        result = blog_post_app.get_all_entries()

        result_dict = {'entries': []}

        for item in result:
            result_dict['entries'].append({'post_id': item[0],'title': item[1],'body': item[2]})

        json_result = json.dumps(result_dict)

        return json_result


class AddEntry(Resource):

    def post(self):
        if not request.json:
            abort(400)
        try:
            blog_post_app.set_entry(request.json['title'], request.json['body'])
        except KeyError as error:
            abort(400)


api.add_resource(GetEntries, "/posts")
api.add_resource(AddEntry, "/post")

if __name__ == '__main__':
    config = configparser.ConfigParser(strict=False, interpolation=None)
    config.read('BlogPost.ini')
    database_file = config['Database']['file']

    logging_file = config['Logging']['file']
    logging_format = config['Logging']['format']
    logging_level = config['Logging']['level']

    api_port = config.get('API','port', fallback='5000')

    blog_post_app.setup_logging(logging_file, logging_level, logging_format)

    blog_post_app.connect_database(database_file)

    app.run(debug=True, port=api_port)