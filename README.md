<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="">
  <h3 align="center">ALIAS TEST</h3>

  <p align="center">
    Alias test project
    <br />
    <a href="https://github.com/Lubov93/alias.git"><strong>Explore the docs »</strong></a>
    <br />
<a href="https://t.me/pythonDevLuba">Report Bug</a>
    <br />
   
    

  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Tests</t></a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
####alias field - string;
####target field - string;
####start field - timestamp/datetime;
####end field - timestamp/datetime or None.
##About Functionality:
####referred_obj_slug() - *gets list of slugs for particular alias. Limitation on particular end period is optional;*
####get_aliases() - *gets aliases which were running at the specific time. Aliases may start before from_time or end after to_time;*
####replace_alias() - *replaces an existing alias with a new one at a specific time point.*



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation


1. Clone the repo
   ```sh
   git clone https://github.com/Lubov93/alias.git
   ```
2. Enter to directory</br>
     ```sh
    cd alias
    ```
   
3. Activate virtualenv</br>
   ```sh
    virtualenv venv_alias&source venv_alias/bin/activate
    ```
4. Install packages
   ```sh
   pip install -r requirements.txt
   ```

5. Run server </br>
   ```sh
    python manage.py runserver
    ```
  

<!-- USAGE EXAMPLES -->
## Usage
####To enter inside SQLite DB and check functionality please run:

\$ python manage.py shell</br>
">>> from app.models import Alias, Object;"</br>
">>> from app.views import get_aliases, referred_obj_slug, replace_alias;"</br>
">>> from datetime import datetime;"</br>
">>>"</br> 
">>> Alias.objects.values_list();"</br>
">>> Object.objects.values_list();"</br>
">>>"</br>
">>> referred_obj_slug('au');"</br>
">>>" </br>
">>> from_time = datetime.now();"</br>
">>> to_time = datetime.now();"</br>
">>> get_aliases(target='whatsapp', from_time=from_time, to_time=to_time);"</br>
">>>"</br> 
">>> replace_at = datetime.now();"</br>
">>> replace_alias(4, replace_at, 'Tenis');"

#Tests
###Tests are separated into distinct folder /tests/ with models and views tests.

To check tests run:
```sh
python manage.py test ./app/tests/
```