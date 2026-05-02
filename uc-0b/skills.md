# skills.md

skills:
  - name: retrieve_policy
    description: Loads a .txt policy file and returns its content structured as numbered sections.
    input: File path to the .txt policy file (string).
    output: A dictionary with section numbers as keys and section content as values.
    error_handling: If the file is not found, return an error message. If the file is not a .txt file or cannot be parsed into sections, return an error indicating invalid input.

  - name: summarize_policy
    description: Takes structured policy sections and produces a compliant summary with clause references.
    input: Structured sections (dictionary from retrieve_policy).
    output: Summary text (string) that includes all clauses and preserves obligations.
    error_handling: If the input sections are empty or invalid, return an error message indicating the issue.
