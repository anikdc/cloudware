## Cloudware
Use your own hardware as cloud storage! This is a work in progress.

## Quick Start

1. Clone the repository
```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
```

2. Create and activate virtual environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your settings
# Windows: notepad .env
# Linux/Mac: nano .env
```

5. Run the application
```bash
python main.py
```

The application will be available at `http://localhost:5000`

## Environment Variables

Required environment variables:
- `SECRET_KEY`: Your Flask secret key
- `UPLOAD_FOLDER`: Full path to upload directory

## Current Progress
 - [ ] Create an upload progress bar
 - [ ] Figure out how static and templates work better
 - [ ] Learn about POST and GET
 - [ ] Improve download efficiency (Fetch)
 - [x] Make the app a little bit more secure
 - [x] Maintain Folder Structure
 - [x] Multiple file storage
 - [x] Download to local storage
 - [x] Connect Flask to index.html
 - [x] Create index.html and main.py
 - [x] Create venv and import modules 
