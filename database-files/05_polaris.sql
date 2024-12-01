DROP DATABASE IF EXISTS polaris;
CREATE DATABASE polaris;
USE polaris;

-- Drop tables in reverse order of dependencies
DROP TABLE IF EXISTS Chats;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Applications;
DROP TABLE IF EXISTS JobPosting;
DROP TABLE IF EXISTS `Match`;
DROP TABLE IF EXISTS Mentor;
DROP TABLE IF EXISTS Mentee;
DROP TABLE IF EXISTS Advisor;
DROP TABLE IF EXISTS Employer;
DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `Events`;
DROP TABLE IF EXISTS Metrics;


CREATE TABLE `User` (
    userId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    profilepic VARCHAR(255),
    college VARCHAR(100),
    major VARCHAR(100),
    minor VARCHAR(100)
);

CREATE TABLE Advisor (
    advisorId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    department VARCHAR(100),
    FOREIGN KEY (userid) REFERENCES `User`(userid)
);

CREATE Table Company (
    companyId INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    bio TEXT
);
CREATE TABLE Employer (
    empId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    companyId INT NOT NULL,
    role VARCHAR(100),
    FOREIGN KEY (companyId) REFERENCES Company(companyId),
    FOREIGN KEY (userId) REFERENCES `User`(userId)
);

CREATE TABLE Mentor (
    mentorId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    isWorking BOOLEAN,
    isInSchool BOOLEAN,
    company VARCHAR(100),
    currentPosition VARCHAR(100),
    advisorId INT,
    FOREIGN KEY (userId) REFERENCES `User`(userId),
    FOREIGN KEY (advisorId) REFERENCES Advisor(advisorId)
);

CREATE TABLE Mentee (
    menteeId INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    bio TEXT,
    resume TEXT,
    FOREIGN KEY (userId) REFERENCES `User`(userId)
);

CREATE TABLE `Match` (
    matchId INT AUTO_INCREMENT PRIMARY KEY,
    mentorId INT NOT NULL,
    menteeId INT NOT NULL,
    FOREIGN KEY (mentorId) REFERENCES Mentor(mentorId),
    FOREIGN KEY (menteeId) REFERENCES Mentee(menteeId)
);



CREATE TABLE JobPosting (
    jobNum INT AUTO_INCREMENT PRIMARY KEY,
    empId INT NOT NULL,
    companyId INT NOT NULL,
    role VARCHAR(100),
    jobDesc TEXT,
    filledBool BOOLEAN,
    FOREIGN KEY (empId) REFERENCES Employer(empId)
        ON DELETE CASCADE,
    FOREIGN KEY (companyId) REFERENCES Company(companyId)
        ON DELETE CASCADE
);

CREATE TABLE Applications (
    studentId INT NOT NULL,
    jobId INT NOT NULL,
    empId INT NOT NULL,
    completed BOOLEAN,
    timeApplied DATETIME,
    FOREIGN KEY (studentId) REFERENCES Mentee(menteeId)
        ON DELETE CASCADE,
    FOREIGN KEY (jobId) REFERENCES JobPosting(jobNum)
        ON DELETE CASCADE,
    FOREIGN KEY (empId) REFERENCES Employer(empId)
        ON DELETE CASCADE
);

CREATE TABLE Chats (
    messageId INT AUTO_INCREMENT PRIMARY KEY,
    senderId INT NOT NULL,
    recipientId INT NOT NULL,
    text TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (senderId) REFERENCES `User`(userId),
    FOREIGN KEY (recipientId) REFERENCES `User`(userId)
);

CREATE TABLE `Events` (
    eventId INT NOT NULL AUTO_INCREMENT,
    speakerId INT NOT NULL,
    organizerId INT NOT NULL,
    speakerName VARCHAR(50) NOT NULL,
    industry VARCHAR(100) NOT NULL,
    `when` DATETIME NOT NULL,
    PRIMARY KEY(eventId, organizerId),
    FOREIGN KEY (speakerId) REFERENCES Employer(empId),
    FOREIGN KEY (organizerId) REFERENCES Advisor(advisorId)
);

CREATE TABLE Metrics (
    mentorId INT NOT NULL,
    menteeId INT NOT NULL,
    progressNotes TEXT NOT NULL,
    adjustmentNotes TEXT NOT NULL,
    PRIMARY KEY(mentorId, menteeId),
    FOREIGN KEY (mentorId) REFERENCES Mentor(mentorId),
    FOREIGN KEY (menteeId) REFERENCES Mentee(menteeId)
);