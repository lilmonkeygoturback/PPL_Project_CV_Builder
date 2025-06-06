# 4.1.6. Testing and Validation

## Objectives of Testing:
- Verify that all core functionalities work as intended.
- Ensure system security measures are robust.

## Testing Process:

### Test Case 1: Upload a valid DSL CV file and generate a resume preview
**Description:** Ensures resume preview renders correctly from a valid DSL file.

| Step | Action                  | Expected System Response | Pass/Fail |
|------|------------------------|-------------------------|-----------|
| 1    | Open web interface     | Page loads              | Pass      |
| 2    | Upload valid DSL file  | File accepted           | Pass      |
| 3    | Backend parses file    | JSON returned           | Pass      |
| 4    | Render preview         | Matches input           | Pass      |

---

### Test Case 2: Invalid DSL File Handling
**Description:** Ensures system rejects malformed DSL and informs user.

| Step | Action             | Expected System Response | Pass/Fail |
|------|-------------------|-------------------------|-----------|
| 1    | Upload invalid file| Error detected          | Pass      |
| 2    | Display error msg  | User informed           | Pass      |
| 3    | Wrong format rendered | System stable        | Pass      |

---

### Test Case 3: PDF/PNG Export Functionality
**Description:** Tests for accurate export of styled resume.

| Step | Action                                 | Expected System Response         | Pass/Fail |
|------|----------------------------------------|----------------------------------|-----------|
| 1    | Click "Download PDF" or "Download PNG" | Export process starts            | Pass      |
| 2    | Save file                              | Exported file matches preview    | Pass      |

---

### Test Case 4: Valid but formally incorrect DSL file handling (dsl_cv_1.json)

#### Case 4.1: Grammatically correct DSL JSON, but string type variable changed to object (e.g., field name)

| Step | Action         | Expected System Response | Pass/Fail |
|------|---------------|-------------------------|-----------|
| 1    | Upload DSL file| File accepted           | Pass      |
| 2    | Backend parses | JSON returned           | Pass      |
| 3    | Render preview | Matches input           | Fail. The output was "[object Object]" |

#### Case 4.2: Grammatically correct DSL JSON, but string type variable changed to array (e.g., field email)

| Step | Action         | Expected System Response | Pass/Fail |
|------|---------------|-------------------------|-----------|
| 1    | Upload DSL file| File accepted           | Pass      |
| 2    | Backend parses | JSON returned           | Pass      |
| 3    | Render preview | Matches input           | Pass. All elements were printed, but missing indentation after comma. |