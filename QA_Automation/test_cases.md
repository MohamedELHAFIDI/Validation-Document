# Test Cases

## Test Case 1: Upload a document with a valid format and size.
- **Steps**:
  1. Navigate to the document upload page.
  2. Select a valid PDF/DOCX file under 10 MB.
  3. Verify the document is accepted.
  
## Test Case 2: Upload a document with an invalid format.
- **Steps**:
  1. Navigate to the document upload page.
  2. Select a file with an invalid format (e.g., `.txt`).
  3. Verify an error message is displayed.

## Test Case 3: Upload a document exceeding maximum size.
- **Steps**:
  1. Navigate to the document upload page.
  2. Select a valid PDF/DOCX file over 10 MB.
  3. Verify an error message is displayed.
  
## Test Case 4: Enter valid and invalid metadata.
- **Steps**:
  1. Proceed to the metadata entry step.
  2. Enter valid data and verify it's accepted.
  3. Enter invalid data (e.g., missing title) and verify an error is shown.
  
## Test Case 5: Form submission with missing/invalid fields.
- **Steps**:
  1. Leave required fields empty or enter invalid data.
  2. Attempt submission.
  3. Verify the form cannot be submitted.
  
## Test Case 6: Simulate a network failure during submission.
- **Steps**:
  1. Begin form submission.
  2. Simulate network failure (e.g., disconnect network).
  3. Verify the system handles the failure gracefully.
