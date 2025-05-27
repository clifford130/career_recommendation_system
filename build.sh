#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Make the patch script executable
echo "Making patch_frozendict.sh executable..."
chmod +x ./patch_frozendict.sh

# Run the patch script
echo "Applying frozendict patch..."
./patch_frozendict.sh

# Convert static asset files
echo "Collecting static files..."
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
echo "Applying database migrations..."
python manage.py migrate

echo "Build process complete."
