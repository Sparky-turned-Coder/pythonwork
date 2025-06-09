from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, '90-Day Self-Study Plan: Python for Industrial Automation (for Electricians)', ln=True, align='C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, ln=True, fill=True)
        self.ln(2)

    def chapter_body(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, text)
        self.ln()

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Introduction
pdf.chapter_title('Introduction')
pdf.chapter_body(
    "This 90-day plan is tailored for electricians who want to break into automation and Python programming, "
    "without the need for formal education. It assumes 3-5 hours per week and is structured around real-world "
    "skills you can build in your spare time."
)

# Month 1
pdf.chapter_title('Month 1: Python Fundamentals')
pdf.chapter_body(
    "Week 1: Learn basic Python syntax, variables, and data types.\n"
    "Week 2: Control flow (if/else), logical operators, and simple conditions.\n"
    "Week 3: Functions and file I/O (read/write sensor data).\n"
    "Week 4: Lists, dictionaries, and simulate device states.\n\n"
    "Goal: Simulate basic control behavior (e.g., start/stop logic)."
)

# Month 2
pdf.chapter_title('Month 2: Control Systems and I/O')
pdf.chapter_body(
    "Week 5: Learn control systems and PLC logic via simulators like PLC Fiddle.\n"
    "Week 6: GPIO with Raspberry Pi or simulation. Read button input, control an LED.\n"
    "Week 7: Use timers and simulate interlocks in Python.\n"
    "Week 8: Build a 3-wire motor control simulation project.\n\n"
    "Goal: Python script simulating real-world control logic."
)

# Month 3
pdf.chapter_title('Month 3: Modbus and Final Project')
pdf.chapter_body(
    "Week 9: Learn Modbus protocol basics.\n"
    "Week 10: Use pymodbus to poll from a simulator or dummy data.\n"
    "Week 11: Visualize data with matplotlib or Streamlit.\n"
    "Week 12: Complete and document a final project.\n\n"
    "Goal: Complete a Mini-SCADA or Smart Panel project."
)

# Tools
pdf.chapter_title('Tools and Resources')
pdf.chapter_body(
    "- Python: https://www.python.org\n"
    "- PLC Simulator: https://plcfiddle.com\n"
    "- Modbus Simulator: ModbusPal\n"
    "- Raspberry Pi Docs: https://www.raspberrypi.com/documentation\n"
    "- Python Libraries: pymodbus, matplotlib, streamlit, gpiozero"
)

# Output the PDF
pdf.output("90-Day_Python_Automation_Study_Plan.pdf")
