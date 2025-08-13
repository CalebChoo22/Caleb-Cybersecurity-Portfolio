#!/usr/bin/env python3
# NIST 800-53 Gap Assessment Tool (tolerates extra spaces/case differences)

import csv, datetime, collections

HIGH = {"AC", "IA", "IR", "SI", "SC"}
MED = {"AU", "CM", "CP", "CA", "RA", "PM", "SR"}

def clean(s):
    """Trim spaces, quotes, and handle None."""
    return (s or "").strip().strip('"').strip("'")

def risk_tier(family):
    fam = clean(family).upper()
    if fam in HIGH:
        return "High"
    if fam in MED:
        return "Medium"
    return "Low"

def normalize_bool(val):
    return clean(val).lower() in {"y", "yes", "true", "1"}

def read_csv(filename):
    """Read CSV into list of dicts with normalized keys."""
    rows = []
    with open(filename, newline="") as f:
        reader = csv.DictReader(f)
        field_map = {k.strip().lower(): k for k in reader.fieldnames}
        for row in reader:
            norm_row = {k.strip().lower(): clean(v) for k, v in row.items()}
            rows.append(norm_row)
    return rows

def main():
    controls = read_csv("controls.csv")
    evidence = read_csv("evidence.csv")
    evidence_map = {row["control_id"].upper(): row for row in evidence if row.get("control_id")}

    gap_rows = []
    fam_total = collections.Counter()
    fam_gaps = collections.Counter()
    total = compliant = high_gaps = 0

    for c in controls:
        cid = c.get("control_id", "").upper()
        fam = c.get("family", "").upper()
        name = c.get("control_name", "")
        if not cid:
            continue

        ev = evidence_map.get(cid, {})
        impl = normalize_bool(ev.get("implemented", ""))
        has_link = bool(clean(ev.get("evidence_link", "")))
        ok = impl and has_link
        tier = risk_tier(fam)
        status = "Compliant" if ok else "Gap"

        gap_rows.append({
            "Control_ID": cid,
            "Family": fam,
            "Control_Name": name,
            "Implemented": "Yes" if impl else "No",
            "Evidence_Link": ev.get("evidence_link", ""),
            "Notes": ev.get("notes", ""),
            "Status": status,
            "Risk_Tier": tier
        })

        total += 1
        fam_total[fam] += 1
        if ok:
            compliant += 1
        else:
            fam_gaps[fam] += 1
            if tier == "High":
                high_gaps += 1

    # Write gap_report.csv
    with open("gap_report.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(gap_rows[0].keys()))
        writer.writeheader()
        writer.writerows(gap_rows)

    # Write summary.txt
    pct = (compliant / total * 100) if total else 0
    with open("summary.txt", "w") as f:
        f.write(f"Gap Assessment Summary\nDate: {datetime.date.today()}\n\n")
        f.write(f"Total controls evaluated: {total}\n")
        f.write(f"Compliant controls: {compliant} ({pct:.1f}%)\n")
        f.write(f"Gaps: {total - compliant}\n")
        f.write(f"High-risk gaps: {high_gaps}\n\n")
        f.write("Gaps by Family:\n")
        for fam in sorted(fam_total):
            f.write(f"  {fam}: {fam_gaps.get(fam,0)}/{fam_total[fam]} gaps\n")

if __name__ == "__main__":
    main()