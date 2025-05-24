#!/bin/bash
# patch_frozendict.sh

# Find the site-packages directory.
# This assumes a standard Python environment where site.getsitepackages() returns the correct path.
SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])")

# Define the target file path
FROZENDICT_INIT_PY="$SITE_PACKAGES/frozendict/__init__.py"

echo "Attempting to patch $FROZENDICT_INIT_PY"

# Check if the target file exists
if [ ! -f "$FROZENDICT_INIT_PY" ]; then
  echo "ERROR: $FROZENDICT_INIT_PY not found!"
  # Try another common path for virtual environments
  SITE_PACKAGES_VENV=$(python -c "import sys; print(next(p for p in sys.path if 'site-packages' in p))")
  FROZENDICT_INIT_PY="$SITE_PACKAGES_VENV/frozendict/__init__.py"
  echo "Retrying with $FROZENDICT_INIT_PY"
  if [ ! -f "$FROZENDICT_INIT_PY" ]; then
    echo "ERROR: $FROZENDICT_INIT_PY still not found! Patching failed."
    exit 1
  fi
fi

# 1. Ensure 'import collections.abc' is present
# Check if the import already exists
grep -q "^import collections.abc" "$FROZENDICT_INIT_PY"
if [ $? -ne 0 ]; then
  # Add the import statement at the beginning of the file.
  # Using a temporary file for portability with sed -i (macOS vs Linux)
  sed '1iimport collections.abc
' "$FROZENDICT_INIT_PY" > "$FROZENDICT_INIT_PY.tmp" && mv "$FROZENDICT_INIT_PY.tmp" "$FROZENDICT_INIT_PY"
  echo "Added 'import collections.abc' to $FROZENDICT_INIT_PY"
else
  echo "'import collections.abc' already present in $FROZENDICT_INIT_PY."
fi

# 2. Replace 'collections.Mapping' with 'collections.abc.Mapping'
# Check if the specific line to be replaced exists
grep -q "class frozendict(collections.Mapping):" "$FROZENDICT_INIT_PY"
if [ $? -eq 0 ]; then
  # Using a temporary file for portability with sed -i
  sed 's/class frozendict(collections.Mapping):/class frozendict(collections.abc.Mapping):/g' "$FROZENDICT_INIT_PY" > "$FROZENDICT_INIT_PY.tmp" && mv "$FROZENDICT_INIT_PY.tmp" "$FROZENDICT_INIT_PY"
  echo "Replaced 'collections.Mapping' with 'collections.abc.Mapping' in $FROZENDICT_INIT_PY."
else
  # Check if it was already patched
  grep -q "class frozendict(collections.abc.Mapping):" "$FROZENDICT_INIT_PY"
  if [ $? -eq 0 ]; then
    echo "'collections.Mapping' already replaced with 'collections.abc.Mapping' in $FROZENDICT_INIT_PY."
  else
    echo "WARNING: Pattern 'class frozendict(collections.Mapping):' not found in $FROZENDICT_INIT_PY. File might be different than expected."
  fi
fi

echo "Patching of $FROZENDICT_INIT_PY complete."
exit 0
