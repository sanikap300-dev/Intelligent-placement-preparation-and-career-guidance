
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from sqlalchemy import Column, Integer, Text

from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

from flask_cors import CORS
CORS(app)

app.secret_key = "placement_secret_key"

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///placement1.db"


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile = db.Column(db.String(15))
    college = db.Column(db.String(100))
    branch = db.Column(db.String(100))
    password = db.Column(db.String(255), nullable=False)



with app.app_context():
    db.create_all()


# ---------------- HOME ---------------- #

@app.route("/")
def home():
    return render_template("home.html")

# ---------------- REGISTER ---------------- #

@app.route("/api/register", methods=["POST"])
def api_register():

    data = request.json

    fullname = data.get("fullname")
    email = data.get("email")
    mobile = data.get("mobile")
    college = data.get("college")
    branch = data.get("branch")
    password = data.get("password")


    # check existing user
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message":"Email already exists"
        }),400


    new_user = User(
        fullname=fullname,
        email=email,
        mobile=mobile,
        college=college,
        branch=branch,
        password=generate_password_hash(password)
    )


    db.session.add(new_user)
    db.session.commit()


    return jsonify({
        "message":"Registration successful"
    }),200

# ---------------- LOGIN ---------------- #
@app.route("/api/login", methods=["POST"])
def api_login():

    data = request.json

    email = data.get("email")
    password = data.get("password")


    user = User.query.filter_by(email=email).first()


    if user and check_password_hash(user.password, password):

        return jsonify({
            "message":"Login successful",
            "user":{
                "id":user.id,
                "fullname":user.fullname,
                "email":user.email,
                "branch":user.branch
            }
        }),200


    return jsonify({
        "message":"Invalid email or password"
    }),401

# ---------------- DASHBOARD ---------------- #

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("dashboard.html", username=session["user"])

# ---------------- LOGOUT ---------------- #

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))

# ---------------- OTHER PAGES ---------------- #

@app.route("/api/aptitude", methods=["GET"])
def aptitude():

    
      return jsonify()


@app.route("/technical")
def technical():
 return jsonify()


