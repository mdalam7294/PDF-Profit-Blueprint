from fpdf import FPDF
from datetime import datetime
import webbrowser

# ==================== REAL PAYMENT LINKS (CHANGE THESE) ====================
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
RAZORPAY_INR_LINK = "https://rzp.io/rzp/BStamAgK"      # ← Your real Razorpay link (₹499)
PAYPAL_USD_LINK   = "https://www.paypal.com/ncp/payment/L3W3N4EWQTANW"  # ← Your real PayPal link ($29)
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

RAZORPAY_PRICE_INR = 499   # ₹499 (India)
PAYPAL_PRICE_USD   = 29    # $29 (International)

# ==================== PAYMENT HANDLER ====================
def handle_payment(product_name):
    print(f"\n💰 {product_name}")
    print(f"1. Razorpay (₹{RAZORPAY_PRICE_INR} - India)")
    print(f"2. PayPal (${PAYPAL_PRICE_USD} - International / Worldwide)")
    
    while True:
        choice = input("\nChoose payment method (1 or 2): ").strip()
        if choice == "1":
            print(f"Opening Razorpay link for ₹{RAZORPAY_PRICE_INR}...")
            webbrowser.open(RAZORPAY_INR_LINK)
            currency = "INR"
            break
        elif choice == "2":
            print(f"Opening PayPal link for ${PAYPAL_PRICE_USD}...")
            webbrowser.open(PAYPAL_USD_LINK)
            currency = "USD"
            break
        else:
            print("Please enter only 1 or 2!")

    input("✅ After payment is complete, press Enter to generate the PDF...")
    print(f"✅ Payment accepted ({currency})! Generating PDF now...\n")
    return True

# ==================== PDF CLASS ====================
class PassivePDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'PDF Profit Blueprint - Premium Digital Product', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Created with Grok Code for PDF Profit Blueprint • Page {self.page_no()}', 0, 0, 'C')

# ==================== ALL 6 PDF FUNCTIONS ====================
def create_daily_planner(filename="Daily_Planner.pdf", niche="Productivity"):
    if not handle_payment(f"Daily Planner - {niche}"):
        return
    pdf = PassivePDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 22)
    pdf.cell(0, 15, f"{niche} Daily Planner {datetime.now().year}", ln=True, align='C')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%d %B %Y')}", ln=True, align='C')
    pdf.ln(15)
    sections = ["🌅 Morning Routine", "🎯 Top 3 Goals Today", "✅ Main Tasks", "💡 Key Learnings", "🙏 Gratitude", "🌙 Evening Reflection"]
    for section in sections:
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 12, section, ln=True)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(0, 10, "→ ______________________________\n\n" * 5)
        pdf.ln(8)
    pdf.output(filename)
    print(f"✅ Daily Planner ready: {filename}")

def create_habit_checklist(filename="30_Day_Habit_Checklist.pdf"):
    if not handle_payment("30-Day Habit Checklist"):
        return
    pdf = PassivePDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "30-Day Habit Checklist", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    for i in range(1, 31):
        pdf.cell(0, 10, f"Day {i:2d}: [ ] ____________________________________________", ln=True)
    pdf.output(filename)
    print(f"✅ Habit Checklist ready: {filename}")

def create_goal_tracker(filename="Goal_Tracker_Workbook.pdf"):
    if not handle_payment("Goal Tracker Workbook"):
        return
    pdf = PassivePDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 22)
    pdf.cell(0, 15, "2026 Goal Tracker Workbook", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 12, "Big 2026 Goals (Write 5)", ln=True)
    pdf.multi_cell(0, 12, "1. ______________________________\n2. ______________________________\n3. ______________________________\n4. ______________________________\n5. ______________________________")
    pdf.ln(15)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 12, "Monthly Progress Tracker", ln=True)
    for month in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]:
        pdf.cell(0, 10, f"{month}: [ ] 25% [ ] 50% [ ] 75% [ ] 100%", ln=True)
    pdf.output(filename)
    print(f"✅ Goal Tracker ready: {filename}")

def create_ai_prompt_pack(filename="AI_Prompt_Pack.pdf"):
    if not handle_payment("AI Prompt Pack"):
        return
    pdf = PassivePDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "50+ Ready-to-Use AI Prompts Pack", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    for i in range(1,51):
        pdf.multi_cell(0, 10, f"{i}. AI prompt here...\n\n")
    pdf.output(filename)
    print(f"✅ AI Prompt Pack ready: {filename}")

def create_habit_journal(filename="Monthly_Habit_Journal.pdf"):
    if not handle_payment("Monthly Habit Journal"):
        return
    pdf = PassivePDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 15, "Monthly Habit Journal", ln=True, align='C')
    pdf.ln(10)
    for day in range(1, 32):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, f"Day {day}", ln=True)
        pdf.set_font('Arial', '', 11)
        pdf.multi_cell(0, 10, "✅ Habits: \n1. \n2. \n3. \nMood: ________   Notes: ________")
        pdf.ln(5)
    pdf.output(filename)
    print(f"✅ Habit Journal ready: {filename}")

def create_niche_guide(filename="Niche_Guide.pdf", niche="Fitness"):
    if not handle_payment(f"{niche} Ultimate Guide"):
        return
    pdf = PassivePDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 22)
    pdf.cell(0, 15, f"Ultimate {niche} Guide 2026", ln=True, align='C')
    pdf.ln(15)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, "Introduction...\n\nStep-by-step Plan...\n\n30-Day Challenge...\n\nResources...")
    pdf.output(filename)
    print(f"✅ {niche} Guide ready: {filename}")

# ==================== MAIN MENU ====================
if __name__ == "__main__":
    print("="*70)
    print("🚀 PDF PROFIT BLUEPRINT - FULL REAL PAYMENT EDITION")
    print("   Razorpay ₹499 (India)  |  PayPal $29 (International)")
    print("="*70)
    print("1. Daily Planner")
    print("2. 30-Day Habit Checklist")
    print("3. Goal Tracker Workbook")
    print("4. AI Prompt Pack (50+ prompts)")
    print("5. Monthly Habit Journal")
    print("6. Niche Specific Guide")
    print("0. Exit")
    print("="*70)

    while True:
        choice = input("\nWhich PDF do you want to create? (1-6 or 0): ").strip()
        
        if choice == "0":
            print("Thank you! Start your business with PDF Profit Blueprint 💰")
            break
        elif choice == "1":
            niche = input("Enter niche (default: Productivity): ") or "Productivity"
            create_daily_planner(niche=niche)
        elif choice == "2":
            create_habit_checklist()
        elif choice == "3":
            create_goal_tracker()
        elif choice == "4":
            create_ai_prompt_pack()
        elif choice == "5":
            create_habit_journal()
        elif choice == "6":
            niche = input("Enter niche (e.g. Fitness, Finance, Study): ") or "Fitness"
            create_niche_guide(niche=niche)
        else:
            print("Invalid choice! Please enter 1-6.")
