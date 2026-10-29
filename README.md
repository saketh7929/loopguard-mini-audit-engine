# LoopGuard Mini Audit Engine

Project ID: PRJ-13

## Project Scope

This beginner Python project checks operational request records
and identifies issues that require human follow-up.

## Features

> Detects the overdue requests that are not closed.
> Detects the missing, null, or blank owners.
> Detects the duplicate Request IDs.
> Detects the closed requests with pending actions.
> Handles the missing and invalid due dates.
> Handles the status capitalization differences.
> Handles an empty dataset.
> Displays recommended actions and a summary.

## Python Concepts Used

 >Lists
 >Dictionaries
 >Sets
 >For loops
 >Conditional statements
 >Exception handling
 >datetime module

## Files

- main.py: Final working program.
- TESTING.md: Test cases and results.
- screenshots: Original output and test screenshots.

## How to Run

1. Install Python.
2. Open the project folder in VS Code.
3. Open a terminal and run:

```bash
python main.py
```

The reference date is set inside the code.
The program does not ask for user input.

## Original Sample Results

Reference date: 2026-10-27

. Total records: 5
. Flagged records: 4
. Passed records: 1

Both records sharing the ID R2 are flagged.
One record may have the multiple issues.

## Testing

See TESTING.md for the test changes and expected results.
The screenshots folder contains proof from the test runs.

## Limitations

The sample records are stored directly in the program.
The code expects an ID, a string status, and a Boolean pending
action value in each record.

The program recommends actions but does not modify the records.