@app.route("/interview")
def interview():

     questions = [
         

{
    "question": "Can you walk me through your resume?",
    "answer": "My resume highlights my education, technical skills, academic projects, and certifications. I have worked on projects that improved my programming and problem-solving abilities. I am continuously learning new technologies to strengthen my knowledge. Overall, my experiences have prepared me for a software development role."
},

{
    "question": "What inspired you to choose software development as a career?",
    "answer": "I enjoy solving real-world problems using technology. Developing applications that make people's lives easier motivates me. I also like learning new programming languages and frameworks. Software development provides continuous learning and exciting career opportunities."
},

{
    "question": "How would your friends describe you?",
    "answer": "My friends describe me as responsible, supportive, and hardworking. They appreciate my willingness to help others and my positive attitude. They also consider me a quick learner who adapts well to new situations. I always try to motivate people around me."
},

{
    "question": "What are your biggest professional values?",
    "answer": "I believe in honesty, teamwork, discipline, and continuous learning. These values help me build strong professional relationships. I always try to complete my work with dedication and integrity. I believe these qualities contribute to long-term success."
},

{
    "question": "How do you prepare before starting a new project?",
    "answer": "I first understand the project requirements carefully. Then I break the work into smaller tasks and create a plan. I research any technologies I am unfamiliar with before starting development. Proper planning helps me complete projects efficiently."
},

{
    "question": "Tell me about a time you solved a difficult problem.",
    "answer": "During one of my projects, I encountered a bug that prevented the application from working correctly. I analyzed the issue, searched documentation, and tested multiple solutions. After identifying the root cause, I fixed the problem successfully. The experience improved my debugging skills."
},

{
    "question": "How do you stay organized while working?",
    "answer": "I create a list of tasks and prioritize them according to deadlines. I divide large tasks into smaller achievable goals. I regularly review my progress to ensure I stay on schedule. This approach helps me maintain productivity."
},

{
    "question": "Describe your ideal work environment.",
    "answer": "I enjoy working in an environment that encourages learning, teamwork, and innovation. Open communication and mutual respect are important to me. I also appreciate opportunities to learn from experienced colleagues. Such an environment helps me perform my best."
},

{
    "question": "How do you react when you make a mistake?",
    "answer": "I accept my mistake and analyze what caused it. Then I take corrective action and ensure the same mistake is not repeated. I believe mistakes are valuable learning opportunities. They help me improve both personally and professionally."
},

{
    "question": "What programming language are you most comfortable with?",
    "answer": "I am most comfortable with Python because of its simple syntax and powerful libraries. I use it for problem-solving, automation, and web development. I also have knowledge of SQL, HTML, CSS, and JavaScript. I am always willing to learn additional languages when required."
},

{
    "question": "What is debugging?",
    "answer": "Debugging is the process of finding and fixing errors in a program. Developers use debugging tools, log messages, and testing to identify issues. Effective debugging improves software quality and reliability. It is an essential skill for every programmer."
},

{
    "question": "What is the SDLC?",
    "answer": "SDLC stands for Software Development Life Cycle. It includes planning, analysis, design, development, testing, deployment, and maintenance. Following SDLC helps ensure high-quality software is delivered on time. It also improves project management and communication."
},

{
    "question": "What is the difference between frontend and backend development?",
    "answer": "Frontend development focuses on the user interface and user experience of an application. Backend development handles business logic, databases, and server-side processing. Both work together to build complete web applications. Effective communication between frontend and backend is essential."
},

{
    "question": "What is a database?",
    "answer": "A database is an organized collection of data that allows efficient storage and retrieval. Databases are managed using Database Management Systems like MySQL or SQLite. They ensure data consistency, security, and easy access. Most modern applications depend on databases."
},

{
    "question": "Why is teamwork important in software development?",
    "answer": "Software projects usually involve multiple developers working together. Teamwork improves productivity, knowledge sharing, and problem-solving. Good communication helps avoid misunderstandings and delays. Successful software development depends on effective collaboration."
},

{
    "question": "How do you ensure the quality of your code?",
    "answer": "I write clean, readable, and well-structured code. I test my programs thoroughly before submitting them. I also review my code to identify possible improvements or errors. Following coding standards helps improve code quality."
},

{
    "question": "What would you do if your project deadline is very close?",
    "answer": "I would prioritize the most important tasks and focus on completing them first. If necessary, I would communicate with my team and manager about the progress. I would avoid compromising the quality of the project. Proper planning helps meet deadlines effectively."
},

{
    "question": "How do you handle multiple tasks at the same time?",
    "answer": "I prioritize tasks based on urgency and importance. I create a schedule and focus on completing one task efficiently before moving to the next. I also monitor my progress regularly. This helps me stay productive without feeling overwhelmed."
},

{
    "question": "What do you know about Agile methodology?",
    "answer": "Agile is a software development methodology that delivers software in small iterations. It encourages teamwork, customer feedback, and continuous improvement. Agile helps teams respond quickly to changing requirements. Scrum is one of the most popular Agile frameworks."
},

{
    "question": "What is version control?",
    "answer": "Version control is a system that tracks changes made to source code over time. It allows developers to collaborate without losing previous versions of the code. Git is one of the most widely used version control systems. It also supports branching and merging."
},

{
    "question": "What are your technical skills?",
    "answer": "My technical skills include Python, SQL, HTML, CSS, JavaScript, and Angular. I also have experience with Flask, Git, and database management. I enjoy learning new technologies through projects and online courses. I continuously improve my technical knowledge."
},

{
    "question": "Describe a project you are proud of.",
    "answer": "One of my favorite projects involved building a complete web application using modern technologies. I worked on both the frontend and backend while managing the database. The project improved my technical and teamwork skills. Completing it successfully gave me confidence in software development."
},

{
    "question": "What makes a good software engineer?",
    "answer": "A good software engineer has strong technical knowledge and problem-solving skills. They communicate effectively and work well in teams. They continuously learn new technologies and follow coding best practices. They also write clean, maintainable, and efficient code."
},

{
    "question": "How do you approach learning a new programming language?",
    "answer": "I start by understanding the basic syntax and core concepts. Then I practice by solving coding problems and building small projects. I also read documentation and watch tutorials. Practical experience helps me learn quickly."
},

{
    "question": "What is your biggest motivation for success?",
    "answer": "My biggest motivation is continuous improvement and achieving meaningful goals. I enjoy solving problems and seeing the results of my efforts. Learning new technologies also motivates me to grow professionally. Success encourages me to take on bigger challenges."
},

{
    "question": "How do you define success?",
    "answer": "I define success as achieving goals while continuously learning and improving. Success is not only about personal achievements but also about contributing to a team's success. Maintaining a positive attitude and strong work ethic is equally important. Every challenge is an opportunity to grow."
},

{
    "question": "What kind of projects do you enjoy working on?",
    "answer": "I enjoy projects that involve problem-solving and real-world applications. Building web applications and learning new technologies excites me. I also enjoy projects that require teamwork and creativity. Such projects help me improve both technical and communication skills."
},

{
    "question": "Why should we choose you over other candidates?",
    "answer": "I am a dedicated learner with strong technical fundamentals and a positive attitude. I work well in teams and adapt quickly to new challenges. I am committed to improving my skills and delivering quality work. I believe my enthusiasm and willingness to learn make me a valuable candidate."
},

{
    "question": "How do you contribute to a team's success?",
    "answer": "I communicate openly with team members and share ideas whenever possible. I complete my assigned work responsibly and support others when needed. I believe collaboration leads to better results. My goal is always to help the team achieve its objectives."
},

{
    "question": "Is there anything else you would like us to know about you?",
    "answer": "I am passionate about technology and always eager to learn new skills. I enjoy taking on challenges that help me grow professionally. I believe my dedication, adaptability, and positive attitude will allow me to contribute effectively to your organization. I am excited about the opportunity to begin my career with your company."
},
       {
    "question": "What is Python?",
    "answer": "Python is a high-level, interpreted, and object-oriented programming language. It is easy to learn because of its simple syntax. Python is widely used for web development, data science, automation, artificial intelligence, and scripting. It also has a large collection of built-in libraries that make development faster."
},

{
    "question": "What are the features of Python?",
    "answer": "Python is simple, readable, and easy to learn. It supports object-oriented, functional, and procedural programming. It has a large standard library and works on multiple operating systems. Python is also open-source and has a strong developer community."
},

{
    "question": "What is the difference between List and Tuple?",
    "answer": "A List is mutable, which means its elements can be changed after creation. A Tuple is immutable, so its values cannot be modified. Lists are generally used when data needs to change, while Tuples are used for fixed data. Tuples are also slightly faster than Lists."
},

{
    "question": "What is Object-Oriented Programming (OOP)?",
    "answer": "Object-Oriented Programming is a programming paradigm based on objects and classes. It helps organize code into reusable components. The four main principles are Encapsulation, Inheritance, Polymorphism, and Abstraction. OOP makes applications easier to maintain and extend."
},

{
    "question": "Explain Encapsulation.",
    "answer": "Encapsulation is the process of combining data and methods into a single unit called a class. It also restricts direct access to data by making variables private. This improves data security and prevents accidental modification. Getter and setter methods are commonly used for controlled access."
},

{
    "question": "What is Inheritance?",
    "answer": "Inheritance allows one class to acquire the properties and methods of another class. The existing class is called the parent class, and the new class is called the child class. It promotes code reusability and reduces duplication. Python supports single, multiple, multilevel, and hierarchical inheritance."
},

{
    "question": "What is Polymorphism?",
    "answer": "Polymorphism means one interface can have multiple implementations. The same method can behave differently depending on the object that calls it. Python supports polymorphism through method overriding and operator overloading. It improves flexibility and code readability."
},

{
    "question": "What is Abstraction?",
    "answer": "Abstraction means hiding implementation details while showing only essential features. It simplifies complex systems by exposing only what is necessary. In Python, abstraction is achieved using abstract classes and methods. It improves maintainability and security."
},

{
    "question": "What is SQL?",
    "answer": "SQL stands for Structured Query Language. It is used to create, retrieve, update, and delete data stored in relational databases. SQL also allows users to define database structures and manage permissions. It is supported by databases like MySQL, PostgreSQL, and SQLite."
},

{
    "question": "What is DBMS?",
    "answer": "A Database Management System is software used to create and manage databases. It provides efficient storage, retrieval, and security of data. Examples include MySQL, Oracle, SQL Server, and SQLite. A DBMS also supports backup, recovery, and data consistency."
},

{
    "question": "What is the difference between DELETE, TRUNCATE, and DROP?",
    "answer": "DELETE removes selected rows from a table and can be rolled back. TRUNCATE removes all rows quickly but keeps the table structure intact. DROP completely removes the table along with its structure and data. These commands are used for different database management tasks."
},

{
    "question": "What are Primary Key and Foreign Key?",
    "answer": "A Primary Key uniquely identifies each record in a table and cannot contain duplicate or NULL values. A Foreign Key is used to establish a relationship between two tables. It references the Primary Key of another table. Together, they help maintain data integrity."
},

{
    "question": "What is a JOIN in SQL?",
    "answer": "A JOIN combines rows from two or more tables based on a related column. Common types include INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN. JOIN operations help retrieve meaningful information from multiple tables. They are widely used in database applications."
},

{
    "question": "What is HTML?",
    "answer": "HTML stands for HyperText Markup Language. It is used to create the structure of web pages using elements like headings, paragraphs, images, and forms. HTML works together with CSS and JavaScript to build modern websites. It is the foundation of web development."
},

{
    "question": "What is CSS?",
    "answer": "CSS stands for Cascading Style Sheets. It is used to style HTML elements by adding colors, layouts, fonts, and animations. CSS helps create responsive and attractive web pages. It separates the design from the content of a website."
},

{
    "question": "What is JavaScript?",
    "answer": "JavaScript is a scripting language used to make web pages interactive. It can handle events, validate forms, update page content, and communicate with servers. JavaScript works alongside HTML and CSS to create dynamic web applications. It is supported by all modern browsers."
},

{
    "question": "What is Angular?",
    "answer": "Angular is a TypeScript-based front-end framework developed by Google. It is used to build single-page applications with reusable components. Angular provides features like routing, dependency injection, and two-way data binding. It helps developers create scalable and maintainable applications."
},

{
    "question": "What is Flask?",
    "answer": "Flask is a lightweight web framework for Python. It is used to build web applications and REST APIs with minimal setup. Flask is flexible, easy to learn, and supports extensions for additional functionality. It is suitable for both small and medium-sized projects."
},

{
    "question": "What is API?",
    "answer": "An API, or Application Programming Interface, allows different software applications to communicate with each other. It defines a set of rules for sending requests and receiving responses. REST APIs commonly use HTTP methods such as GET, POST, PUT, and DELETE. APIs are widely used in modern web and mobile applications."
},

{
    "question": "What is Git?",
    "answer": "Git is a distributed version control system used to track changes in source code. It allows multiple developers to work on the same project efficiently. Git provides features such as branching, merging, and version history. Platforms like GitHub use Git for project collaboration."
},

{
    "question": "What is the difference between Compiler and Interpreter?",
    "answer": "A compiler translates the entire source code into machine code before execution, while an interpreter translates and executes code line by line. Compiled programs usually run faster than interpreted programs. Python uses an interpreter, whereas C and C++ use compilers. Both have their own advantages depending on the application."
},



{
    "question": "What is Object-Oriented Programming (OOP)?",
    "answer": "Object-Oriented Programming is a programming paradigm based on objects and classes. It helps organize code into reusable components. The four main principles are Encapsulation, Inheritance, Polymorphism, and Abstraction. OOP improves code reusability, scalability, and maintainability."
},

{
    "question": "What is the difference between C and C++?",
    "answer": "C is a procedural programming language, while C++ supports both procedural and object-oriented programming. C++ provides features like classes, objects, inheritance, and polymorphism. C is mainly used for system programming, whereas C++ is widely used for application and game development."
},

{
    "question": "Why is Python so popular?",
    "answer": "Python is popular because of its simple and readable syntax. It has a large collection of libraries for web development, data science, machine learning, and automation. Python is platform-independent and has a huge developer community. It is an excellent language for beginners as well as professionals."
},

{
    "question": "What are Python lists and tuples?",
    "answer": "Lists and tuples are data structures used to store collections of items. A list is mutable, meaning its elements can be modified after creation. A tuple is immutable, so its values cannot be changed. Tuples are generally faster and more memory-efficient than lists."
},

{
    "question": "What is the difference between == and = in Python?",
    "answer": "The '=' operator is used to assign a value to a variable. The '==' operator is used to compare two values for equality. It returns either True or False depending on whether the values are equal. These operators serve completely different purposes."
},

{
    "question": "What are functions in programming?",
    "answer": "A function is a block of reusable code that performs a specific task. Functions help reduce code duplication and improve readability. They can accept input through parameters and return results. Using functions makes programs easier to maintain and debug."
},

{
    "question": "What is recursion?",
    "answer": "Recursion is a technique where a function calls itself to solve a problem. It is useful for problems that can be divided into smaller subproblems. Every recursive function should have a base case to stop execution. Without a base case, recursion can lead to infinite function calls."
},

{
    "question": "What is an array?",
    "answer": "An array is a collection of elements stored in contiguous memory locations. It allows quick access to elements using an index. Arrays are efficient for storing multiple values of the same data type. They are widely used in algorithms and data structures."
},

{
    "question": "What is a linked list?",
    "answer": "A linked list is a linear data structure where each node contains data and a reference to the next node. Unlike arrays, linked lists do not require contiguous memory. They allow efficient insertion and deletion of elements. However, accessing elements takes more time because traversal is required."
},

{
    "question": "What is a stack?",
    "answer": "A stack is a linear data structure that follows the Last In, First Out (LIFO) principle. Elements are added using the push operation and removed using the pop operation. Stacks are commonly used for function calls, expression evaluation, and undo operations. They are simple but very useful in programming."
},


        # Add more questions here...
    ]
     return render_template("interview.html", questions=questions)



