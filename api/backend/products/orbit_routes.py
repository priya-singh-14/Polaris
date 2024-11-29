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
orbit = Blueprint('orbit_db', __name__)

# Return a list of jobs and their information
# GET/JobPosting
@orbit.route('/JobPosting', methods=['GET'])
def get_job_postings():
    query = '''
        SELECT  *
        FROM JobPosting
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
def delete_job(jobId):
    query = '''
        DELETE FROM JobPosting
        WHERE jobId = {str(jobId)}
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

# ------------------------------------------------------------
# This is a stubbed route to update a product in the catalog
# The SQL query would be an UPDATE. 
@products.route('/product', methods = ['PUT'])
def update_product():
    product_info = request.json
    current_app.logger.info(product_info)

    return "Success"