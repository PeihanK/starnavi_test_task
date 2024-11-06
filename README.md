1 Clone the repository:
git clone https://github.com/your-username/starnavi_test.git

2 Navigate into the project directory:
cd starnavi_test

3 Create and activate a virtual environment:
python -m venv .venv
Activate the virtual environment:
Win: .venv\Scripts\activate
Mac/Linux: source .venv/bin/activate

4 Install dependencies from requirements.txt:
pip install -r requirements.txt

5 Apply database migrations:
python manage.py migrate

6 Run the development server:
python manage.py runserver

The server will now be accessible at http://127.0.0.1:8000.
