# <<<<<<< fix/render-deployment-errors
# #!/usr/bin/env bash
# # Exit on error
# set -o errexit

# # Install dependencies
# pip install -r requirements.txt

# # Make the patch script executable
# echo "Making patch_frozendict.sh executable..."
# chmod +x ./patch_frozendict.sh

# # Run the patch script
# echo "Applying frozendict patch..."
# ./patch_frozendict.sh

# # Convert static asset files
# echo "Collecting static files..."
# python manage.py collectstatic --no-input

# # Apply any outstanding database migrations
# echo "Applying database migrations..."
# python manage.py migrate

# echo "Build process complete."
# =======
# # #!/usr/bin/env bash
# # # Exit on error
# # set -o errexit

# # # Modify this line as needed for your package manager (pip, poetry, etc.)
# # pip install -r requirements.txt

# # # Convert static asset files
# # python manage.py collectstatic --no-input

# # # Apply any outstanding database migrations
# # python manage.py migrate
# #!/usr/bin/env bash
# # Exit on error
# set -o errexit

# # Install dependencies
# pip install -r requirements.txt

# # Make the patch script executable
# echo "Making patch_frozendict.sh executable..."
# chmod +x ./patch_frozendict.sh

# # Run the patch script
# echo "Applying frozendict patch..."
# ./patch_frozendict.sh

# # Convert static asset files
# echo "Collecting static files..."
# python manage.py collectstatic --no-input

# # Apply any outstanding database migrations
# echo "Applying database migrations..."
# python manage.py migrate

# echo "Build process complete."
# >>>>>>> main
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
