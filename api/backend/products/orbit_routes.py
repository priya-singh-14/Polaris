
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


@orbit.route('/updateUser', methods=['PUT'])
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

@orbit.route('/updateMentee', methods=['PUT'])
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

@orbit.route('/updateMentor', methods=['PUT'])
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

@orbit.route('/getMenteeData/<int:menteeId>', methods=['GET'])
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

@orbit.route('/Mentees/<string:college>/<string:major>/<string:minor>', methods=['GET'])
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

@orbit.route('/AllMentees', methods=['GET'])
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

@orbit.route('/getMentorData/<int:mentorId>', methods=['GET'])
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

@orbit.route('/createNewMentee', methods=['POST'])
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
    isWorking = 1 if the_data['isWorking'] else 0   
    isInSchool = 1 if the_data['isInSchool'] else 0  
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

# view all mentors
@orbit.route('/viewMentorList', methods=['GET'])
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
        SELECT JobPosting.jobDesc, JobPosting.role, Company.name, JobPosting.empId, JobPosting.jobNum
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

# Return all mentees
@orbit.route('/Applications', methods=['GET'])
def get_applications():
    query = '''
        SELECT  *
        FROM Applications
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Return all employers
@orbit.route('/Employers', methods=['GET'])
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

# Return all jobs posted by a specific employer
@orbit.route('/EmployerJobs/<int:empId>', methods=['GET'])
def get_employer_applications(empId):
    query = f'''
        SELECT  *
        FROM JobPosting
        WHERE JobPosting.empId = '{empId}'
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


# Return the most recently created mentor profile
@orbit.route('/mostRecentMentor', methods=['GET'])
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


# Return the most recently created mentee profile
@orbit.route('/mostRecentMentee', methods=['GET'])
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
@orbit.route('/NewJobPosting', methods=['POST'])
def post_new_job():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    empId = the_data['empId']
    companyId = the_data['companyId']
    role = the_data['role']
    jobDesc = the_data['jobDesc']
    filledBool = the_data['filledBool']

    query = '''
        INSERT INTO JobPosting (empId, companyId, role, jobDesc, filledbool)
        VALUES (%s, %s, %s, %s, %s )
    '''

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query, (empId, companyId, role, jobDesc, filledBool))
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

# Remove a job opportunity that is no longer available or hiring. 
# DELETE/JobPosting/<jobId>
@orbit.route('/JobPosting/<int:jobId>', methods = ['DELETE'])
def delete_job():

    the_data = request.json
    current_app.logger.info(the_data)

    jobId = the_data['jobId']

    query = f'''
        DELETE FROM JobPosting
        WHERE jobNum = {jobId}
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

# Returns mentor assigned to a given mentee 
# GET/Match
@orbit.route('/Match/<int:menteeId>', methods=['GET'])
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
@orbit.route('/MatchMentees', methods=['POST'])
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
@orbit.route('/Match', methods = ['PUT'])
def update_match(og_mentorId, og_menteeId, new_mentorId, new_menteeId):
    
    the_data = request.json
    current_app.logger.info(the_data)

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
@orbit.route('/JobApplications/<int:jobNum>', methods=['GET'])
def return_spec_apps(jobNum):

    query = f'''
        SELECT User.name, User.major, User.minor, Applications.timeApplied, Mentee.resume, Mentee.menteeId
        FROM Applications JOIN Mentee ON Applications.studentId = Mentee.menteeId JOIN User ON Mentee.userId = User.userId
        WHERE jobId = {jobNum}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# submit an application to a specific job
@orbit.route('/NewApplications', methods=['POST'])
def add_application():
    
    # In a POST request, there is a 
    # collecting data from the request object 
    the_data = request.json
    current_app.logger.info(the_data)

    #extracting the variable
    jobId = the_data['jobId']
    empId = the_data['empId']
    completed = 1 if the_data['completed'] else 0 
    studentId = the_data['studentId']
    timeApplied = the_data['timeApplied']
    

    query = f'''
        INSERT INTO Applications (studentId,
                              jobId, empId, completed, timeApplied)
        VALUES ('{studentId}', '{jobId}', '{empId}', '{completed}', '{timeApplied}')
    '''

    current_app.logger.info(query)


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

