---
title: App Structure
parent: Technical Docs
nav_order: 1
---

{: .label }
Rayan

# Appstruktur
{: .no_toc }

<details open markdown="block">
  <summary>Table of contents</summary>
  {: .text-delta }
  + ToC
  {: toc }
</details>

**Unsere Webanwendung "VIPVoyage" ist folgendermaßen strukturiert:**

| Datei/Verzeichnis | Beschreibung |
| ----------------- | ------------ |
| `app.py`          | Die Hauptdatei, die die Flask-Anwendung initialisiert, Routen definiert und die Logik der Webanwendung steuert. |
| `db.py`           | Zuständig für die Datenbankinteraktionen. |
| `forms.py`        | Definiert die Formulare für Benutzereingaben, unter Nutzung von Flask-WTF. |
| `static`          | Verzeichnis für statische Dateien wie CSS, JavaScript und Bilder zur Gestaltung der Benutzeroberfläche. |
| `templates`       | Enthält HTML-Template-Dateien, die für die Darstellung der verschiedenen Seiten der Anwendung verwendet werden. |
| `migrations`      | Verzeichnis für Alembic-Migrationen zur Versionierung und Migration der Datenbankstruktur. |
| `requirements.txt`| Listet alle Abhängigkeiten auf, die für das Ausführen der Anwendung benötigt werden. |
| `README.md`       | Bietet eine Übersicht über das Projekt sowie Installationsanweisungen. |
| `.git` und `.gitignore` | Für Git-Versionierung zur Verwaltung der Versionskontrolle und zum Ausschließen bestimmter Dateien. |
| `env`             | Verzeichnis für Umgebungsvariablen, um Konfigurationen sicher zu speichern. |
| `instance`        | Ordner für instanzspezifische Konfigurationen wie geheime Schlüssel. |
| `flask_session`   | Speichert Sessiondaten der Flask-Anwendung. |

