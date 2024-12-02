
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
orbit = Blueprint('orbit', __name__)

@orbit.route('/createNewUser', methods=['POST'])
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

@orbit.route('/generateUserID', methods=['GET'])
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


@orbit.route('/createNewMentee', methods=['POST'])
def create_mentee_profile():
    the_data = request.json
    current_app.logger.info(the_data)

    userID = the_data['userID']
    bio = the_data['bio']
    resume = the_data['resume']

    query = f'''
        INSERT INTO Mentee (userID, bio, resume)
        VALUES ('{userID}', '{bio}', '{resume}')
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query) 
    db.get_db().commit()

    response = make_response("Successfully created profile")
    response.status_code = 200
    return response

@orbit.route('/viewMenteeProfile/<int:menteeId>', methods=['GET'])
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


@orbit.route('/createNewMentor', methods=['POST'])
def create_mentor_profile():
    the_data = request.json
    current_app.logger.info(f"Received data for mentor creation: {the_data}")

    userID = the_data['userID']
    isWorking = 1 if the_data['isWorking'] else 0  # Convert boolean to integer
    isInSchool = 1 if the_data['isInSchool'] else 0  # Convert boolean to integer
    company = the_data['company']
    currentPosition = the_data['currentPosition']
    advisorID = the_data['advisorID']

    query = f'''
        INSERT INTO Mentor (userID, isWorking, isInSchool, company, currentPosition, advisorID)
        VALUES ('{userID}', '{isWorking}', '{isInSchool}', '{company}', '{currentPosition}', '{advisorID}')
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query) 
    db.get_db().commit()

    response = make_response("Successfully created profile", 200)

    return response


@orbit.route('/viewMentorProfile/<int:mentorId>', methods=['GET'])
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

# Return a list of jobs and their information
# GET/JobPosting
@orbit.route('/JobPosting', methods=['GET'])
def get_job_postings():
    query = '''
        SELECT JobPosting.jobDesc, JobPosting.role, Company.name
        FROM JobPosting JOIN Company on JobPosting.companyId = Company.companyId 
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# Return all mentees
@orbit.route('/Mentees', methods=['GET'])
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

# Return all advisors
@orbit.route('/Advisors', methods=['GET'])
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

# Return a list of jobs and their information
# GET/JobPosting
@orbit.route('/Users', methods=['GET'])
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


    
# Add new job/co-op opportunities to the database for students to apply to. 
# POST/JobPosting
@orbit.route('/JobPosting', methods=['POST'])
def add_new_product():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    empId = the_data['empId']
    companyId = the_data['companyId']
    role = the_data['role']
    jobDesc = the_data['jobDesc']

    query = f'''
        INSERT INTO JobPosting (empId,
                              companyId,
                              role, 
                              jobDesc)
        VALUES ('{empId}', '{companyId}', '{role}', {jobDesc})
    '''

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

# Remove a job opportunity that is no longer available or hiring. 
# DELETE/JobPosting/<jobId>
@orbit.route('/JobPosting/<jobId>', methods = ['DELETE'])
def delete_job():

    the_data = request.json
    current_app.logger.info(the_data)

    jobId = the_data['jobId']

    query = f'''
        DELETE FROM JobPosting
        WHERE jobId = {jobId}
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Returns mentor and mentee matches
# GET/Match
@orbit.route('/Match', methods=['GET'])
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

# GET the list of mentees matched with a specific mentor
@orbit.route('/MentorMentees/<int:mentorId>', methods=['GET'])

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


# Create matches between mentors and mentees
# POST/Match 
@orbit.route('/Match', methods=['POST'])
def create_match():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    menteeId = the_data['menteeId']
    mentorId = the_data['mentorId']
    

    query = f'''
        INSERT INTO `Match` (menteeId,
                              mentorId)
        VALUES ('{menteeId}', '{mentorId}')
    '''

    current_app.logger.info(query)


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

'''
CHECK THIS ONE IDRK HOW TO WRITE IT WITH NEW VARIABLES
'''
# change matches between mentors and mentees
@orbit.route('/Match', methods = ['PUT'])
def update_match(og_mentorId, og_menteeId, new_mentorId, new_menteeId):
    
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    menteeId = the_data['menteeId']
    mentorId = the_data['mentorId']

    query = f'''
    UPDATE `Match`
    SET mentorId = {new_mentorId}, menteeId = {new_menteeId}
    WHERE mentorId = {og_mentorId}, menteeId = {og_menteeId}
    '''

    product_info = request.json
    current_app.logger.info(product_info)

    return "Success"

# delete a match between a mentor and mentee
@orbit.route('/Match', methods = ['DELETE'])
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
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# return a list of applications for a specific position
@orbit.route('/Applications/<jobId>', methods=['GET'])
def return_spec_apps():

    the_data = request.json
    current_app.logger.info(the_data)

    jobId = the_data['jobId']

    query = f'''
        SELECT  *
        FROM Applications
        WHERE jobId = {jobId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# submit an application to a specific job
@orbit.route('/Applications/<jobId>', methods=['POST'])
def add_application():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    jobId = the_data['jobId']
    studentId = the_data['studentId']
    

    query = f'''
        INSERT INTO Applications (studentId,
                              jobId)
        VALUES ('{studentId}', '{jobId}')
    '''

    current_app.logger.info(query)


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

# withdraw an application
@orbit.route('/Applications/<jobId>', methods = ['DELETE'])
def delete_application():

    the_data = request.json
    current_app.logger.info(the_data)

    studentId = the_data['studentId']
    jobId = the_data['jobId']

    query = f'''
        DELETE FROM Applications
        WHERE studentId = {studentId} AND jobId = {jobId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Return a list of current mentors
@orbit.route('/Mentor', methods=['GET'])
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

# add a mentor to the platform
#####
#### NOT WORKING YET
######
@orbit.route('/Mentor', methods=['POST'])
def add_mentor():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    mentorId = the_data['userId']
    

    query = f'''
        INSERT INTO Applications (mentorId)
        VALUES ('{mentorId}')
    '''

    current_app.logger.info(query)


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

# remove a mentor from the system
@orbit.route('/Mentor', methods = ['DELETE'])
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
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# return user information 
@orbit.route('/User', methods=['GET'])
def return_user_info():
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

# remove users that are no longer active or to whom the platform does not suit
@orbit.route('/User', methods = ['DELETE'])
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
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# return all chat logs between all users
@orbit.route('/Chats', methods=['GET'])
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

# returns a list of networking events and information
@orbit.route('/Events', methods=['GET'])
def return_events():
    query = '''
        SELECT  *
        FROM Events
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# remove an event from the schedule
@orbit.route('/Events', methods = ['DELETE'])
def delete_event():

    the_data = request.json
    current_app.logger.info(the_data)

    eventId = the_data['eventId']

    query = f'''
        DELETE FROM Events
        WHERE userId = {eventId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
        
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# returns information about a specific application for a position
@orbit.route('/Applications/<userId>', methods=['GET'])
def return_applicant():

    the_data = request.json
    current_app.logger.info(the_data)

    userId = the_data['userId']

    query = f'''
        SELECT  *
        FROM Applications a JOIN Users u ON a.studentId = u.userId
        WHERE userId = {userId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@orbit.route('/Metrics/<menteeId>', methods=['GET'])
def view_mentee_progress():

    the_data = request.json
    current_app.logger.info(the_data)

    menteeId = the_data['menteeId']

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