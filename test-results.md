# Testing summary

All tests were performed separately.
The original code and sample data were restored after testing.

| Test | Change | Expected result | Screenshot |
----------------------------------------------------------
| Original run | No changes; reference date 2026-10-27 | 5 total, 4 flagged, 1 passed | 01-original-output.png |
| Changed reference date | Reference date changed to 2026-10-19 | R1 passes; 3 flagged, 2 passed | 02-changed-reference-date.png |
| Missing owner | Owner field removed from R1 | R1 reports missing owner and overdue | 03-missing-owner.png |
| Invalid date | R1 due date changed to 2026-02-30 | Invalid date reported; program continues | 04-invalid-date.png |
| Empty dataset | Records replaced with an empty list | Zero records and no-records message | 05-empty-dataset.png |

## Other Checks Demonstrated by the Original Data

> Duplicate ID: Both records with ID R2 are flagged.
> Null owner: The first R2 record has owner set to None.
> Missing due date: The second R2 record has no due date value.
> Closed with pending action: R3 is flagged.
> Closed without pending action: R4 passes.
> Status capitalization: R4 uses CLOSED and is handled correctly.

## Final Submitted Version

main.py contains the original five sample records
and the reference date 2026-10-27.