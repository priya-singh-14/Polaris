USE `polaris`;

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