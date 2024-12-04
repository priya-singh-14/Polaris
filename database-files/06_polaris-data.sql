SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

USE polaris;

INSERT INTO User (name, email, profilepic, college, major, minor)
VALUES
    ('Isla North', 'north.i@example.com', 'isla.jpg', 'Khoury', 'Computer Science', NULL),
    ('Andy Romeda', 'romeda.a@example.com', 'andy.jpg', 'Khoury', 'Cybersecurity', NULL),
    ('Billy Blakhole', 'blakhole.b@example.com', 'billy.jpg', 'Khoury', NULL, NULL),
    ('John Aquarius', 'aquarius.j@example.com', 'john.jpg', NULL, NULL, NULL),

    ('Sandra Cao', 'cao.s@example.com', 'sandra.jpg', 'Khoury', 'Data Science', 'Design'),
    ('Ava Knight', 'knight.a@example.com', 'ava.jpg', 'Khoury', 'Cybersecurity', NULL),
    ('Lucas Gay', 'gay.l@example.com', 'lucas.jpg', 'Khoury', NULL, NULL),
    ('Priya Singh', 'singh.p@example.com', 'priya.jpg', NULL, NULL, NULL),

    ('James Night', 'night.j@example.com', 'james.jpg', 'College of Engineering', 'Data Science', 'Finance'),
    ('Oliver Brooks', 'brooks.o@example.com', 'oliver.jpg', 'College of Arts, Media, and Design', 'Graphic Design', 'Psychology'),
    ('Sophia Lane', 'lane.s@example.com', 'sophia.jpg', 'College of Engineering', NULL, NULL),
    ('Liam West', 'west.l@example.com', 'liam.jpg', NULL, NULL, NULL),
    
    ('Emily Davis', 'davis.e@example.com', 'emily.jpg', 'Khoury', 'Cybersecurity', 'Business'),
    ('Ethan Hill', 'hill.e@example.com', 'ethan.jpg', 'College of Science', 'Physics', NULL),
    ('Chloe Kim', 'kim.c@example.com', 'chloe.jpg', 'College of Science', NULL, NULL),
    ('Noah Green', 'green.n@example.com', 'noah.jpg', NULL, NULL, NULL),
    
    ('Miley Carter', 'carter.m@example.com', 'miley.jpg', 'College of Engineering', 'Electrical Engineering', 'Computer Science'),
    ('Michael Brown', 'brown.m@example.com', 'michael.jpg', 'D''Amore-McKim', 'Marketing', NULL),
    ('Sophia Turner', 'turner.s@example.com', 'sophia.jpg', 'D''Amore-McKim', NULL, NULL),
    ('Ryan Davis', 'davis.r@example.com', 'ryan.jpg', NULL, NULL, NULL),
    
    ('Olivia Martin', 'martin.o@example.com', 'olivia.jpg', 'Khoury', 'Computer Science', 'Psychology'),
    ('Luis Wilson', 'wilson.l@example.com', 'luis.jpg', 'College of Social Sciences and Humanities', 'Philosophy', NULL),
    ('Charlotte Lee', 'lee.c@example.com', 'charlotte.jpg', 'Khoury', NULL, NULL),
    ('Aiden White', 'white.a@example.com', 'aiden.jpg', NULL, NULL, NULL),
    
    ('Amelia Harris', 'harris.a@example.com', 'amelia.jpg', 'Khoury', 'Computer Science', NULL),
    ('Nolan Clark', 'clark.n@example.com', 'nolan.jpg', 'College of Science', 'Physics', 'Mathematics'),
    ('Mia Lewis', 'lewis.m@example.com', 'mia.jpg', 'College of Arts, Media, and Design', NULL, NULL),
    ('Benjamin Walker', 'walker.b@example.com', 'benjamin.jpg', NULL, NULL, NULL),
    
    ('Harper Hall', 'hall.h@example.com', 'harper.jpg', 'D''Amore-McKim', 'Entrepreneurship', 'International Business'),
    ('Luca Allen', 'allen.l@example.com', 'luca.jpg', 'Bouve College of Health Sciences', 'Environmental Science', 'Data Analysis'),
    ('Ella Young', 'young.e@example.com', 'ella.jpg', 'Bouve College of Health Sciences', 'Radiology', NULL),
    ('Jack Hernandez', 'hernandez.j@example.com', 'jack.jpg', NULL, NULL, NULL),
    
    ('Avery King', 'king.a@example.com', 'avery.jpg', 'College of Arts', 'Film Studies', 'Cultural Studies'),
    ('Mason Scott', 'scott.m@example.com', 'mason.jpg', 'Khoury', 'Data Science', 'Statistics'),
    ('Isabella Rivera', 'rivera.i@example.com', 'isabella.jpg', 'College of Science', NULL, NULL),
    ('Marcus Green', 'green.l@example.com', 'marcus.jpg', NULL, NULL, NULL),

    ('Elliot Harper', 'elliot.h@example.com', 'elliot.jpg', 'Khoury', 'Computer Science', NULL),
    ('Maria Torres', 'sophia.t@example.com', 'maria.jpg', 'College of Science', 'Mathematics', 'Statistics'),
    ('Josh Patel', 'liam.p@example.com', 'josh.jpg', 'College of Engineering', NULL, NULL),
    ('Aria Mitchell', 'ava.m@example.com', 'aria.jpg', NULL, NULL, NULL),

    ('Bella Cruz', 'bella.c@example.com', 'bella.jpg', 'College of Business', 'Finance', 'Economics'),
    ('Jason Rivera', 'jason.r@example.com', 'jason.jpg', 'College of Science', 'Biology', 'Environmental Studies'),
    ('Sia Ross', 'sia.r@example.com', 'sia.jpg', 'Khoury', NULL, NULL),
    ('Cain Greek', 'cain.g@example.com', 'cain.jpg', NULL, NULL, NULL),
    
    ('Olive Carter', 'olive.c@example.com', 'olive.jpg', 'College of Arts', 'Creative Writing', NULL),
    ('Sora Perez', 'sora.p@example.com', 'sora.jpg', 'Khoury', 'Artificial Intelligence', NULL),
    ('Mina Scott', 'mina.s@example.com', 'mina.jpg', 'Bouve College of Health Sciences', 'Nursing', NULL),
    ('Lou Edwards', 'lou.e@example.com', 'lou.jpg', NULL, NULL, NULL),
    
    ('Charlotte Kelly', 'charlotte.k@example.com', 'charlotte.jpg', 'College of Engineering', 'Chemical Engineering', 'Materials Science'),
    ('Benjamin Lee', 'benjamin.l@example.com', 'benjamin.jpg', 'Khoury', 'Software Engineering', NULL),
    ('Emmalie Walker', 'emmalie.w@example.com', 'emmalie.jpg', 'D''Amore McKim', NULL, NULL),
    ('Mike Young', 'mike.y@example.com', 'mike.jpg', NULL, NULL, NULL),
   
    ('Nicole Bennett', 'nicole.b@example.com', 'nicole.jpg', 'Khoury', 'Cybersecurity', NULL),
    ('Dev James', 'dev.j@example.com', 'dev.jpg', 'College of Science', 'Neuroscience', NULL),
    ('Niki Morris', 'niki.m@example.com', 'niki.jpg', 'College of Social Sciences and Humanities', NULL, NULL),
    ('Eve Brooks', 'eve.b@example.com', 'eve.jpg', NULL, NULL, NULL);