# withdraw an application
@orbit.route('/DeleteApplication', methods = ['DELETE'])
def delete_application():

    the_data = request.json
    current_app.logger.info(the_data)

    studentId = the_data['studentId']
    jobId = the_data['jobId']

    query = f'''
        DELETE FROM Applications
        WHERE Applications.studentId = {studentId} AND Applications.jobId = {jobId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
        
    response = make_response(jsonify(the_data))
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

@orbit.route('/Mentor', methods=['POST'])
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

# change mentor details
####
####NOT DONE
#####
# @orbit.route('/Mentor/<mentorId>', methods = ['PUT'])
# def update_mentor_details():
    
#     the_data = request.json
#     current_app.logger.info(the_data)

#     query = f'''
#     UPDATE `Match`
#     SET mentorId = {new_mentorId}, menteeId = {new_menteeId}
#     WHERE mentorId = {og_mentorId}, menteeId = {og_menteeId}
#     '''

#     product_info = request.json
#     current_app.logger.info(product_info)

#     return "Success"

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

# remove a mentor from the system
@orbit.route('/Mentee', methods = ['DELETE'])
def delete_mentee():

    the_data = request.json
    current_app.logger.info(the_data)

    menteeId = the_data['menteeId']

    query = f'''
        DELETE FROM Mentee
        WHERE mentorId = {menteeId};
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

# return all chat logs between all users
@orbit.route('/Chats/<int:senderId>/<int:recipientId>', methods=['GET'])
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

@orbit.route('/createNewChat', methods=['POST'])
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

# returns a list of networking events and information
@orbit.route('/Events/<date>', methods=['GET'])
def return_events_on_date(date):
    
    input_date = datetime.strptime(date, '%Y-%m-%d')
    query = '''
            SELECT *
            FROM Events
            WHERE DATE(Events.when) = %s
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (input_date.strftime('%Y-%m-%d'),))
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
@orbit.route('/Applications/<int:menteeId>', methods=['GET'])
def return_applicant(menteeId):

    query = f'''
        SELECT *
        FROM Applications a JOIN Mentee m ON a.studentId = m.menteeId JOIN JobPosting j on a.jobId = j.jobNum JOIN Company c on j.companyId = c.companyId
        WHERE menteeId = {menteeId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


@orbit.route('/Metrics/<int:menteeId>', methods=['GET'])
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

# create an event
@orbit.route('/createEvent', methods=['POST'])
def createEvent():
    the_data = request.json
    current_app.logger.info(the_data)

    eventId = the_data['eventId']
    speakerId = the_data['speakerId']
    organizerId = the_data['organizerId']
    speakerName = the_data['speakerName']
    industry = the_data['industry']
    when = the_data['when']

    query = '''
        INSERT INTO `EVENTS` (eventId, speakerId, organizerId, speakerName, industry, `when`)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (eventId, speakerId, organizerId, speakerName, industry, when) ) 
    db.get_db().commit()

    response = make_response("Successfully scheduled event")
    response.status_code = 200
    return response

# generate event id
@orbit.route('/generateEventId', methods=['GET'])
def generate_event_id():
    cursor = db.get_db().cursor()

    query = '''
        SELECT MAX(eventId) AS max_eventId 
        FROM `Events`
    '''
    cursor.execute(query)
    result = cursor.fetchone()

    new_eventId = result['max_eventId'] + 1

    response = make_response({'new_userID': new_eventId})
    response.status_code = 200
    return response

@orbit.route('/Applications/<jobId>', methods=['GET'])
def view_applications_for_job():

    the_data = request.json
    current_app.logger.info(the_data)

    jobId = the_data['jobId']

    query = f'''
        SELECT *
        FROM Applications
        WHERE jobId = {jobId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@orbit.route('/ApplicationTotal/<int:menteeId>', methods=['GET'])
def view_application_total(menteeId):

    query = f'''
        SELECT COUNT(*) as total
        FROM Applications
        WHERE Applications.studentId = {menteeId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@orbit.route('/createMetric', methods=['POST'])
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