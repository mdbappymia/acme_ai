from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

LEGAL_DOCS = [
    {
        "id": 1,
        "title": "Employment Agreement",
        "content": "Employees are entitled to annual leave of 14 working days. Employment may be terminated with 30 days written notice."
    },
    {
        "id": 2,
        "title": "Data Privacy Policy",
        "content": "Personal data must be processed lawfully and transparently. Users may request deletion of personal information."
    },
    {
        "id": 3,
        "title": "Commercial Lease Agreement",
        "content": "Tenants shall pay rent before the 5th day of each month. Landlords must provide notice before inspection."
    },
    {
        "id": 4,
        "title": "Non-Disclosure Agreement",
        "content": "Parties agree not to disclose confidential information obtained during business operations."
    },
    {
        "id": 5,
        "title": "Service Agreement",
        "content": "Service providers must deliver agreed services within specified timelines and quality standards."
    },
    {
        "id": 6,
        "title": "Partnership Agreement",
        "content": "Partners share profits, losses, and responsibilities according to agreed ownership percentages."
    },
    {
        "id": 7,
        "title": "Vendor Contract",
        "content": "Vendors shall provide goods according to specifications and delivery schedules."
    },
    {
        "id": 8,
        "title": "Consulting Agreement",
        "content": "Consultants will provide expert advice and maintain confidentiality of client information."
    },
    {
        "id": 9,
        "title": "Software License Agreement",
        "content": "Software licenses grant limited rights to use software subject to restrictions."
    },
    {
        "id": 10,
        "title": "Intellectual Property Agreement",
        "content": "All intellectual property created during employment belongs to the employer."
    },
    {
        "id": 11,
        "title": "Rental Agreement",
        "content": "Rent payments are due monthly. Property damage beyond normal wear is tenant responsibility."
    },
    {
        "id": 12,
        "title": "Loan Agreement",
        "content": "Borrowers must repay principal and interest according to the agreed repayment schedule."
    },
    {
        "id": 13,
        "title": "Franchise Agreement",
        "content": "Franchisees may use trademarks and systems in accordance with brand guidelines."
    },
    {
        "id": 14,
        "title": "Purchase Agreement",
        "content": "Ownership transfers upon full payment and completion of contractual obligations."
    },
    {
        "id": 15,
        "title": "Shareholder Agreement",
        "content": "Shareholders have voting rights proportional to their ownership interests."
    },
    {
        "id": 16,
        "title": "Insurance Policy",
        "content": "Coverage applies only to losses specified within the policy terms and conditions."
    },
    {
        "id": 17,
        "title": "Consumer Protection Policy",
        "content": "Customers have rights regarding refunds, warranties, and fair treatment."
    },
    {
        "id": 18,
        "title": "Workplace Safety Policy",
        "content": "Employees must comply with safety procedures and report workplace hazards."
    },
    {
        "id": 19,
        "title": "Remote Work Policy",
        "content": "Remote employees must maintain productivity and secure company information."
    },
    {
        "id": 20,
        "title": "Code of Conduct",
        "content": "Employees shall behave ethically and professionally in all business interactions."
    },
    {
        "id": 21,
        "title": "Cybersecurity Policy",
        "content": "Strong passwords and multi-factor authentication are required for system access."
    },
    {
        "id": 22,
        "title": "Terms and Conditions",
        "content": "Use of services constitutes acceptance of all terms and conditions."
    },
    {
        "id": 23,
        "title": "Privacy Notice",
        "content": "Users are informed about data collection, processing, and storage practices."
    },
    {
        "id": 24,
        "title": "Employee Handbook",
        "content": "Employees must follow workplace policies and organizational procedures."
    },
    {
        "id": 25,
        "title": "Conflict Resolution Policy",
        "content": "Disputes should be resolved through mediation before legal proceedings."
    },
    {
        "id": 26,
        "title": "Procurement Policy",
        "content": "Purchases must follow approved procurement and vendor selection procedures."
    },
    {
        "id": 27,
        "title": "Data Retention Policy",
        "content": "Records shall be retained for legally required periods before deletion."
    },
    {
        "id": 28,
        "title": "Whistleblower Policy",
        "content": "Employees may report misconduct without fear of retaliation."
    },
    {
        "id": 29,
        "title": "Environmental Policy",
        "content": "Organizations shall minimize environmental impact and comply with regulations."
    },
    {
        "id": 30,
        "title": "Health Benefits Policy",
        "content": "Eligible employees receive medical coverage according to benefit plans."
    },
    {
        "id": 31,
        "title": "Supplier Agreement",
        "content": "Suppliers shall provide products meeting agreed quality standards."
    },
    {
        "id": 32,
        "title": "Distribution Agreement",
        "content": "Distributors may market products within designated territories."
    },
    {
        "id": 33,
        "title": "Agency Agreement",
        "content": "Agents act on behalf of principals within authorized limits."
    },
    {
        "id": 34,
        "title": "Joint Venture Agreement",
        "content": "Parties collaborate on projects while sharing profits and risks."
    },
    {
        "id": 35,
        "title": "Investment Agreement",
        "content": "Investors provide capital in exchange for specified ownership rights."
    },
    {
        "id": 36,
        "title": "Mortgage Agreement",
        "content": "Property serves as collateral until the mortgage is fully repaid."
    },
    {
        "id": 37,
        "title": "Settlement Agreement",
        "content": "Parties agree to resolve disputes without further litigation."
    },
    {
        "id": 38,
        "title": "Construction Contract",
        "content": "Contractors must complete work according to approved plans and timelines."
    },
    {
        "id": 39,
        "title": "Maintenance Agreement",
        "content": "Service providers shall perform routine maintenance at agreed intervals."
    },
    {
        "id": 40,
        "title": "Employment Termination Policy",
        "content": "Termination procedures must comply with labor laws and company policies."
    },
    {
        "id": 41,
        "title": "Leave Management Policy",
        "content": "Employees may request annual, sick, and unpaid leave subject to approval."
    },
    {
        "id": 42,
        "title": "Attendance Policy",
        "content": "Employees are expected to maintain regular attendance and punctuality."
    },
    {
        "id": 43,
        "title": "Compensation Policy",
        "content": "Compensation is determined based on performance and market standards."
    },
    {
        "id": 44,
        "title": "Anti-Harassment Policy",
        "content": "Harassment of any kind is prohibited and subject to disciplinary action."
    },
    {
        "id": 45,
        "title": "Equal Opportunity Policy",
        "content": "Employment decisions are made without discrimination."
    },
    {
        "id": 46,
        "title": "Trade Secret Agreement",
        "content": "Trade secrets must remain confidential during and after employment."
    },
    {
        "id": 47,
        "title": "Customer Service Policy",
        "content": "Customer inquiries should be handled professionally and promptly."
    },
    {
        "id": 48,
        "title": "Return and Refund Policy",
        "content": "Customers may return eligible products within the specified period."
    },
    {
        "id": 49,
        "title": "Compliance Policy",
        "content": "All employees must comply with applicable laws and regulations."
    },
    {
        "id": 50,
        "title": "Corporate Governance Policy",
        "content": "Directors and officers shall act in the best interests of the organization."
    }
]


@app.get("/")
async def root():
    return {"message": "App is runnitg"}


class QueryRequest(BaseModel):
    query: str


@app.post("/generate")
async def generate(
    request: QueryRequest,
):
    query = request.query.lower()
    print()
    matches = []

    for doc in LEGAL_DOCS:
        if any(
            word in doc["content"].lower()
            or word in doc["title"].lower()
            for word in query.split()
        ):
            matches.append(doc)

    if not matches:
        return {
            "summary": "No matching legal document found.",
            "sources": []
        }

    summaries = []

    for doc in matches:
        summaries.append({
            "title": doc["title"],
            "summary": doc["content"].strip()[:150]
        })

    return {
        "summary": f"Found {len(matches)} relevant legal document(s).",
        "sources": summaries
    }