INSERT INTO Advisor (userid, department)
VALUES
    (3, 'Khoury'),
    (7, 'Khoury'),
    (11, 'College of Engineering'),
    (15, 'College of Science'),
    (19, 'D''Amore McKim'),
    (23, 'Khoury'),
    (27, 'College of Arts, Media, and Design'),
    (31, 'Bouve College of Health Sciences'),
    (35, 'College of Science'),
    (39, 'College of Engineering'),
    (43, 'Khoury'),
    (47, 'Bouve College of Health Sciences'),
    (51, 'D''Amore McKim'),
    (55, 'College of Social Sciences and Humanities');
     

INSERT INTO Company (name, bio)
VALUES
    ('Google', 'At Google, we believe in solving big problems with innovative technology.'),
    ('Meta', 'At Meta, we want aspiring developers to shape the future of digital connection.'),
    ('Microsoft', 'Empowering every person and organization on the planet to achieve more.'),
    ('Labcorp', 'Leading the future of healthcare through diagnostics and innovation.'),
    ('Coca-Cola', 'Refreshing the world and making a difference with our iconic beverages.'),
    ('Adobe', 'We enable creativity and innovation for everyone, everywhere.'),
    ('Mass General', 'Advancing healthcare and improving lives through cutting-edge research and care.'),
    ('NVIDIA', 'Revolutionizing industries with accelerated computing and AI.'),
    ('OpenAI', 'Creating artificial intelligence that benefits all of humanity.'),
    ('Salesforce', 'Connecting businesses and customers through cloud-based solutions.'),
    ('RWJ', 'Innovating for healthier communities through research and clinical care.'),
    ('Northeastern University', 'Empowering experiential learning and innovation in education.'),
    ('Tesla', 'Accelerating the world’s transition to sustainable energy.'),
    ('Amazon', 'Delivering customer obsession with unmatched speed and scale.'),
    ('Spotify', 'Bringing music and podcasts to life for billions of listeners.'),
    ('Intel', 'Engineering tomorrow’s technology for a connected world.'),
    ('Disney', 'Creating magical experiences for audiences around the globe.'),
    ('Apple', 'Innovating technology to enrich people’s lives.'),
    ('SpaceX', 'Making life multiplanetary through groundbreaking space exploration.'),
    ('Pfizer', 'Innovating for breakthroughs that change patients’ lives.');


