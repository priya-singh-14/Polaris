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
    eventId INT NOT NULL,
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

INSERT INTO User (name, email, profilepic, college, major, minor)
VALUES
    ('Tyler Dipper', 'dipper.t@example.com', 'tyler.jpg', 'Khoury', 'Computer Science', 'Math'),
    ('Sara Star', 'star.s@example.com', 'sara.jpg', 'Khoury', 'Cybersecurity', NULL),
    ('Billy Blakhole', 'blakhole.b@example.com', 'billy.jpg', 'Khoury', NULL, NULL),
    ('John Aquarius', 'aquarius.j@example.com', 'john.jpg', NULL, NULL, NULL),
    ('Sandra Cao', 'cao.s@example.com', 'sandra.jpg', 'Khoury', 'Data Science', 'Design'),
    ('Ava Knight', 'knight.a@example.com', 'ava.jpg', 'Khoury', 'Cybersecurity', NULL),
    ('Lucas Gay', 'gay.l@example.com', 'lucas.jpg', 'Khoury', NULL, NULL),
    ('Priya Singh', 'singh.p@example.com', 'priya.jpg', NULL, NULL, NULL);

INSERT INTO Advisor (userid, department)
VALUES
    (3, 'Computer Science'),
    (7, 'Computer Science');

INSERT INTO Company (name, bio)
VALUES
    ('Google', 'At Google, we believe in designing for the future.'),
    ('Meta', 'At Meta, we want aspiring developers who think outside the box.');

INSERT INTO Employer (userid, companyId, role)
VALUES
    (4, 1, 'Manager'),
    (8, 2, 'CEO');

INSERT INTO Mentor (userid, isWorking, isInSchool, company, currentPosition, advisorId)
VALUES
    (2, TRUE, FALSE, 'Tesla', 'Senior Engineer', 1),
    (6, TRUE, FALSE, 'Microsoft', 'Junior Engineer', 2);

INSERT INTO Mentee (userid, bio, resume)
VALUES
    (1, 'Aspiring developer interested in tech startups.', 'resume_tyler.pdf'),
    (5, 'Designer and Developer, looking for UX roles.', 'resume_sandra.pdf');

INSERT INTO `Match` (mentorId, menteeId)
VALUES
    (1, 1),
    (1, 2);


INSERT INTO JobPosting (empId, companyId, role, jobDesc, filledBool)
VALUES
    (1, 1, 'Intern', 'Frontend intern role at Google.', FALSE),
    (2, 2, 'Co-op', 'DevOps Co-op role at Meta.', FALSE);

INSERT INTO Applications (studentId, jobId, empId, completed, timeApplied)
VALUES
    (1, 1, 1, FALSE, '2024-11-01 09:00:00'),
    (1, 2, 1, FALSE, '2024-11-07 09:00:00'),
    (2, 2, 2, FALSE, '2024-11-01 07:00:00');

INSERT INTO Chats (senderId, recipientId, text)
VALUES
    (1, 2, 'Hi Sara, can you help me with my application?'),
    (2, 1, 'Sure, Tyler! Let me know the details.'),
    (6, 5, 'Here is a role that I thought would be a good fit!'),
    (5, 6, 'Thanks! I will take a look!');

INSERT INTO Events (eventID, speakerID, organizerID, speakerName, industry, `when`)
VALUES
    (1, 1, 1, 'John Aquarius', 'Finance and Community Relations', '2024-12-01 10:00:00');