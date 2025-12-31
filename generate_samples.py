from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

def create_pdf(filename, title, content):
    path = os.path.join("samples", filename)
    os.makedirs("samples", exist_ok=True)
    
    c = canvas.Canvas(path, pagesize=LETTER)
    width, height = LETTER
    
    # Header
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width/2, height - 50, title)
    
    # Line
    c.setStrokeColor(colors.black)
    c.line(50, height - 60, width - 50, height - 60)
    
    # Content
    c.setFont("Helvetica", 11)
    text = c.beginText(50, height - 100)
    text.setLeading(14)
    
    for line in content.split('\n'):
        text.textLine(line)
    
    c.drawText(text)
    c.save()
    print(f"Created {path}")

# 1. Mutual NDA
nda_content = """This Mutual Non-Disclosure Agreement ("Agreement") is entered into as of January 1, 2026.

1. PURPOSE. The parties wish to explore a business opportunity of mutual interest.
2. CONFIDENTIAL INFORMATION. "Confidential Information" means any information disclosed by one party to the other.
3. OBLIGATIONS. The receiving party shall use the same degree of care it uses to protect its own secrets.
4. EXCLUSIONS. Confidential Information does not include information that is publicly known.
5. TERM. This agreement shall remain in effect for 5 years.
6. GOVERNING LAW. This agreement is governed by the laws of Mars.

[Note for AI: No termination clause for convenience.]
"""

# 2. Software Service Agreement (with risk)
sla_content = """SERVICE LEVEL AGREEMENT (SLA) v1.0

1. SERVICES. Provider will deliver cloud hosting services 24/7.
2. UPTIME. Provider guarantees 99.9% uptime per calendar month.
3. SERVICE CREDITS. If uptime is not met, a 5% credit is applied to the next bill.
4. LIMITATION OF LIABILITY. The Provider's liability is UNLIMITED in all circumstances. 
Even for minor data loss or accidental downtime, the Provider will pay full damages.
5. INDEMNIFICATION. Client shall indemnify Provider for any third-party claims.
6. TERMINATION. Provider can terminate this for any reason with 15 days notice.

[Note for AI: Unlimited liability is a huge risk for the provider.]
"""

# 3. Freelancer Agreement
freelancer_content = """FREELANCE SERVICES AGREEMENT

Effective Date: February 15, 2026
Consultant: John Doe
Company: LexAssistant Pro

1. SCOPE OF WORK. Consultant will provide AI development services.
2. PAYMENT. $150/hour, billed bi-weekly.
3. INTELLECTUAL PROPERTY. All work created belongs to John Doe personally. 
The Company is granted a 30-day license to use the results, after which it must pay a renewal fee.
4. NON-COMPETE. John Doe is allowed to work with the Company's direct competitors at any time.

[Note for AI: IP ownership and Non-compete terms are highly unfavorable for the Company.]
"""

create_pdf("Mutual_NDA.pdf", "Mutual Non-Disclosure Agreement", nda_content)
create_pdf("Service_Level_Agreement_Risk.pdf", "Service Level Agreement", sla_content)
create_pdf("Unfavorable_Freelancer_Contract.pdf", "Freelance Services Agreement", freelancer_content)