INSERT INTO Employer (userid, companyId, role)
VALUES
    (4, 1, 'Manager'),
    (8, 2, 'CEO'),
    (12, 3, 'Senior Engineer'),
    (16, 4, 'Healthcare Consultant'),
    (20, 5, 'Marketing Strategist'),
    (24, 6, 'Creative Director'),
    (28, 7, 'Clinical Researcher'),
    (32, 8, 'AI Researcher'),
    (36, 9, 'Product Manager'),
    (40, 10, 'Sales Executive'),
    (44, 11, 'Data Scientist'),
    (48, 12, 'University Liaison'),
    (52, 13, 'Energy Engineer'),
    (56, 14, 'Logistics Coordinator');

INSERT INTO Mentor (userid, isWorking, isInSchool, company, currentPosition, advisorId)
VALUES
    (2, TRUE, FALSE, 'Tesla', 'Data Analyst', 1),
    (6, TRUE, FALSE, 'Microsoft', 'Junior Engineer', 2),
    (10, FALSE, TRUE, NULL, NULL, 7),
    (14, TRUE, FALSE, 'LabCorp', 'Physicist', 4),
    (18, TRUE, FALSE, 'Coca-Cola', 'Market Researcher', 5),
    (22, FALSE, FALSE, NULL, NULL, 14),
    (26, TRUE, FALSE, 'Adobe', 'Graphic Designer', 7),
    (30, TRUE, FALSE, 'Mass General', 'PA', 8),
    (34, TRUE, FALSE, 'NVIDIA', 'Data Analyst', 1),
    (38, TRUE, FALSE, 'Microsoft', 'Junior Engineer', 2),
    (42, TRUE, FALSE, 'OpenAI', 'Product Strategist', 4),
    (46, TRUE, FALSE, 'RWJ', 'Intern', 8),
    (50, FALSE, FALSE, NULL, NULL, 2),
    (54, TRUE, FALSE, 'Northeastern University', 'Lab Assistant', 4);

INSERT INTO Mentee (userid, bio, resume)
VALUES
    (1, 'Aspiring developer interested in tech startups.', 'resume_isla.pdf'),
    (5, 'Designer and Developer, looking for UX roles.', 'resume_sandra.pdf'),
    (9, 'Keen on bridging the gap between technology and sustainable finance.', 'resume_default.pdf'),
    (13, 'Motivated to explore machine learning applications in healthcare.', 'resume_default.pdf'),
    (17, 'Passionate about creating innovative cybersecurity solutions.', 'resume_default.pdf'),
    (21, 'Focused on building efficient and scalable software systems.', 'resume_default.pdf'),
    (25, 'Aiming to merge graphic design and user experience principles.', 'resume_default.pdf'),
    (29, 'Driven to excel in full-stack development for e-commerce platforms.', 'resume_default.pdf'),
    (33, 'Enthusiastic about marine conservation technologies and data analysis.', 'resume_default.pdf'),
    (37, 'Excited to explore HCI and accessibility in web applications.', 'resume_default.pdf'),
    (41, 'Interested in renewable energy and sustainable engineering practices.', 'resume_default.pdf'),
    (45, 'Aspiring entrepreneur with a focus on digital transformation.', 'resume_default.pdf'),
    (49, 'Fascinated by the interplay of finance and artificial intelligence.', 'resume_default.pdf'),
    (53, 'Eager to contribute to advancements in space technology and physics.', 'resume_default.pdf');

