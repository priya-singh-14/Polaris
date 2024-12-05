
########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
outcome = Blueprint('outcome', __name__)


# Returns mentor and mentee matches
# GET/Match
@outcome.route('/Match', methods=['GET'])
def return_match():
    query = '''
        SELECT  *
        FROM `Match`
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Returns a match supervised by an advisor
# GET/Match
@outcome.route('/AdvisorMatch/<int:advisorId>', methods=['GET'])
def return_advisor_match(advisorId):

    query = f'''
        SELECT *
        FROM `Match`
        JOIN Mentor ON `Match`.mentorId = Mentor.mentorId
        JOIN Mentee ON `Match`.menteeId = Mentee.menteeId
        JOIN User AS MentorUser ON Mentor.userId = MentorUser.userId
        JOIN User AS MenteeUser ON Mentee.userId = MenteeUser.userId
        WHERE Mentor.advisorId = {advisorId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Returns mentor assigned to a given mentee 
# GET/Match
@outcome.route('/Match/<int:menteeId>', methods=['GET'])
def return_matched_mentor(menteeId):
    query = f'''
        SELECT  Match.mentorId
        FROM `Match` Join Mentee on Match.menteeId = Mentee.menteeId
        Where Match.menteeId = {menteeId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# GET the list of mentees matched with a specific mentor



# Create matches between mentors and mentees
# POST/Match 
@outcome.route('/MatchMentees', methods=['POST'])
def create_match():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    menteeId = the_data['menteeId']
    mentorId = the_data['mentorId']
    

    query = f'''
        INSERT INTO `Match` (menteeId, mentorId)
        VALUES ('{menteeId}', '{mentorId}')
    '''

    current_app.logger.info(query)


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response


# change matches between mentors and mentees
@outcome.route('/UpdateMatch', methods = ['PUT'])
def update_match():
    
    the_data = request.json
    og_mentorId = the_data['ogMentorId']
    og_menteeId = the_data['ogMenteeId']
    new_menteeId = the_data['newMenteeId']
    new_mentorId = the_data['newMentorId']

    query = '''
    UPDATE `Match`
    SET mentorId = %s, menteeId = %s
    WHERE mentorId = %s AND menteeId = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (new_mentorId, new_menteeId, og_mentorId, og_menteeId))
    db.get_db().commit()
    
    response = make_response("Successfully updated profile")
    response.status_code = 200
    return response


# delete a match between a mentor and mentee
@outcome.route('/DeleteMatch', methods = ['DELETE'])
def delete_match():

    the_data = request.json
    current_app.logger.info(the_data)

    mentorId = the_data['mentorId']
    menteeId = the_data['menteeId']

    query = f'''
        DELETE FROM `Match`
        WHERE mentorId = {mentorId} AND menteeId = {menteeId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
        
    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response


# return all chat logs between all users
@outcome.route('/Chats', methods=['GET'])
def return_chats():
    query = '''
        SELECT  *
        FROM Chats
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# return all chat logs between all users
@outcome.route('/Chats/<int:senderId>/<int:recipientId>', methods=['GET'])
def return_chat_history(senderId, recipientId):
    query = '''
        SELECT senderId, text, timestamp 
        FROM Chats 
        WHERE (senderId = %s AND recipientId = %s) 
        OR (senderId = %s AND recipientId = %s) 
        ORDER BY timestamp ASC
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (senderId, recipientId, recipientId, senderId))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@outcome.route('/createNewChat', methods=['POST'])
def create_new_chat():
    the_data = request.json
    current_app.logger.info(the_data)

    senderId = the_data['senderId']
    recipientId = the_data['recipientId']
    text = the_data['text']
    cursor = db.get_db().cursor()

    query = '''
        INSERT INTO Chats (senderId, recipientId, text)
        VALUES (%s, %s, %s)
    '''
   
    cursor.execute(query, (senderId, recipientId, text))
    db.get_db().commit()    

    response = make_response("Successfully created profile")
    response.status_code = 200
    return response


@outcome.route('/Metrics/<int:menteeId>', methods=['GET'])
def view_mentee_progress(menteeId):

    query = f'''
        SELECT  menteeId, progressNotes, adjustmentNotes
        FROM Metrics
        WHERE menteeId = {menteeId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@outcome.route('/createMetric', methods=['POST'])
def post_new_metrics():
    the_data = request.json
    current_app.logger.info(the_data)


    mentorId = the_data['mentorId']
    menteeId = the_data['menteeId']
    progressNotes = the_data['progressNotes']
    adjustmentNotes = the_data['adjustmentNotes']

    query = '''
        INSERT INTO Metrics (mentorId, menteeId, progressNotes, adjustmentNotes)
        VALUES (%s, %s, %s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (mentorId, menteeId, progressNotes, adjustmentNotes))
    db.get_db().commit()
    
    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response