@app.route("/performance")
def performance():
    return render_template("performance.html")


def get_value(field):
    value = request.form.get(field)
    other = request.form.get(field + "_other")

    if value == "other" and other:
        return other
    return value


# Resume class
class Resume:
    def __init__(self, name, email, phone, address,
                 career, education, skills,
                 project, experience, languages, hobbies):

        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.career = career
        self.education = education
        self.skills = skills
        self.project = project
        self.experience = experience
        self.languages = languages
        self.hobbies = hobbies


@app.route("/resume", methods=["GET", "POST"])
def resume():
    if request.method == "POST":
        student = Resume(
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            request.form["address"],
            request.form["career"],
            request.form["education"],
            request.form["skills"],
            request.form["project"],
            request.form["experience"],
            request.form["languages"],
            request.form["hobbies"]
        )
        from Moduler.resume_generator import ResumePDFGenerator

        pdf_path = "static/resume.pdf"
        re = ResumePDFGenerator(pdf_path)
        re.generate(request.form)

        re = ResumePDFGenerator('resume.pdf')
        re.generate(request.form)

        return render_template("resume.html", student=student, pdf_url="static/resume.pdf")

    return render_template("resume.html", student=None)


@app.route("/companies")
def companies():
    return render_template("companies.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        # You can print or save the data
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)

        return render_template("contact.html", message_sent=True)

    return render_template("contact.html", message_sent=False)


  # ✅ GLOBAL CAREER DATA (IMPORTANT: outside function)
