**Property Management Application with Built-in AI Agents**

A full-stack property management platform built with Python, Flask, HTML, CSS, SQLAlchemy, and integrated AI agents for request processing, rent reminder generation, and rental agreement drafting. The application supports owners, tenants, and admins through a role-based workflow and demonstrates modular backend design with AI-assisted business operations.

**Features**

1. Role-based authentication for Owner, Tenant, and Admin
2. Owner dashboard for adding and managing properties
3. Tenant dashboard for browsing and applying to properties
4. AI Request Processing Agent for tenant issue classification
5. AI Rent Collection Agent for generating rent reminder messages
6. AI Agreement Creation Agent for drafting rental agreements
7. Admin dashboard for platform overview
8. Modular Flask project structure


## Built-in AI Agents

### 1. Request Processing Agent
Processes tenant requests and returns:
- category
- priority
- short summary

### 2. Rent Collection Agent
Generates professional rent reminder messages for unpaid dues.

### 3. Agreement Creation Agent
Creates rental agreement drafts using owner, tenant, property, rent, and duration details.

The OpenAI API supports lightweight text generation workflows through the Responses API, making it suitable for embedding agent-like assistants inside application features. [web:81]

## Tech Stack

| Layer | Technology |
|------|------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, Jinja2 |
| Database | SQLite, SQLAlchemy |
| Authentication | Flask-Login |
| Forms | Flask-WTF |
| AI Integration | OpenAI API |
| Configuration | Python Dotenv |

## Project Structure

```text
PROPERTY-MANAGEMENT-APP/
│
├── app/
│   ├── __init__.py
│   ├── ai_agents.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static/
│   │   └── style.css
│   └── templates/
│       ├── base.html
│       ├── landing.html
│       ├── login.html
│       ├── register.html
│       ├── owner_dashboard.html
│       ├── tenant_dashboard.html
│       ├── admin_dashboard.html
│       ├── owner_properties.html
│       ├── tenant_properties.html
│       ├── ai_request_result.html
│       ├── ai_agreement_result.html
│       └── ai_rent_reminder_result.html
│
├── .env
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/property-management-app.git
cd property-management-app
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create `.env`:
```env
SECRET_KEY=your_super_secret_key_here
DATABASE_URL=sqlite:///property.db
OPENAI_API_KEY=your_openai_api_key_here
```

6. Run the application:
```bash
python run.py
```

7. Open:
```text
http://127.0.0.1:5000
```

## User Flow

### Owner
- Register/login as owner
- Add properties
- Use AI to generate agreements
- Use AI to generate rent reminders

### Tenant
- Register/login as tenant
- View available properties
- Apply for a property
- Use AI request processor

### Admin
- Login and monitor the system

## Security Notes

- API keys should be stored in `.env`, not hardcoded.
- Passwords are hashed before storage.
- Role checks are applied before owner and tenant actions.
- AI output should be reviewed before using it in legal or financial workflows.

GitHub recommends using the repository README to explain what the project does and how users can run it, while application secrets should stay outside the repository. [web:13][web:68]

## Production-Oriented Notes

This project uses Flask’s application factory style, which is the recommended pattern for organizing setup and extensions in larger Flask applications. [web:57][web:23]

For a stronger production deployment, future upgrades can include:
- PostgreSQL
- Alembic migrations
- File uploads for agreement documents
- Real-time chat
- Payment gateway integration
- Audit logs
- Role-specific admin controls

## Author

**K Dhanvardhan**  
Computer Science Student  
Hyderabad, Telangana, India
