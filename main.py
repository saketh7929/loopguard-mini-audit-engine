from datetime import datetime

reference_date = datetime.strptime("2026-10-27", "%Y-%m-%d").date()
records = [
    {"id": "R1", "status": "Open", "owner": "Saketh", "due": "2026-10-20", "pending": True},
    {"id": "R2", "status": "Open", "owner": None, "due": "2026-11-05", "pending": True},
    {"id": "R3", "status": "Closed", "owner": "Priya", "due": "2026-10-15", "pending": True},
    {"id": "R2", "status": "Open", "owner": "Rahul", "due": None, "pending": False},
    {"id": "R4", "status": "CLOSED", "owner": "Meena", "due": "2026-10-10", "pending": False}
]
seen = set()
duplicates = set()
for record in records:
    if record["id"] in seen:
        duplicates.add(record["id"])
    seen.add(record["id"])

flagged = 0
print("LOOPGUARD MINI AUDIT ENGINE")
print("Reference date:", reference_date)
for record in records:
    issues = []
    status = record["status"].strip().lower()
    if not str(record.get("owner") or "").strip():
        issues.append("Missing owner: Assign an owner.")
    if record["id"] in duplicates:
        issues.append("Duplicate ID: Review matching records.")
    if status == "closed" and record["pending"] is True:
        issues.append("Closed with pending action: Verify completion and update.")
    if not str(record.get("due") or "").strip():
        issues.append("Missing due date: Add the correct date.")
    else:
        try:
            due = datetime.strptime(record["due"].strip(), "%Y-%m-%d").date()
            if status != "closed" and due < reference_date:
                issues.append("Overdue: Follow up with the owner.")
        except ValueError:
            issues.append("Invalid date: Use a valid YYYY-MM-DD date.")
    print("\nRequest:", record["id"])
    if issues:
        flagged += 1
        for issue in issues:
            print("-", issue)
    else:
        print("PASS: No issues found.")
print("\nSUMMARY | Total:", len(records), "| Flagged:", flagged)
print("Passed:", len(records) - flagged)
if not records:
    print("No records to audit. Add records and run again.")
print("Follow-up: Review listed actions." if flagged else "No follow-up required.")