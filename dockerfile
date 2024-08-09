# Base Image: Use an official Python image with a suitable version
FROM python:3.9-slim-buster

# Set Working Directory: Create and set the working directory inside the container
WORKDIR /app

# Copy Requirements: Copy the requirements file to the working directory
COPY requirements.txt .

# Install Dependencies: Install project dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy Project Files: Copy the entire project to the working directory
COPY . .

# Expose Port: Expose the port your Django app will run on (typically 8000)
EXPOSE 8000

# Collect Static Files: Collect static files for production use
RUN python manage.py collectstatic --noinput

# Set Environment Variables: Set any necessary environment variables (e.g., Django settings)
ENV DJANGO_SETTINGS_MODULE=my_cv_site.my_cv_site.settings

# Run Server: Start the Django development server (replace 0.0.0.0 with your host if needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
