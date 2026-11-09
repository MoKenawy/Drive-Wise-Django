<div align="center">

<img src="DriveWiseProject/DrivewiseApp/static/images/logo.png" alt="Drive Wise logo" width="140"/>

# Drive-Wise — Manager's Dashboard

**Safety Driving, Our Priority.**

A Django fleet-management dashboard that turns raw telemetry from the Drive-Wise
in-vehicle station into driver ratings, violation logs and live analytics.

<p>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img alt="Django" src="https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img alt="Firebase" src="https://img.shields.io/badge/Firebase-Realtime%20DB-FFCA28?style=for-the-badge&logo=firebase&logoColor=black"/>
  <img alt="Bootstrap" src="https://img.shields.io/badge/MDB5-Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
  <img alt="License" src="https://img.shields.io/badge/License-MIT-3CB54A?style=for-the-badge"/>
</p>

<img src="Drive-wise%20Dashboard%20Docs/Home%20Page.png" alt="Drive Wise landing page" width="100%"/>

</div>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Screenshots](#screenshots)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Routes](#routes)
- [Related Repositories](#related-repositories)
- [License](#license)
- [Contact](#contact)

---

## Overview

Drive-Wise is a two-part system. An **in-vehicle station** watches the driver and
the road — detecting overspeeding, drowsiness and unsafe following distance — and
streams every violation to Firebase. **This repository** is the other half: the
manager's web dashboard that reads that stream and answers the question *"how is
my fleet actually driving?"*

Each violation is logged with its type, measured value, threshold and timestamp.
From that history the dashboard derives a per-driver rating, ranks the fleet on a
leaderboard, and surfaces the best and worst performers at a glance.

<div align="center">
  <img src="Drive-wise%20Dashboard%20Docs/Dashboard.png" alt="Fleet dashboard with ratings and leaderboard" width="90%"/>
</div>

---

## Features

| | Feature | What it does |
|:--:|:--|:--|
| ⭐ | **Automatic Driver Rating** | Converts each driver's violation history into a 1–5 star score, updated as new events arrive. |
| 🏆 | **Fleet Leaderboard** | Ranks every driver and highlights the fleet average plus the best and worst performer. |
| 📋 | **Violation Logs** | Per-driver table of every event — type, recorded value, threshold that was breached, and timestamp. |
| 📊 | **Violation Analytics** | Breaks violations down by category (speed, distance, drowsiness) as an interactive chart. |
| 😴 | **Drowsiness Tracking** | Fatigue events captured by the in-vehicle station are logged and counted alongside traffic violations. |
| 👤 | **Driver Management** | Add and remove drivers from the fleet directly in the dashboard. |
| 🔐 | **Firebase Authentication** | Manager accounts with session-backed login, registration and route protection. |

<div align="center">
  <img src="Drive-wise%20Dashboard%20Docs/Features.png" alt="Feature highlights" width="90%"/>
</div>

---

## Screenshots

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>Driver detail &amp; violation log</strong><br/>
      <img src="Drive-wise%20Dashboard%20Docs/Driver%20details.png" alt="Driver detail page with violation table"/>
      <sub>Rating, totals per violation type, and the full event table.</sub>
    </td>
    <td width="50%" valign="top">
      <strong>Violation breakdown chart</strong><br/>
      <img src="Drive-wise%20Dashboard%20Docs/Driver%20Details%202.png" alt="Chart of violations by category"/>
      <sub>Speed vs. distance vs. drowsiness, per driver.</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong>Manager login</strong><br/>
      <img src="Drive-wise%20Dashboard%20Docs/Login%20(new).png" alt="Login screen"/>
      <sub>Firebase-backed authentication.</sub>
    </td>
    <td width="50%" valign="top">
      <strong>Fleet overview</strong><br/>
      <img src="Drive-wise%20Dashboard%20Docs/Dashboard.png" alt="Fleet dashboard"/>
      <sub>Average rating, best/worst driver, leaderboard.</sub>
    </td>
  </tr>
</table>

---

## Tech Stack

| Layer | Technology |
|:--|:--|
| Backend | Django 5.0 (Python 3.12+) |
| Database | Firebase Realtime Database |
| Auth | Firebase Authentication (Admin SDK + REST sign-in) |
| File storage | Firebase Cloud Storage |
| UI | MDB5 (Material Design for Bootstrap 5), MaterializeCSS form rendering |
| Charts | Chart.js |
| Local DB | SQLite (Django sessions &amp; admin only) |

---

## Getting Started

### Prerequisites

- **Python 3.12 or newer**
- A **Firebase project** with Realtime Database, Authentication and Cloud Storage enabled
- A Firebase **service-account key** (`.json`), downloadable from
  *Project settings → Service accounts → Generate new private key*

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/MoKenawy/Drive-Wise-Django.git
cd Drive-Wise-Django
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
```

```bash
# Windows
.venv\Scripts\activate
```

```bash
# macOS / Linux
source .venv/bin/activate
```

**3. Install the dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure your Firebase credentials** — see [Configuration](#configuration) below.

**5. Apply migrations and start the server**

```bash
cd DriveWiseProject
python manage.py migrate
python manage.py runserver
```

The dashboard is now live at **http://127.0.0.1:8000/**.

---

## Configuration

The project reads its Firebase settings from a `.env` file. Create one in the
**repository root** (`.env` is already listed in `.gitignore`, so it will not be
committed):

```ini
# Firebase Realtime Database URL
DB_URL=https://<your-project>-default-rtdb.firebaseio.com/

# Firebase Cloud Storage bucket
STORAGE_BUCKET_URL=<your-project>.appspot.com

# Absolute or relative path to your service-account JSON key
FIREBASE_CREDS_FILEPATH=path/to/serviceAccountKey.json

# Web API key, used for the email/password sign-in call
FIREBASE_WEB_API_KEY=<your-web-api-key>
```

| Variable | Required | Purpose |
|:--|:--:|:--|
| `DB_URL` | ✅ | Realtime Database endpoint that stores drivers and violations. |
| `STORAGE_BUCKET_URL` | ✅ | Cloud Storage bucket used for uploaded driver images. |
| `FIREBASE_CREDS_FILEPATH` | ✅ | Path to the service-account key used by the Firebase Admin SDK. |
| `FIREBASE_WEB_API_KEY` | ✅ | Identifies your project on the Identity Toolkit sign-in endpoint. Found in the Firebase console under *Project settings → General → Web API Key*. |

> **Note:** the first three are read at import time in
> `DriveWiseProject/settings.py`. If any of them is missing, Django will fail to
> start — so set them before running `manage.py`.
>
> `FIREBASE_WEB_API_KEY` is read lazily, the first time somebody signs in. If it
> is missing you will get an `ImproperlyConfigured` error at that point rather
> than at startup.

---

## Project Structure

```
Drive-Wise-Django/
├── DriveWiseProject/              # Django project root
│   ├── DriveWiseProject/          # Settings, URLs, WSGI/ASGI, Firebase init
│   ├── DrivewiseApp/              # Public site: landing, about, login, register
│   │   ├── static/                # CSS, JS and imagery for the marketing site
│   │   ├── templates/             # home, about, login, register
│   │   └── utils/firebase_utils.py
│   ├── dashboard/                 # Authenticated manager dashboard
│   │   ├── static/dashboard/      # Dashboard styles, charts, star ratings
│   │   ├── template/              # dashboard, driver_detail, add/remove driver
│   │   └── utils/firebase_utils.py
│   └── manage.py
├── Design prototyping/            # Static HTML/CSS prototypes of the UI
├── Drive-wise Dashboard Docs/     # Screenshots used in this README
├── requirements.txt
└── LICENSE
```

---

## Routes

| Path | View | Description |
|:--|:--|:--|
| `/` | `home` | Public landing page |
| `/about/` | `about` | About the project |
| `/login/` | `login` | Manager sign-in |
| `/register/` | `register` | Manager sign-up |
| `/dashboard/` | `dashboard` | Fleet overview, ratings and leaderboard |
| `/dashboard/driver/<driver_id>/` | `driver_detail` | A single driver's stats and violation log |
| `/dashboard/add_driver/` | `AddDriverView` | Add a driver to the fleet |
| `/dashboard/remove_driver/` | `RemoveDriverView` | Remove a driver from the fleet |

---

## Related Repositories

| Repository | Description |
|:--|:--|
| [**DriveWise Driving Station**](https://github.com/MoKenawy/DriveWise-Driving-Station) | The in-vehicle ADAS half of the system — detects overspeeding, drowsiness and unsafe following distance, and reports violations to Firebase. |

---

## License

Released under the **MIT License**. See [LICENSE](LICENSE) for the full text.

---

## Contact

**Mohammed Gamal** — [mokenawy.business@gmail.com](mailto:mokenawy.business@gmail.com)

<div align="center">
  <sub>Built to make the roads safer, one trip at a time. 🚗💚</sub>
</div>
