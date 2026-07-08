from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class ResumePDFGenerator:

    def __init__(self, filename="resume.pdf"):
        self.filename = filename
        self.doc = SimpleDocTemplate(self.filename, pagesize=A4)
        self.styles = getSampleStyleSheet()
        self.story = []

    def add_title(self, name):
        title_style = self.styles["Title"]
        self.story.append(Paragraph(name, title_style))
        self.story.append(Spacer(1, 12))

    def add_section(self, heading, content):
        heading_style = self.styles["Heading2"]
        normal_style = self.styles["BodyText"]

        self.story.append(Paragraph(f"<b>{heading}</b>", heading_style))
        self.story.append(Spacer(1, 6))

        # convert line breaks into readable format
        formatted_text = content.replace("\n", "<br/>")

        self.story.append(Paragraph(formatted_text, normal_style))
        self.story.append(Spacer(1, 12))

    def build_resume(self):
        self.doc.build(self.story)

    def generate(self, form_data):
        """
        form_data = request.form
        """

        self.add_title(form_data.get("name", "No Name"))

        self.add_section("Email", form_data.get("email", ""))
        self.add_section("Phone", form_data.get("phone", ""))
        self.add_section("Address", form_data.get("address", ""))
        self.add_section("Career Objective", form_data.get("career", ""))
        self.add_section("Education", form_data.get("education", ""))
        self.add_section("Skills", form_data.get("skills", ""))
        self.add_section("Projects", form_data.get("project", ""))
        self.add_section("Experience", form_data.get("experience", ""))
        self.add_section("Languages", form_data.get("languages", ""))
        self.add_section("Hobbies", form_data.get("hobbies", ""))

        self.build_resume()

        return self.filename