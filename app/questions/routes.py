# questions/routes.py
from flask import Blueprint, request, make_response, jsonify
from flask import current_app as app
from ..models import Question
from datetime import datetime
# from .. import db

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# set up a blueprint
questions_bp = Blueprint('questions_bp', __name__)


@questions_bp.route('/add_question', methods=['POST'])
def add_question():
    """Add a question to the database.

    Precondition(s):
    - user_id is not None
    - question_text is not None
    - is_anon is not None
    """

    # get query parameters
    user_id = request.args.get('user_id')
    title = request.args.get('title')
    content = request.args.get('content')
    is_anon = int(request.args.get('is_anonymous'))
    source = request.args.get('source')
    
    if user_id is not None and content is not None and is_anon is not None:

        # check if a question with this content exists already
        existing_question = Question.query.filter(Question.content == content).first()
        if existing_question:
            return make_response(f"This question already exists!")

        # check if source was provided
        if source is None:
            source = "SideEffects App" # default source       

        # create new question object
        new_question = Question(user_id=user_id,
                        title=title,
                        content=content,
                        date_created=datetime.now(),
                        date_updated=datetime.now(),
                        is_anonymous=is_anon,                        
                        source=source,
                        num_comments=0)
        db.session.add(new_question) # adds a new question to the database
        db.session.commit() # commit all changes to the database        
        return make_response(f"Question successfully created!", 200)                        
        
    return make_response(f"Unable to create question due to missing information!", 400)                        


@questions_bp.route('/get_question', methods=['GET'])
def get_question():
    """Return a question from the database with id 'question_id' in JSON format.

    Returns a JSON response containing the question text of the given question_id.
    """

    # get query parameters
    question_id = request.args.get('question_id')

    # query for question
    question = Question.query.get(question_id)

    # format response
    response = []
    response.append({
        "question_id": question_id,
        "question_user_id": question.user_id,
        "question_title": question.title,
        "question_content": question.content,
        "question_date_updated": question.date_updated,
        "question_source": question.source,
        "question_is_anon": question.is_anonymous,
        "question_num_comments": question.num_comments
    })

    return jsonify(response)