INSERT INTO `Match` (mentorId, menteeId)
VALUES
    (1, 1),
    (1, 2),
    (2, 5),
    (2, 9),
    (3, 13),
    (3, 17),
    (4, 21),
    (4, 25),
    (5, 29),
    (5, 33),
    (6, 37),
    (6, 41),
    (7, 45),
    (7, 49),
    (8, 53),
    (8, 29),
    (9, 33),
    (9, 45),
    (10, 1),
    (10, 5),
    (11, 9),
    (11, 21),
    (12, 13),
    (12, 25),
    (13, 29),
    (13, 37),
    (14, 41),
    (14, 49),
    (15, 53),
    (15, 17),
    (16, 21),
    (16, 45),
    (17, 33),
    (17, 5),
    (18, 25),
    (18, 29),
    (19, 37),
    (19, 41),
    (20, 49),
    (20, 1),
    (21, 9),
    (21, 45);


INSERT INTO JobPosting (empId, companyId, role, jobDesc, filledBool)
VALUES
    (1, 1, 'Intern', 'Frontend intern role at Google.', FALSE),
    (2, 2, 'Co-op', 'DevOps Co-op role at Meta.', FALSE),
    (3, 3, 'Software Engineer', 'Join Microsoft’s team to build scalable software solutions.', FALSE),
    (4, 4, 'Healthcare Analyst', 'Work with Labcorp to analyze healthcare data and improve diagnostics.', FALSE),
    (5, 5, 'Brand Manager', 'Join Coca-Cola’s team to drive brand growth and market strategies.', FALSE),
    (6, 6, 'Junior Designer', 'Help Adobe design creative assets for a variety of digital platforms.', FALSE),
    (7, 7, 'Clinical Trial Assistant', 'Assist in clinical research at Mass General, supporting trial operations.', FALSE),
    (8, 8, 'Machine Learning Engineer', 'Help NVIDIA develop AI-driven technologies for diverse industries.', FALSE),
    (9, 9, 'AI Research Intern', 'Join OpenAI to contribute to innovative AI research and development.', FALSE),
    (10, 10, 'Sales Engineer', 'Support Salesforce customers by providing tailored technical solutions.', FALSE),
    (11, 11, 'Clinical Research Intern', 'Contribute to research projects focused on health innovation at RWJ.', FALSE),
    (12, 12, 'Research Assistant', 'Assist Northeastern University’s faculty in cutting-edge research projects.', FALSE),
    (13, 13, 'Sustainability Engineer', 'Work with Tesla to develop sustainable energy solutions.', FALSE),
    (14, 14, 'Software Developer', 'Join Amazon’s software development team to build scalable applications.', FALSE),
    (1, 1, 'UX/UI Design Intern', 'Collaborate with Google’s design team to create seamless user experiences for web and mobile applications.', FALSE),
    (2, 2, 'Cloud Solutions Co-op', 'Work with Meta’s cloud infrastructure team to design and implement scalable cloud solutions.', FALSE),
    (3, 3, 'Backend Software Engineer', 'Join Microsoft’s engineering team to develop robust and scalable backend services for enterprise applications.', FALSE),
    (4, 4, 'Medical Data Scientist', 'Analyze large healthcare datasets at Labcorp to improve diagnostic models and patient outcomes.', FALSE),
    (5, 5, 'Digital Marketing Manager', 'Lead Coca-Cola’s digital marketing strategies to engage customers and enhance brand awareness through digital channels.', FALSE),
    (6, 6, 'Visual Designer', 'Help Adobe design compelling visual experiences across digital platforms, focusing on branding and user interfaces.', FALSE),
    (7, 7, 'Clinical Research Coordinator', 'Support Mass General’s clinical research projects, ensuring trials are conducted efficiently and in compliance with regulations.', FALSE),
    (8, 8, 'AI Research Scientist', 'Join NVIDIA’s AI research team to create cutting-edge algorithms for machine learning and artificial intelligence solutions.', FALSE),
    (9, 9, 'AI Ethics Intern', 'Contribute to OpenAI’s research on ethical AI development, ensuring responsible and fair use of AI technologies.', FALSE),
    (10, 10, 'Customer Solutions Engineer', 'Work at Salesforce to provide technical support and create solutions for clients using Salesforce’s cloud platform.', FALSE),
    (11, 11, 'Healthcare Policy Intern', 'Assist in developing policy recommendations at RWJ, focusing on healthcare innovation and access improvement.', FALSE),
    (12, 12, 'Innovation Research Assistant', 'Assist Northeastern University’s research teams in exploring cutting-edge innovations in technology and education.', FALSE),
    (13, 13, 'Energy Systems Engineer', 'Collaborate with Tesla’s engineering team to develop and optimize energy storage and sustainable energy systems.', FALSE),
    (14, 14, 'Web Developer', 'Join Amazon’s engineering team to build and maintain web applications that improve the shopping experience for millions of users.', FALSE);

INSERT INTO Applications (studentId, jobId, empId, completed, timeApplied)
VALUES
    (1, 1, 1, FALSE, '2024-11-01 09:00:00'),
    (1, 2, 2, FALSE, '2024-11-07 09:00:00'),
    (1, 3, 3, FALSE, '2024-11-02 08:30:00'),
    (2, 4, 4, FALSE, '2024-11-03 09:15:00'),
    (3, 5, 5, FALSE, '2024-11-04 10:30:00'),
    (4, 6, 6, FALSE, '2024-11-05 11:45:00'),
    (5, 7, 7, FALSE, '2024-11-06 13:15:00'),
    (6, 8, 8, FALSE, '2024-11-07 14:30:00'),
    (7, 9, 9, FALSE, '2024-11-01 15:00:00'),
    (8, 10, 10, FALSE, '2024-11-02 16:00:00'),
    (9, 11, 11, FALSE, '2024-11-03 17:00:00'),
    (10, 12, 12, FALSE, '2024-11-04 18:00:00'),
    (11, 13, 13, FALSE, '2024-11-05 19:00:00'),
    (12, 14, 14, FALSE, '2024-11-06 20:00:00'),
    (13, 1, 1, FALSE, '2024-11-07 09:30:00'),
    (14, 2, 2, FALSE, '2024-11-01 07:00:00'),
    (1, 4, 4, FALSE, '2024-11-02 09:15:00'),
    (2, 5, 5, FALSE, '2024-11-03 10:00:00'),
    (3, 6, 6, FALSE, '2024-11-04 11:15:00'),
    (4, 7, 7, FALSE, '2024-11-05 12:30:00'),
    (5, 8, 8, FALSE, '2024-11-06 13:45:00'),
    (6, 9, 9, FALSE, '2024-11-07 14:00:00'),
    (7, 10, 10, FALSE, '2024-11-01 15:15:00'),
    (8, 11, 11, FALSE, '2024-11-02 16:30:00'),
    (9, 12, 12, FALSE, '2024-11-03 17:30:00'),
    (10, 13, 13, FALSE, '2024-11-04 18:45:00'),
    (11, 14, 14, FALSE, '2024-11-05 19:15:00'),
    (12, 1, 1, FALSE, '2024-11-06 20:30:00'),
    (13, 2, 2, FALSE, '2024-11-07 21:00:00'),
    (14, 3, 3, FALSE, '2024-11-01 08:00:00');

INSERT INTO Chats (senderId, recipientId, text)
VALUES
    (1, 2, 'Hi Andy, can you help me with my application?'),
    (2, 1, 'Sure, Isla! Let me know the details.'),
    (6, 5, 'Here is a role that I thought would be a good fit!'),
    (5, 6, 'Thanks! I will take a look!');

INSERT INTO Events (eventID, speakerID, organizerID, speakerName, industry, `when`)
VALUES
    (1, 1, 1, 'John Aquarius', 'Finance and Community Relations', '2024-12-01 10:00:00');
