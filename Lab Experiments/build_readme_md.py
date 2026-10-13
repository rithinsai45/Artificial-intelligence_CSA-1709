import os
import subprocess
from experiments_data import experiments

def generate_markdown(output_paths):
    base_dir = r"c:\Users\Vishal_balaji_J\Downloads\git hub\Artificial-Intelligence\Lab Experiments"

    md_content = """# CSA17 — ARTIFICIAL INTELLIGENCE LAB OBSERVATION MANUAL
### SAVEETHA INSTITUTE OF MEDICAL AND TECHNICAL SCIENCES (SIMATS ENGINEERING)
**Department of Computer Science and Engineering**

- **Student Name:** Vishal Balaji J
- **Register Number:** 192525014
- **Course Code & Title:** CSA17 — Artificial Intelligence
- **Degree & Branch:** B.Tech Computer Science and Engineering

---

## INDEX / EXPERIMENT SCHEDULE

| Exp. No. | Submission Date | Experiment Title | Course Outcome | Status |
|:---:|:---:|:---|:---:|:---:|
| **1** | 13.10.2026 | 8-Puzzle Problem using A* Search | CO1 | Completed |
| **2** | 13.10.2026 | 8-Queen Problem using Backtracking | CO1 | Completed |
| **3** | 13.10.2026 | Water Jug Problem using State Space Search | CO2 | Completed |
| **4** | 13.10.2026 | Missionaries and Cannibals Problem | CO3 | Completed |
| **5** | 13.10.2026 | Vacuum Cleaner Agent (Vacuum World) | CO3 | Completed |
| **6** | 15.10.2026 | Breadth First Search (BFS) Implementation | CO3 | Completed |
| **7** | 15.10.2026 | Depth First Search (DFS) Implementation | CO4 | Completed |
| **8** | 15.10.2026 | A* Search Algorithm on Weighted Graph | CO4 | Completed |
| **9** | 15.10.2026 | Crypt-Arithmetic Problem (SEND + MORE = MONEY) | CO2 | Completed |
| **10** | 15.10.2026 | Travelling Salesman Problem (TSP) | CO4 | Completed |

---
"""

    for exp in experiments:
        py_path = os.path.join(base_dir, exp["file"])
        with open(py_path, 'r', encoding='utf-8') as f:
            code_text = f.read()

        res = subprocess.run(["python", py_path], capture_output=True, text=True, cwd=base_dir)
        idle_out = res.stdout.strip()

        proc_lines = "\n".join([f"- {p}" for p in exp["procedure"]])
        algo_lines = "\n".join([f"{a}" for a in exp["algorithm"]])

        md_content += f"""
## EXPERIMENT {exp['num']}: {exp['title']}

- **Date:** {exp['date']}
- **Course Outcome:** {exp['co']}
- **Submission Target:** {'Assigned for 13.10.2026' if '13.10' in exp['date'] else 'Assigned for 15.10.2026'}

### AIM
{exp['aim']}

### PROCEDURE
{proc_lines}

### ALGORITHM
```text
{algo_lines}
```

### SOURCE CODE
```python
{code_text}
```

### PYTHON COMPILER IDLE OUTPUT
```text
=================== RESTART: Shell Execution ===================
{idle_out}
```

### RESULT
{exp['result']}

---
"""

    for path in output_paths:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Generated Markdown at: {path}")

if __name__ == '__main__':
    targets = [
        r"c:\Users\Vishal_balaji_J\Downloads\git hub\Artificial-Intelligence\Lab Experiments\README.md",
        r"c:\Users\Vishal_balaji_J\Downloads\git hub\Artificial-intelligence_CSA-1709\Lab Experiments\README.md",
        r"c:\Users\Vishal_balaji_J\Downloads\CSA17_Artificial_Intelligence_Lab_Observation_Manual.md"
    ]
    generate_markdown(targets)
