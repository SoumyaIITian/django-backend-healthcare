# Healthcare Backend API

A secure RESTful backend system for managing healthcare records, built with Django, Django REST Framework (DRF), and PostgreSQL. 

## Tech Stack
- **Framework:** Django & Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JSON Web Tokens (SimpleJWT)
- **Environment:** python-dotenv

## Local Setup

1. **Clone the repository and set up the virtual environment:**
   `python3 -m venv venv`
   `source venv/bin/activate`

2. **Install dependencies:**
   `pip install -r requirements.txt`

3. **Configure Environment Variables:**
   Create a `.env` file in the root directory:
   `SECRET_KEY=your_django_secret_key`
   `DEBUG=True`
   `DB_NAME=healthcare_db`
   `DB_USER=postgres`
   `DB_PASSWORD=your_postgres_password`
   `DB_HOST=localhost`
   `DB_PORT=5432`

4. **Run Database Migrations:**
   `python manage.py makemigrations`
   `python manage.py migrate`

5. **Start the Development Server:**
   `python manage.py runserver`

## API Endpoints

**Authentication**
- `POST /api/auth/register/` - Register a new user
- `POST /api/auth/login/` - Login and receive JWT access/refresh tokens

**Patients** *(Requires JWT Auth)*
- `GET /api/patients/` - List all patients created by the authenticated user
- `POST /api/patients/` - Add a new patient
- `GET /api/patients/<id>/` - Get specific patient details
- `PUT /api/patients/<id>/` - Update a patient
- `DELETE /api/patients/<id>/` - Delete a patient

**Doctors** - `GET /api/doctors/` - List all doctors (Public)
- `POST /api/doctors/` - Add a new doctor *(Requires JWT Auth)*
- `GET /api/doctors/<id>/` - Get specific doctor details
- `PUT /api/doctors/<id>/` - Update a doctor
- `DELETE /api/doctors/<id>/` - Delete a doctor

**Patient-Doctor Mappings** *(Requires JWT Auth)*
- `GET /api/mappings/` - List all patient-doctor assignments
- `POST /api/mappings/` - Assign a doctor to a patient
- `GET /api/mappings/<patient_id>/` - List all doctors assigned to a specific patient
- `DELETE /api/mappings/<id>/` - Remove a specific doctor assignment

## Security Notes
- All patient records are strictly isolated to the user who created them.
- JWT tokens must be included in the `Authorization` header as `Bearer <token>` for protected endpoints.
