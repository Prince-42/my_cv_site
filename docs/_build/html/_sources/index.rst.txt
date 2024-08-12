.. Prince CV documentation master file, created by
   sphinx-quickstart on Fri Aug  9 19:11:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

My_cv_site documentation
========================

This repository contains the code for my Capstone Project, a personal CV website built using Django.

Table of Contents
-----------------

1. `Features`_
2. `Technologies Used`_
3. `Getting Started`_
   - `Prerequisites`_
   - `Installation and Setup`_
4. `Usage`_
5. `Credits`_

Features
--------

* Displays my professional experience, skills, and education.
* Responsive design for optimal viewing on different devices.
* Easy to update and maintain.

Technologies Used
-----------------

* **Django**: Web framework used to build the site.
* **Python 3.x**: Programming language for the backend.
* **HTML/CSS**: Markup and styling for the frontend.
* **Docker** : For containerization and easier deployment.

Getting Started
---------------

.. _Prerequisites:

### Prerequisites

* Python 3.x
* pip
* Docker (optional)

.. _Installation and Setup:

### Installation and Setup

1. Clone the repository:

   .. code-block:: bash

      git clone <repository_url>
      cd <project_directory>

2. Create a virtual environment:

   .. code-block:: bash

      python -m venv venv

3. Activate the virtual environment:

   **Windows:**

   .. code-block:: bash

      venv\Scripts\activate

   **macOS/Linux:**

   .. code-block:: bash

      source venv/bin/activate

4. Install dependencies:

   .. code-block:: bash

      pip install -r requirements.txt

5. Run migrations:

   .. code-block:: bash

      python manage.py migrate

6. Start the development server:

   .. code-block:: bash

      python manage.py runserver

The website should now be accessible at `http://127.0.0.1:8000/`.

Usage
-----

Navigate to the development server URL in your web browser to view and interact with the CV site. You can also modify the content and styles by editing the appropriate Django templates and static files.

Credits
-------

Prince Nkosi


.. toctree::
   :maxdepth: 2
   :caption: Contents:


