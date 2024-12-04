SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;

USE polaris;

INSERT INTO User (name, email, profilepic, college, major, minor)
VALUES
    ('Isla North', 'north.i@example.com', 'isla.jpg', 'Khoury College of Computer Science', 'Computer Science', NULL),
    ('Andy Romeda', 'romeda.a@example.com', 'andy.jpg', 'Khoury College of Computer Science', 'Cybersecurity', NULL),
    ('Billy Blakhole', 'blakhole.b@example.com', 'billy.jpg', 'Khoury College of Computer Science', NULL, NULL),
    ('John Aquarius', 'aquarius.j@example.com', 'john.jpg', NULL, NULL, NULL),

    ('Sandra Cao', 'cao.s@example.com', 'sandra.jpg', 'Khoury College of Computer Science', 'Data Science', 'Design'),
    ('Ava Knight', 'knight.a@example.com', 'ava.jpg', 'Khoury College of Computer Science', 'Cybersecurity', NULL),
    ('Lucas Gay', 'gay.l@example.com', 'lucas.jpg', 'Khoury College of Computer Science', NULL, NULL),
    ('Priya Singh', 'singh.p@example.com', 'priya.jpg', NULL, NULL, NULL),

    ('James Night', 'night.j@example.com', 'james.jpg', 'College of Engineering', 'Data Science', 'Finance'),
    ('Oliver Brooks', 'brooks.o@example.com', 'oliver.jpg', 'College of Arts, Media, and Design', 'Graphic Design', 'Psychology'),
    ('Sophia Lane', 'lane.s@example.com', 'sophia.jpg', 'College of Engineering', NULL, NULL),
    ('Liam West', 'west.l@example.com', 'liam.jpg', NULL, NULL, NULL),
    
    ('Emily Davis', 'davis.e@example.com', 'emily.jpg', 'Khoury College of Computer Science', 'Cybersecurity', 'Business'),
    ('Ethan Hill', 'hill.e@example.com', 'ethan.jpg', 'College of Science', 'Physics', NULL),
    ('Chloe Kim', 'kim.c@example.com', 'chloe.jpg', 'College of Science', NULL, NULL),
    ('Noah Green', 'green.n@example.com', 'noah.jpg', NULL, NULL, NULL),
    
    ('Miley Carter', 'carter.m@example.com', 'miley.jpg', 'College of Engineering', 'Electrical Engineering', 'Computer Science'),
    ('Michael Brown', 'brown.m@example.com', 'michael.jpg', 'D''Amore-McKim School of Business', 'Marketing', NULL),
    ('Sophia Turner', 'turner.s@example.com', 'sophia.jpg', 'D''Amore-McKim School of Business', NULL, NULL),
    ('Ryan Davis', 'davis.r@example.com', 'ryan.jpg', NULL, NULL, NULL),
    
    ('Olivia Martin', 'martin.o@example.com', 'olivia.jpg', 'Khoury College of Computer Science', 'Computer Science', 'Psychology'),
    ('Luis Wilson', 'wilson.l@example.com', 'luis.jpg', 'College of Social Sciences and Humanities', 'Philosophy', NULL),
    ('Charlotte Lee', 'lee.c@example.com', 'charlotte.jpg', 'Khoury College of Computer Science', NULL, NULL),
    ('Aiden White', 'white.a@example.com', 'aiden.jpg', NULL, NULL, NULL),
    
    ('Amelia Harris', 'harris.a@example.com', 'amelia.jpg', 'Khoury College of Computer Science', 'Computer Science', NULL),
    ('Nolan Clark', 'clark.n@example.com', 'nolan.jpg', 'College of Science', 'Physics', 'Mathematics'),
    ('Mia Lewis', 'lewis.m@example.com', 'mia.jpg', 'College of Arts, Media, and Design', NULL, NULL),
    ('Benjamin Walker', 'walker.b@example.com', 'benjamin.jpg', NULL, NULL, NULL),
    
    ('Harper Hall', 'hall.h@example.com', 'harper.jpg', 'D''Amore-McKim School of Business', 'Entrepreneurship', 'International Business'),
    ('Luca Allen', 'allen.l@example.com', 'luca.jpg', 'Bouve College of Health Sciences', 'Environmental Science', 'Data Analysis'),
    ('Ella Young', 'young.e@example.com', 'ella.jpg', 'Bouve College of Health Sciences', 'Radiology', NULL),
    ('Jack Hernandez', 'hernandez.j@example.com', 'jack.jpg', NULL, NULL, NULL),
    
    ('Avery King', 'king.a@example.com', 'avery.jpg', 'College of Arts, Media, and Design', 'Film Studies', 'Cultural Studies'),
    ('Mason Scott', 'scott.m@example.com', 'mason.jpg', 'Khoury College of Computer Science', 'Data Science', 'Statistics'),
    ('Isabella Rivera', 'rivera.i@example.com', 'isabella.jpg', 'College of Science', NULL, NULL),
    ('Marcus Green', 'green.l@example.com', 'marcus.jpg', NULL, NULL, NULL),

    ('Elliot Harper', 'elliot.h@example.com', 'elliot.jpg', 'Khoury College of Computer Science', 'Computer Science', NULL),
    ('Maria Torres', 'sophia.t@example.com', 'maria.jpg', 'College of Science', 'Mathematics', 'Statistics'),
    ('Josh Patel', 'liam.p@example.com', 'josh.jpg', 'College of Engineering', NULL, NULL),
    ('Aria Mitchell', 'ava.m@example.com', 'aria.jpg', NULL, NULL, NULL),

    ('Bella Cruz', 'bella.c@example.com', 'bella.jpg', 'D''Amore McKim School of Business', 'Finance', 'Economics'),
    ('Jason Rivera', 'jason.r@example.com', 'jason.jpg', 'College of Science', 'Biology', 'Environmental Studies'),
    ('Sia Ross', 'sia.r@example.com', 'sia.jpg', 'Khoury', NULL, NULL),
    ('Cain Greek', 'cain.g@example.com', 'cain.jpg', NULL, NULL, NULL),
    
    ('Olive Carter', 'olive.c@example.com', 'olive.jpg', 'College of Arts, Media, and Design', 'Creative Writing', NULL),
    ('Sora Perez', 'sora.p@example.com', 'sora.jpg', 'Khoury College of Computer Science', 'Artificial Intelligence', NULL),
    ('Mina Scott', 'mina.s@example.com', 'mina.jpg', 'Bouve College of Health Sciences', 'Nursing', NULL),
    ('Lou Edwards', 'lou.e@example.com', 'lou.jpg', NULL, NULL, NULL),
    
    ('Charlotte Kelly', 'charlotte.k@example.com', 'charlotte.jpg', 'College of Engineering', 'Chemical Engineering', 'Materials Science'),
    ('Benjamin Lee', 'benjamin.l@example.com', 'benjamin.jpg', 'Khoury College of Computer Science', 'Software Engineering', NULL),
    ('Emmalie Walker', 'emmalie.w@example.com', 'emmalie.jpg', 'D''Amore McKim School of Business', NULL, NULL),
    ('Mike Young', 'mike.y@example.com', 'mike.jpg', NULL, NULL, NULL),
   
    ('Nicole Bennett', 'nicole.b@example.com', 'nicole.jpg', 'Khoury College of Computer Science', 'Cybersecurity', NULL),
    ('Dev James', 'dev.j@example.com', 'dev.jpg', 'College of Science', 'Neuroscience', NULL),
    ('Niki Morris', 'niki.m@example.com', 'niki.jpg', 'College of Social Sciences and Humanities', NULL, NULL),
    ('Eve Brooks', 'eve.b@example.com', 'eve.jpg', NULL, NULL, NULL),

    ('Amy Bear', 'bear.a@example.com', 'nicole.jpg', 'Khoury College of Computer Science', 'Cybersecurity', NULL),
    ('Tony Lanez', 'lanez.t@example.com', 'tony.jpg', 'College of Science', 'Neuroscience', "Finance"),
    ('Marren Lowell', 'lowell.m@example.com', 'marren.jpg', 'College of Social Sciences and Humanities', "Journalist", "Political Science"),
    ('Masie Brie', 'masie.b@example.com', 'masie.jpg','College of Social Sciences and Humanities', "Political Science", NULL),

    ('Kate Sharma', 'sharma.k@example.com', 'kate.jpg', 'Khoury College of Computer Science', 'Cybersecurity', NULL),
    ('Mika Lee', 'lee.m@example.com', 'mika.jpg', 'College of Science', 'Biology', NULL),
    ('Brian Jacobs', 'jacobs.b@example.com', 'brian.jpg', 'College of Arts, Media, and Design', "Graphic Design", NULL),
    ('Steve Tuchel', 'tuchel.s@example.com', 'steve.jpg', "College of Science", "Chemical Engineering", NULL),

    ('Phoebe Bridgers', 'bridgers.p@example.com', 'phoebe.jpg', 'Khoury College of Computer Science', 'Cybersecurity', NULL),
    ('Lola Young', 'young.l@example.com', 'lola.jpg', 'College of Science', 'Neuroscience', NULL),
    ('Lucy Rox', 'rox.l@example.com', 'lucy.jpg', 'D''Amore McKim School of Business', "Business and Information Technology", NULL),
    ('Matt Del Rey', 'drey.matt@example.com', 'matt.jpg', "Bouve College of Health Sciences", "Public Health", "Business");

INSERT INTO Advisor (userid, department)
VALUES
    (3, 'Khoury College of Computer Science'),
    (7, 'Khoury College of Computer Science'),
    (11, 'College of Engineering'),
    (15, 'College of Science'),
    (19, 'D''Amore McKim School of Business'),
    (23, 'Khoury College of Computer Science'),
    (27, 'College of Arts, Media, and Design'),
    (31, 'Bouve College of Health Sciences'),
    (35, 'College of Science'),
    (39, 'College of Engineering'),
    (43, 'Khoury College of Computer Science'),
    (47, 'Bouve College of Health Sciences'),
    (51, 'D''Amore McKim School of Business'),
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
    (53, 'Eager to contribute to advancements in space technology and physics.', 'resume_default.pdf'),
    (57, 'Passionate about pioneering solutions in space technology and advancing the boundaries of modern physics to inspire the next frontier of exploration.', 'resume_default.pdf'),
    (58, 'Committed to contributing to groundbreaking advancements in space technology through collaboration, innovation, and scientific rigor.', 'resume_default.pdf'),
    (59, 'Eager to harness cutting-edge technologies and scientific research to revolutionize our understanding of the cosmos.', 'resume_default.pdf'),
    (60, 'Inspired by the wonders of space and physics, striving to contribute meaningful advancements to the fields that shape our understanding of the universe.', 'resume_default.pdf'),
    (61, 'Dedicated to merging theoretical insights with practical applications to drive innovations in space exploration and fundamental physics.', 'resume_default.pdf'),
    (62, 'Motivated to advance space technology through meticulous design, engineering, and a passion for solving challenges on a universal scale.', 'resume_default.pdf'),
    (63, 'Excited to explore uncharted territories in space and physics, contributing innovative solutions to some of humanity’s most ambitious goals.', 'resume_default.pdf'),
    (64, 'Focused on leveraging technical expertise and creative problem-solving to push the boundaries of space exploration and physics.', 'resume_default.pdf'),
    (65, 'Combining a deep fascination with the cosmos and an engineering mindset to advance technologies that bring humanity closer to the stars.', 'resume_default.pdf'),
    (66, 'Bridging disciplines to make transformative contributions to space technology and uncover the mysteries of physics.', 'resume_default.pdf'),
    (67, 'Driven to analyze and innovate, crafting technologies that redefine space exploration and deepen our grasp of physical laws.', 'resume_default.pdf'),
    (68, 'Excited to shape the future of space technology with strategic foresight and a profound appreciation for the complexities of physics.', 'resume_default.pdf');

INSERT INTO `Match` (mentorId, menteeId)
VALUES
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (12, 5),
    (2, 6),
    (3, 7),
    (13, 8),
    (3, 9),
    (14, 10),
    (4, 11),
    (4, 12),
    (5, 13),
    (5, 14),
    (5, 15),
    (6, 16),
    (6, 17),
    (6, 18),
    (7, 19),
    (7, 20),
    (8, 21),
    (8, 22),
    (9, 23),
    (9, 24),
    (10, 25),
    (11, 26);

INSERT INTO JobPosting (empId, companyId, role, jobDesc, majors, filledBool)
VALUES
    (1, 1, 'Intern', 'Frontend intern role at Google.', 'Computer Science, Software Engineering, Information Systems', FALSE),
    (2, 2, 'Co-op', 'DevOps Co-op role at Meta.', 'Computer Science, Information Technology, Software Engineering', FALSE),
    (3, 3, 'Software Engineer', 'Join Microsoft’s team to build scalable software solutions.', 'Computer Science, Software Engineering, Electrical Engineering', FALSE),
    (4, 4, 'Healthcare Analyst', 'Work with Labcorp to analyze healthcare data and improve diagnostics.', 'Health Informatics, Data Science, Public Health', FALSE),
    (5, 5, 'Brand Manager', 'Join Coca-Cola’s team to drive brand growth and market strategies.', 'Marketing, Business Administration, Communications', FALSE),
    (6, 6, 'Junior Designer', 'Help Adobe design creative assets for a variety of digital platforms.', 'Graphic Design, Interaction Design, Visual Arts', FALSE),
    (7, 7, 'Clinical Trial Assistant', 'Assist in clinical research at Mass General, supporting trial operations.', 'Biology, Biomedical Science, Public Health', FALSE),
    (8, 8, 'Machine Learning Engineer', 'Help NVIDIA develop AI-driven technologies for diverse industries.', 'Computer Science, Data Science, Artificial Intelligence', FALSE),
    (9, 9, 'AI Research Intern', 'Join OpenAI to contribute to innovative AI research and development.', 'Computer Science, Artificial Intelligence, Data Science', FALSE),
    (10, 10, 'Sales Engineer', 'Support Salesforce customers by providing tailored technical solutions.', 'Computer Science, Information Systems, Business Administration', FALSE),
    (11, 11, 'Clinical Research Intern', 'Contribute to research projects focused on health innovation at RWJ.', 'Biology, Public Health, Health Informatics', FALSE),
    (12, 12, 'Research Assistant', 'Assist Northeastern University’s faculty in cutting-edge research projects.', 'Computer Science, Mechanical Engineering, Social Sciences', FALSE),
    (13, 13, 'Sustainability Engineer', 'Work with Tesla to develop sustainable energy solutions.', 'Environmental Engineering, Mechanical Engineering, Energy Systems', FALSE),
    (14, 14, 'Software Developer', 'Join Amazon’s software development team to build scalable applications.', 'Computer Science, Software Engineering, Information Systems', FALSE),
    (1, 1, 'UX/UI Design Intern', 'Collaborate with Google’s design team to create seamless user experiences for web and mobile applications.', 'Interaction Design, Human-Computer Interaction, Computer Science', FALSE),
    (2, 2, 'Cloud Solutions Co-op', 'Work with Meta’s cloud infrastructure team to design and implement scalable cloud solutions.', 'Computer Science, Information Technology, Software Engineering', FALSE),
    (3, 3, 'Backend Software Engineer', 'Join Microsoft’s engineering team to develop robust and scalable backend services for enterprise applications.', 'Computer Science, Software Engineering, Data Science', FALSE),
    (4, 4, 'Medical Data Scientist', 'Analyze large healthcare datasets at Labcorp to improve diagnostic models and patient outcomes.', 'Health Informatics, Data Science, Statistics', FALSE),
    (5, 5, 'Digital Marketing Manager', 'Lead Coca-Cola’s digital marketing strategies to engage customers and enhance brand awareness through digital channels.', 'Marketing, Business Administration, Communications', FALSE),
    (6, 6, 'Visual Designer', 'Help Adobe design compelling visual experiences across digital platforms, focusing on branding and user interfaces.', 'Graphic Design, Interaction Design, Visual Arts', FALSE),
    (7, 7, 'Clinical Research Coordinator', 'Support Mass General’s clinical research projects, ensuring trials are conducted efficiently and in compliance with regulations.', 'Biology, Biomedical Science, Health Informatics', FALSE),
    (8, 8, 'AI Research Scientist', 'Join NVIDIA’s AI research team to create cutting-edge algorithms for machine learning and artificial intelligence solutions.', 'Computer Science, Data Science, Artificial Intelligence', FALSE),
    (9, 9, 'AI Ethics Intern', 'Contribute to OpenAI’s research on ethical AI development, ensuring responsible and fair use of AI technologies.', 'Computer Science, Philosophy, Ethics', FALSE),
    (10, 10, 'Customer Solutions Engineer', 'Work at Salesforce to provide technical support and create solutions for clients using Salesforce’s cloud platform.', 'Computer Science, Information Systems, Business Administration', FALSE),
    (11, 11, 'Healthcare Policy Intern', 'Assist in developing policy recommendations at RWJ, focusing on healthcare innovation and access improvement.', 'Public Health, Political Science, Health Informatics', FALSE),
    (12, 12, 'Innovation Research Assistant', 'Assist Northeastern University’s research teams in exploring cutting-edge innovations in technology and education.', 'Computer Science, Education, Innovation Studies', FALSE),
    (13, 13, 'Energy Systems Engineer', 'Collaborate with Tesla’s engineering team to develop and optimize energy storage and sustainable energy systems.', 'Mechanical Engineering, Environmental Engineering, Energy Systems', FALSE),
    (14, 14, 'Web Developer', 'Join Amazon’s engineering team to build and maintain web applications that improve the shopping experience for millions of users.', 'Computer Science, Software Engineering, Information Systems', FALSE);

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