career_data = {

    "Python": """
Python is one of the most popular and beginner-friendly programming languages in the world. It is widely used in web development, data science, artificial intelligence, machine learning, automation, and scripting. Python is known for its simple syntax and readability, which makes it ideal for beginners.

A Python developer builds applications, APIs, backend systems, and automation tools. Python is also heavily used in research, finance, and cloud computing. Major companies like Google, Amazon, Microsoft, Netflix, and Meta use Python in their systems.

To become a Python developer, you should first learn basic programming concepts like variables, loops, functions, and object-oriented programming. After mastering basics, you should move to advanced topics like file handling, exception handling, and modules.

Frameworks like Flask and Django are important for backend web development. Flask is lightweight and simple, while Django is powerful and used for large applications. You should also learn REST APIs and how web servers work.

Database knowledge is essential, especially SQL databases like MySQL or PostgreSQL. Python also works well with data libraries like Pandas and NumPy, which are used in data science.

For career growth, you should build real-world projects such as a resume builder, blog application, or e-commerce backend. You should also learn Git and GitHub for version control and collaboration.

Python developers can grow into roles like backend engineer, AI engineer, data analyst, or machine learning engineer. Learning cloud platforms like AWS or Azure further increases job opportunities.
""",

    "Java": """
Java is a powerful object-oriented programming language used in enterprise-level applications and Android development. It is known for its stability, security, and portability across platforms.

Java is widely used in banking systems, large-scale enterprise applications, and backend systems. Companies like Oracle, IBM, Infosys, TCS, and Wipro rely heavily on Java developers.

To start with Java, you must learn core concepts like variables, loops, arrays, functions, and object-oriented programming principles such as inheritance, polymorphism, and encapsulation.

After mastering core Java, you should learn collections framework, multithreading, exception handling, and file handling. These concepts are important for real-world applications and interviews.

Spring Boot is one of the most important frameworks in Java for backend development. It helps in building scalable and production-ready web applications. Hibernate is used for database operations.

You should also learn SQL databases and REST API development. Understanding microservices architecture is important for advanced backend roles.

Projects like banking systems, e-commerce platforms, and student management systems are very useful for practice.

Java developers can work as backend engineers, Android developers, or full-stack developers with strong backend skills.
""",

    "C++": """
C++ is a high-performance programming language used in system programming, game development, and competitive programming. It provides low-level memory control and high execution speed.

C++ is widely used in gaming engines, operating systems, embedded systems, and performance-critical applications. Companies like Microsoft, Adobe, Google, and Amazon use C++ in system-level development.

To learn C++, you should start with basic syntax, loops, functions, and object-oriented programming concepts. After that, you should focus heavily on Data Structures and Algorithms (DSA).

DSA is extremely important for C++ developers, especially for cracking coding interviews. You should practice arrays, linked lists, stacks, queues, trees, graphs, and dynamic programming.

The Standard Template Library (STL) is a powerful feature of C++ that includes prebuilt data structures and algorithms. Learning STL improves coding efficiency.

C++ also requires understanding memory management, pointers, and system-level concepts like operating systems basics.

Competitive programming platforms like Codeforces, LeetCode, and CodeChef are very useful for improving problem-solving skills.

Career roles include software engineer, game developer, and system programmer.
""",

    "Web Development": """
Web development is the process of building websites and web applications that run on the internet. It is one of the most in-demand skills in the tech industry.

Web development is divided into frontend, backend, and full-stack development. Frontend deals with user interface, backend handles server logic, and full-stack includes both.

Frontend technologies include HTML, CSS, and JavaScript. Modern frameworks like React, Angular, and Vue.js are widely used to build interactive web applications.

Backend development includes technologies like Node.js, Python Flask, and Django. These handle databases, authentication, and business logic.

Databases like MySQL and MongoDB are used to store application data. REST APIs are used to connect frontend and backend systems.

To become a web developer, you should start by building static websites and gradually move to dynamic full-stack projects.

Important projects include portfolio websites, e-commerce platforms, job portals, and social media applications.

Web developers are in high demand in startups, IT companies, and product-based companies.
""",

    "Data Science": """
Data Science is the field of analyzing and interpreting large amounts of data to extract useful insights. It combines programming, statistics, and machine learning.

Data scientists help companies make data-driven decisions. This field is used in business analytics, healthcare, finance, marketing, and artificial intelligence.

Python is the most commonly used language in data science due to its powerful libraries like Pandas, NumPy, Matplotlib, and Scikit-learn.

You must also learn statistics, probability, and linear algebra to understand data patterns and machine learning models.

Machine learning is an important part of data science, where models are trained to predict outcomes based on data.

Common projects include sales prediction, fraud detection, recommendation systems, and data visualization dashboards.

Tools like Power BI and Tableau are used for creating interactive reports.

Data science offers high-paying roles in companies like Google, Amazon, IBM, and Deloitte.
""",

    "Cyber Security": """
Cyber security focuses on protecting computer systems, networks, and data from cyber attacks and unauthorized access.

Cyber security professionals work to prevent hacking, data breaches, and malware attacks in organizations.

Key areas include network security, ethical hacking, cryptography, and risk management.

You should learn networking fundamentals, Linux operating system, and security tools like Wireshark and Nmap.

Ethical hackers test systems to find vulnerabilities before attackers can exploit them.

Certifications like CEH (Certified Ethical Hacker) and CompTIA Security+ are highly valuable.

Cyber security is important in banking, government, IT companies, and defense organizations.

Projects include network scanning tools, password strength checkers, and security auditing systems.
""",

    "Cloud Computing": """
Cloud computing provides computing services like storage, servers, databases, and networking over the internet.

It eliminates the need for physical infrastructure and allows scalable and flexible computing resources.

Major cloud platforms include Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform.

Cloud engineers manage servers, deploy applications, and ensure system scalability and security.

DevOps is closely related to cloud computing and includes automation tools like Docker and Kubernetes.

You should learn Linux, networking, CI/CD pipelines, and cloud architecture.

Cloud computing is used in almost every modern IT company due to its flexibility and cost efficiency.

Projects include deploying web applications, building cloud storage systems, and setting up CI/CD pipelines.

Cloud professionals are highly paid and in demand globally.
"""
}
    
    # ✅ ROUTE
@app.route("/career", methods=["GET", "POST"])
def career():

    recommendation = ""

    if request.method == "POST":
        skill = request.form.get("skill")   # safe method
        recommendation = career_data.get(skill, "No recommendation available.")

    return render_template("career.html", recommendation=recommendation)

    

    return render_template("career.html", recommendation=recommendation)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
 