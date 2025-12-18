import py_compile
import sys
from pathlib import Path

errors = []
python_files = list(Path("app").rglob("*.py"))

for file in python_files:
    try:
        py_compile.compile(str(file), doraise=True)
        print(f"✓ {file}")
    except py_compile.PyCompileError as e:
        errors.append(f"✗ {file}: {e}")
        print(f"✗ {file}: {e}")

if errors:
    print(f"\n{len(errors)} error(s) found!")
    sys.exit(1)
else:
    print(f"\n✓ All {len(python_files)} files are syntactically valid!")