INSERT INTO Events (speakerId, organizerId, speakerName, industry, `when`)
VALUES
    (1, 1, 'John Aquarius', 'Finance and Community Relations', '2024-12-01 10:00:00'),
    (1, 1, 'John Aquarius', 'Finance and Community Relations', '2024-12-02 10:00:00'),
    (1, 1, 'John Aquarius', 'Finance and Community Relations Day 3', '2024-12-03 11:00:00'),
    (2, 2, 'Priya Singh', 'Innovative Leadership Strategies', '2024-12-05 14:00:00'),
    (3, 3, 'Liam West', 'The Future of AI in Everyday Life', '2024-12-06 11:00:00'),
    (4, 4, 'Noah Green', 'Advances in Healthcare Consulting', '2024-12-07 09:30:00'),
    (2, 3, 'Priya Singh', 'Day 2: Finance Leadership Summit', '2024-12-19 11:00:00'),
    (3, 4, 'Liam West', 'The AI Revolution', '2024-12-20 14:00:00'),
    (4, 5, 'Noah Green', 'Healthcare Innovations 2024', '2024-12-21 12:00:00'),
    (5, 5, 'Ryan Davis', 'Modern Marketing Tactics', '2024-12-08 13:00:00'),
    (6, 6, 'Aiden White', 'Designing for Creativity', '2024-12-09 15:00:00'),
    (7, 7, 'Benjamin Walker', 'Breakthroughs in Clinical Research', '2024-12-10 10:30:00'),
    (5, 6, 'Ryan Davis','Creative Strategies for Marketers', '2024-12-22 13:00:00'),
    (6, 7, 'Aiden White','Design Thinking in Practice', '2024-12-23 15:00:00'),
    (7, 8, 'Benjamin Walker','Clinical Research Breakthroughs', '2024-12-24 10:30:00'),
    (8, 8, 'Jack Hernandez','Artificial Intelligence and Ethics', '2024-12-11 16:00:00'),
    (9, 9, 'Marcus Green','Product Management in the Digital Era', '2024-12-12 14:30:00'),
    (10, 10, 'Aria Mitchell', 'Effective Sales Techniques in 2024', '2024-12-13 12:00:00'),
    (8, 9, 'Jack Hernandez','Ethical AI: Challenges Ahead', '2024-12-25 16:00:00'),
    (9, 10, 'Marcus Green', 'Agile Product Management', '2024-12-26 14:30:00'),
    (10, 11, 'Aria Mitchell', 'Sales Strategies for 2025', '2024-12-27 12:00:00'),
    (11, 11, 'Cain Greek', 'Data Science for Decision Making', '2024-12-14 11:00:00'),
    (12, 12, 'Lou Edwards', 'Building University-Industry Partnerships', '2024-12-15 09:00:00'),
    (11, 12, 'Cain Greek', 'Data Science Impact on Business', '2024-12-28 11:00:00'),
    (12, 13, 'Lou Edwards', 'University-Industry Collaborations', '2024-12-29 09:00:00'),
    (13, 13, 'Mike Young', 'Renewable Energy Engineering', '2024-12-16 15:00:00'),
    (14, 14, 'Eve Brooks', 'Streamlining Logistics Operations', '2024-12-17 13:30:00'),
    (13, 14, 'Eve Brooks', 'Engineering Sustainability', '2024-12-30 15:00:00');