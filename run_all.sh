#!/usr/bin/env bash
set -euo pipefail

echo "======================================================================"
echo "RUNNING FULL FISCAL PER-CAPITA RESEARCH & AUDIT PIPELINE"
echo "======================================================================"

# Determine Python binary: prefer .venv if present
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "${SCRIPT_DIR}/.venv/bin/python" ]; then
    PYTHON="${SCRIPT_DIR}/.venv/bin/python"
    echo "✓ Using virtual environment Python: ${PYTHON}"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON="$(command -v python3)"
    echo "✓ Using system Python 3: ${PYTHON}"
else
    echo "✗ Error: No Python interpreter found!" >&2
    exit 1
fi

echo ""
echo "--- Step 1: Data Preparation & Accounting Reconciliations ---"
"${PYTHON}" "${SCRIPT_DIR}/src/data_preparation.py"

echo ""
echo "--- Step 2: Modeling & Vector/Raster/HTML Visualization Generation ---"
"${PYTHON}" "${SCRIPT_DIR}/src/modeling.py"

echo ""
echo "--- Step 3: Responsible Research Protocol Audit Suite ---"
"${PYTHON}" "${SCRIPT_DIR}/.agents/skills/responsible-research/scripts/audit_research_pipeline.py"

echo ""
echo "======================================================================"
echo "✓ FULL PIPELINE EXECUTION & AUDIT COMPLETED SUCCESSFULLY"
echo "======================================================================"

