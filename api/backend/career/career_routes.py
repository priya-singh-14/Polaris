
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
# JobPostings, Applications, Events, Companies
career = Blueprint('career', __name__)



@career.route('/updateEvent', methods=['PUT'])
def update_event_data():
    
    the_data = request.json
    inviteAccepted = 1 if the_data['inviteAccepted'] else 0 

    query = f'''
        UPDATE Events 
        SET inviteAccepted = %s
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (inviteAccepted))
    db.get_db().commit()

    response = make_response("Successfully updated profile")
    response.status_code = 200
    return response


# Return a list of jobs and their information
# GET/JobPosting
@career.route('/JobPosting', methods=['GET'])
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



@career.route('/Applications', methods=['GET'])
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


# Return all jobs posted by a specific employer
@career.route('/EmployerJobs/<int:empId>', methods=['GET'])
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

@career.route('/NewJobPosting', methods=['POST'])
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
    majors = the_data['majors']

    query = '''
        INSERT INTO JobPosting (empId, companyId, role, jobDesc, majors, filledbool)
        VALUES (%s, %s, %s, %s, %s, %s )
    '''

    current_app.logger.info(query)

    # executing and committing the insert statement 
    cursor = db.get_db().cursor()
    cursor.execute(query, (empId, companyId, role, jobDesc, majors, filledBool))
    db.get_db().commit()
    
    response = make_response("Successfully added position")
    response.status_code = 200
    return response

# Remove a job opportunity that is no longer available or hiring. 
# DELETE/JobPosting/<jobId>
@career.route('/DeleteJobPosting', methods = ['DELETE'])
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
    db.get_db().commit()
        
    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response


# return a list of applications for a specific position
@career.route('/JobApplications/<int:jobNum>', methods=['GET'])
def return_spec_apps(jobNum):

    query = f'''
        SELECT User.name, User.major, User.minor, User.email, Applications.timeApplied, Mentee.resume, Mentee.menteeId
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
@career.route('/NewApplications', methods=['POST'])
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
@career.route('/DeleteApplication', methods = ['DELETE'])
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

@career.route('/MatchingJobs/<int:menteeId>', methods=['GET'])
def match_jobs_to_mentee(menteeId):

    query = f'''
        SELECT jp.role, jp.jobDesc
        FROM JobPosting jp JOIN Mentee m Join User on m.userId = User.userId 
        ON jp.majors LIKE CONCAT('%', User.major, '%') 
        OR jp.majors LIKE CONCAT('%', User.minor, '%')
        WHERE m.menteeId = {menteeId}
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

@career.route('/Events', methods=['GET'])
def return_events():
    query = '''
        SELECT  *
        FROM Events
        WHERE Events.inviteAccepted = TRUE
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# returns a list of networking events and information
@career.route('/Events/<date>', methods=['GET'])
def return_events_on_date(date):
    
    input_date = datetime.strptime(date, '%Y-%m-%d')
    query = '''
            SELECT *
            FROM Events
            WHERE DATE(Events.when) = %s and Events.inviteAccepted = TRUE
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (input_date.strftime('%Y-%m-%d'),))
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# returns a list of networking events and information
@career.route('/PendingEvents/<int:empId>', methods=['GET'])
def return_events_for_emp(empId):
    
    query = f'''
            SELECT *
            FROM Events Join Advisor on Events.organizerId = Advisor.advisorId 
            Join User on Advisor.userId = User.userId
            WHERE Events.speakerId = {empId} and Events.inviteAccepted = FALSE
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# returns a list of networking events and information
@career.route('/Events/<int:empId>', methods=['GET'])
def return_confirmed_events_for_emp(empId):
    
    query = f'''
            SELECT *
            FROM Events Join Advisor on Events.organizerId = Advisor.advisorId 
            Join User on Advisor.userId = User.userId
            WHERE Events.speakerId = {empId} and Events.inviteAccepted = TRUE
        '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# remove an event from the schedule
@career.route('/DeleteEvent', methods = ['DELETE'])
def delete_event():

    the_data = request.json
    current_app.logger.info(the_data)

    eventId = the_data['eventId']

    query = f'''
        DELETE FROM Events
        WHERE eventId = {eventId};
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
        
    response = make_response(jsonify(the_data))
    response.status_code = 200
    return response

# returns information about a specific application for a position
@career.route('/Applications/<int:menteeId>', methods=['GET'])
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

@career.route('/createEvent', methods=['POST'])
def createEvent():
    the_data = request.json
    current_app.logger.info(the_data)

    speakerId = the_data['speakerId']
    organizerId = the_data['organizerId']
    speakerName = the_data['speakerName']
    industry = the_data['industry']
    when = the_data['when']
    inviteAccepted = False

    query = '''
        INSERT INTO Events (speakerId, organizerId, speakerName, industry, `when`, inviteAccepted)
        VALUES (%s, %s, %s, %s, %s, %s)
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query, (speakerId, organizerId, speakerName, industry, when, inviteAccepted) ) 
    db.get_db().commit()

    response = make_response("Successfully scheduled event")
    response.status_code = 200
    return response

# generate event id
@career.route('/generateEventId', methods=['GET'])
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

@career.route('/Applications/<jobId>', methods=['GET'])
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

@career.route('/ApplicationTotal/<int:menteeId>', methods=['GET'])
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

@career.route('/Companies', methods=['GET'])
def view_all_companies():
    query = '''
        SELECT companyId, name, bio
        FROM Company
    '''

    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()

    response = make_response(jsonify(theData))
    response.status_code = 200
    
    return response