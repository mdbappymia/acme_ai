# Legal document search portal

# Frontend (React)

## Installation

### Clone Repository

```
git clone https://github.com/mdbappymia/acme_ai.git
cd acme_ai
cd client
```

### Install Dependencies

```
npm install
```

### Running Locally

```
npm run dev
```

Application URL: http://localhost:5173

# Backend (FastAPI)

## Installation

### Navigate to the server folder

```
cd server
```

### Create Virtual Environment
Windows:
```
python -m venv venv
```
Linux:
```
sudo apt update
sudo apt install python3-venv
python3 -m venv venv
```

### Activate Virtual Environment

Windows:

```
venv\Scripts\activate
```

Linux:

```
source venv/bin/activate
```

### Install Dependencies

```python
pip install -r requirements.txt
```

### Running Locally

```
uvicorn main:app --reload
```

### Server will start at:

http://localhost:8000
