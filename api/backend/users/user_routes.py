# anything /mentor /mentee /advisor /employer


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
from datetime import datetime

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
user = Blueprint('user', __name__)


@user.route('/createNewUser', methods=['POST'])
def create_profile():
    the_data = request.json
    current_app.logger.info(the_data)

    name = the_data['name']
    email = the_data['email']
    profilepic = the_data['profilepic']
    college = the_data['college']
    major = the_data['major']
    minor = the_data['minor']

    cursor = db.get_db().cursor()

    query = f'''
        INSERT INTO User (name, email, profilepic, college, major, minor)
        VALUES ('{name}', '{email}', '{profilepic}', '{college}', '{major}', '{minor}')
    '''
   
    cursor.execute(query)
    db.get_db().commit()    

    response = make_response("Successfully created profile")
    response.status_code = 200
    return response

@user.route('/generateUserID', methods=['GET'])
def generate_user_id():
    cursor = db.get_db().cursor()

    query = '''
        SELECT MAX(userID) AS max_userID 
        FROM User
    '''
    cursor.execute(query)
    result = cursor.fetchone()

    new_userID = result['max_userID'] + 1

    response = make_response({'new_userID': new_userID})
    response.status_code = 200
    return response

@user.route('/updateUser', methods=['PUT'])
def update_user_data():
    
    the_data = request.json
    name = the_data['name']
    email = the_data['email']
    profilepic = the_data['profilepic']
    major = the_data['major']
    minor = the_data['minor']
    college = the_data['college']
    id = the_data['id']
    current_app.logger.info('PUT /the_data')

    query = f'''
        UPDATE User 
        SET name = %s, profilepic = %s, email = %s, major = %s, minor = %s, college = %s 
          WHERE User.userId = %s 
    '''

    data = (name, profilepic, email, major, minor, college, id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response("Successfully updated profile")
    response.status_code = 200
    return response

@user.route('/updateMentee', methods=['PUT'])
def update_mentee_data():
    
    the_data = request.json
    current_app.logger.info('PUT /the_data')

    bio = the_data['bio']
    resume = the_data['resume']
    id = the_data['id']

    query = f'''
        UPDATE Mentee 
        SET bio = %s, resume = %s
          WHERE Mentee.userId = %s 
    '''
    data = (bio, resume, id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response("Successfully updated profile")
    response.status_code = 200
    return response

@user.route('/updateMentor', methods=['PUT'])
def update_mentor_data():
    
    the_data = request.json
    current_app.logger.info('PUT /the_data')

    company = the_data['company']
    currentPosition = the_data['currentPosition']
    isWorking = 1 if the_data['isWorking'] else 0 
    isInSchool = 1 if the_data['isInSchool'] else 0 
    id = the_data['id']

    query = f'''
        UPDATE Mentor 
        SET company = %s, currentPosition = %s, isInSchool = %s, isWorking = %s
          WHERE Mentor.userId = %s 
    '''
    data = (company, currentPosition, isInSchool, isWorking, id)
    cursor = db.get_db().cursor()
    cursor.execute(query, data)
    db.get_db().commit()

    response = make_response("Successfully updated profile")
    response.status_code = 200
    return response

@user.route('/getMenteeData/<int:menteeId>', methods=['GET'])
def get_mentee_data(menteeId):

    query = f'''
        SELECT User.name, Mentee.bio, Mentee.userId, Mentee.resume, User.email, User.profilepic, User.major, User.minor, User.college
        FROM Mentee Join User on Mentee.userId = User.userId
        WHERE Mentee.menteeId = '{menteeId}'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/Mentees/<string:college>/<string:major>/<string:minor>', methods=['GET'])
def get_relevant_mentee(college, major, minor):

    query = f'''
        SELECT User.name, Mentee.bio, Mentee.userId, Mentee.menteeId, Mentee.resume, User.email, User.profilepic, User.major, User.minor, User.college
        FROM Mentee Join User on Mentee.userId = User.userId
        WHERE User.college = '{college}' OR User.major = '{major}' OR User.minor = '{minor}'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/AllMentees', methods=['GET'])
def get_all_mentee_data():

    query = f'''
        SELECT User.name, Mentee.bio, Mentee.userId, Mentee.menteeId, Mentee.resume, User.email, User.profilepic, User.major, User.minor, User.college
        FROM Mentee join User on Mentee.userId = User.userId
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/getMentorData/<int:mentorId>', methods=['GET'])
def get_mentor_data(mentorId):

    query = f'''
        SELECT User.name, Mentor.userId, Mentor.isInSchool, Mentor.isWorking, Mentor.currentPosition, Mentor.company, User.email, User.profilepic, User.major, User.minor, User.college
        FROM Mentor Join User on Mentor.userId = User.userId
        WHERE Mentor.mentorId = '{mentorId}'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@user.route('/createNewMentee', methods=['POST'])
def create_mentee_profile():
    the_data = request.json
    current_app.logger.info(the_data)

    userID = the_data['userID']
    bio = the_data['bio']
    resume = the_data['resume']

    query = '''
        INSERT INTO Mentee (userID, bio, resume)
        VALUES (%s, %s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (userID, bio, resume) ) 
    db.get_db().commit()

    response = make_response("Successfully created profile")
    response.status_code = 200
    return response

@user.route('/viewMenteeProfile/<int:menteeId>', methods=['GET'])
def view_profile(menteeId):
    cursor = db.get_db().cursor()
    query = f'''
        SELECT User.userID, User.name, User.email, User.profilepic, User.major, User.minor, User.college, Mentee.bio, Mentee.resume
        FROM User Join Mentee ON User.userId = Mentee.userId
        WHERE menteeId = '{menteeId}'
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@user.route('/createNewMentor', methods=['POST'])
def create_mentor_profile():
    the_data = request.json
    current_app.logger.info(f"Received data for mentor creation: {the_data}")

    userID = the_data['userID']
    isWorking = 1 if the_data['isWorking'] else 0   
    isInSchool = 1 if the_data['isInSchool'] else 0  
    company = the_data['company']
    currentPosition = the_data['currentPosition']
    advisorID = the_data['advisorID']

    query = '''
        INSERT INTO Mentor (userID, isWorking, isInSchool, company, currentPosition, advisorID)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (userID, isWorking, isInSchool, company, currentPosition, advisorID)) 
    db.get_db().commit()

    response = make_response("Successfully created profile", 200)
    return response

@user.route('/viewMentorList', methods=['GET'])
def view_mentor_list():
    cursor = db.get_db().cursor()
    query = f'''
        SELECT *
        FROM User Join Mentor ON User.userId = Mentor.userId
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/viewMentorProfile/<int:mentorId>', methods=['GET'])
def view_mentor_profile(mentorId):
    cursor = db.get_db().cursor()
    query = f'''
        SELECT User.userID, User.name, User.email, User.profilepic, User.major, User.minor, User.college, Mentor.isWorking, Mentor.isInSchool, Mentor.company, Mentor.currentPosition
        FROM User Join Mentor ON User.userId = Mentor.userId
        WHERE mentorId = '{mentorId}'
    '''
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/Mentees', methods=['GET'])
def get_mentees():
    query = '''
        SELECT  *
        FROM Mentee
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/Employers', methods=['GET'])
def get_employers():
    query = '''
        SELECT  *
        FROM Employer
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/mostRecentMentor', methods=['GET'])
def get_recent_mentor():
    query = f'''
        SELECT MAX(mentorId)
        FROM Mentor
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@user.route('/Mentors/<int:advisorId>', methods=['GET'])
def get_advisor_mentor(advisorId):

    query = f'''
        SELECT *
        FROM Mentor Join User on Mentor.userId = User.userId
        WHERE Mentor.advisorID = {advisorId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



@user.route('/mostRecentMentee', methods=['GET'])
def get_recent_mentee():
    query = f'''
        SELECT MAX(menteeId)
        FROM Mentee
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchone()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response



@user.route('/Advisors', methods=['GET'])
def get_advisors():
    query = '''
        SELECT  *
        FROM Advisor
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/Users', methods=['GET'])
def get_users():
    query = '''
        SELECT  *
        FROM User
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@user.route('/PairAdvisor/<string:college>', methods = ['GET'])
def advisor_pairing(college):

    query = '''
        SELECT Advisor.advisorId, Advisor.userId
        FROM Advisor
        WHERE Advisor.department = %s
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (college,)) 
    the_data = cursor.fetchone()

    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response


@user.route('/Mentor', methods=['GET'])
def return_mentors():
    query = '''
        SELECT  *
        FROM Mentor
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/Mentor', methods=['POST'])
def add_mentor(mentorId, userId, isWorking, isInSchool, company, currentPosition, advisorId):
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)


    query = f'''
        INSERT INTO Mentor
        VALUES ('{mentorId}, {userId}, {isWorking}, {isInSchool}, {company}, {currentPosition}, {advisorId}')
    '''

    current_app.logger.info(query)


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

@user.route('/DeleteMentor', methods = ['DELETE'])
def delete_mentor():


    the_data = request.json
    current_app.logger.info(the_data)

    mentorId = the_data['mentorId']

    query = f'''
        DELETE FROM Mentor
        WHERE mentorId = {mentorId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
        
    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response

@user.route('/DeleteMentee', methods = ['DELETE'])
def delete_mentee():

    the_data = request.json
    current_app.logger.info(the_data)

    menteeId = the_data['menteeId']

    query = f'''
        DELETE FROM Mentee 
        WHERE menteeId = {menteeId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
        
    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response

# return user information 
@user.route('/User', methods=['GET'])
def return_gen_user_info():
    query = '''
        SELECT  *
        FROM User
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# select user by uid 
@user.route('/User/<userid>', methods=['GET'])
def return_user_info(userid):
    query = '''
        SELECT *
        FROM User
        WHERE userId = %s
    '''
    cursor = db.get_db().cursor()
    cursor.execute(query, (userid,))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/User', methods = ['DELETE'])
def delete_user():

    the_data = request.json
    current_app.logger.info(the_data)

    userId = the_data['userId']

    query = f'''
        DELETE FROM User
        WHERE userId = {userId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)

    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@user.route('/MentorMentees/<int:mentorId>', methods=['GET'])

def get_mentor_mentees(mentorId):
    query = '''
        SELECT 
            Mentee.menteeId,
            User.name,
            User.profilepic,
            User.major,
            Mentee.bio,
            Mentee.resume
        FROM 
            `Match`
        JOIN 
            Mentee ON Match.menteeId = Mentee.menteeId
        JOIN 
            User ON Mentee.userId = User.userId
        WHERE 
            Match.mentorId = %s;
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query, (mentorId,))
    mentee_data = cursor.fetchall()
    response = make_response(jsonify(mentee_data))
    response.status_code = 200
    return response