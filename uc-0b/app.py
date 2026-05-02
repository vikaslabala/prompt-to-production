"""
UC-0B app.py — Policy Summarizer.
Implements retrieve_policy and summarize_policy skills.
"""
import argparse
import re
import os

def retrieve_policy(file_path):
    """
    Loads a .txt policy file and returns its content structured as numbered sections.
    Input: File path to the .txt policy file (string).
    Output: A dictionary with clause numbers as keys and clause content as values.
    Error handling: If file not found or invalid, raise ValueError.
    """
    if not os.path.exists(file_path):
        raise ValueError(f"File not found: {file_path}")
    if not file_path.endswith('.txt'):
        raise ValueError("Input must be a .txt file")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all clauses: lines starting with digit.digit space
    clauses = {}
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        if re.match(r'^\d+\.\d+', line):
            # Extract clause number and text
            match = re.match(r'^(\d+\.\d+)\s+(.+)', line)
            if match:
                clause_num = match.group(1)
                clause_text = match.group(2)
                clauses[clause_num] = clause_text
    if not clauses:
        raise ValueError("No clauses found in the file")
    return clauses

def summarize_policy(clauses):
    """
    Takes structured policy sections and produces a compliant summary with clause references.
    Input: Structured sections (dictionary from retrieve_policy).
    Output: Summary text (string) that includes all clauses and preserves obligations.
    Error handling: If clauses empty, raise ValueError.
    """
    if not clauses:
        raise ValueError("No clauses provided")
    
    summary_lines = []
    for clause_num, clause_text in clauses.items():
        summary_lines.append(f"Clause {clause_num}: {clause_text}")
    
    summary = "\n".join(summary_lines)
    return summary

def main():
    parser = argparse.ArgumentParser(description="Summarize policy document")
    parser.add_argument('--input', required=True, help='Input policy file path')
    parser.add_argument('--output', required=True, help='Output summary file path')
    args = parser.parse_args()
    
    try:
        clauses = retrieve_policy(args.input)
        summary = summarize_policy(clauses)
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(summary)
        print(f"Summary written to {args.output}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
