# PPL_Project_CV_Builder

Group 10 - Saturday Morning

# CV/Resume Builder - DSL to Resume

This project allows you to upload a CV/Resume described in a custom JSON-based DSL format and renders it as a beautiful resume in your browser.

## How It Works

- **Frontend:** `index.html` lets you upload your DSL file and displays the parsed resume.
- **Backend:** Python (Flask Framework) parses the uploaded file and returns the structured data as JSON.
- **Parsing:** The backend uses ANTLR (with the provided `CV.g4` grammar) to parse the DSL. The grammar expects a JSON-like structure (see below).

## DSL Input Format

Your input file should be a valid JSON file with the following structure:

```json
{
  "cv": {
    "personal_info": {
      "name": "Your Name",
      "email": "your@email.com",
      "phone": "+1 234 567 890",
      "address": "Your Address",
      "linkedin": "linkedin.com/in/yourprofile",
      "website": "yourwebsite.com"
    },
    "summary": "A short professional summary...",
    "education": [
      {
        "degree": "Degree Name",
        "institution": "Institution Name",
        "start": "Start Year",
        "end": "End Year",
        "details": "Details or honors (optional)"
      }
    ],
    "experience": [
      {
        "title": "Job Title",
        "company": "Company Name",
        "start": "Start Date",
        "end": "End Date or Present",
        "location": "Location",
        "responsibilities": [
          "Responsibility 1",
          "Responsibility 2"
        ]
      }
    ],
    "skills": ["Skill1", "Skill2", "Skill3"],
    "certifications": [
      { "name": "Certification Name", "year": "Year" }
    ],
    "languages": [
      { "language": "English", "level": "native" },
      { "language": "Spanish", "level": "intermediate" }
    ]
  }
}
```

## Example DSL File

```json

```

See `dsl_cv.json` for a sample input.

## How to Use

1. **Start the backend server** (Flask/FastAPI) to handle `/parse` POST requests.
   - Run "python run.py gen" 
   - Then "run python app.py"
2. **Open `index.html`** in your browser.
   - The server is running on port "http://127.0.0.1:5000/".
3. **Upload your DSL file** (JSON format) and view your resume.

## Notes

- The ANTLR grammar (`CV.g4`) expects the root rule to be `cv: obj EOF;` and the main object to be named `cv`.
- The DSL is JSON, so you can use any text editor to create your file.
- The resume sections and fields are mapped to the UI as shown in `index.html`.

## Troubleshooting

- If parsing fails, ensure your JSON is valid and matches the structure above.

- If you modify the grammar, regenerate the parser with:

```sh
java -jar antlr-4.x-complete.jar -Dlanguage=Python3 -o CompiledFiles -visitor CV.g4
```

- For Python backend, ensure you use the generated files from `CompiledFiles/`.

---

**Contact:** For questions, please contact the team leader.
