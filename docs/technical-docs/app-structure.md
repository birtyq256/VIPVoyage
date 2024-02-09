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
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Main Features

1. **Buchungsanfragen:** Ein Button "Send Inquiry" auf der Homesseite lädt den Nutzer ein, eine Buchungsanfrage zu stellen. Sie werden dann auf eine Seite geleitet, auf der sie den gewünschten Service auswählen können, darunter luxuriöse Villen, Yachten oder Premium-Autos. Nach der Auswahl füllen die Nutzer ein Formular aus, das4 in forms.py definiert ist. Nach dem Absenden des Formulars erhalten sie eine Bestätigung. 

2. **Login-Funktion für Administratoren/Agenten:** Ein Login-Bereich, der es Administratoren oder Agenten ermöglicht, sich mit festgelegten Zugangsdaten anzumelden. Es besteht auch die Möglichkeit, sich über eine Logout-Funktion wieder abzumelden.

3. **Buchungsübersicht (Inquiries Overview):** Eine Übersichtsseite, auf der Administratoren (Agenten) alle gestellten Buchungsanfragen einsehen können. Die Übersicht zeigt detaillierte Informationen zu jeder Anfrage, wie Name, Telefonnummer, Ankunfts- und Abreisedaten, Anzahl der Gäste, Budget und den aktuellen Status. Admins können den Status der Anfrage aktualisieren und Anfragen bei Bedarf löschen.

Unsere Webanwendung "VIPVoyage" ist folgendermaßen strukturiert:

**app.py**: Die Hauptdatei, die die Flask-Anwendung initialisiert, Routen definiert und die Logik der Webanwendung steuert.

**db.py**: Zuständig für die Datenbankinteraktionen

**forms.py**: Definiert die Formulare für Benutzereingaben, unter Nutzung von Flask-WTF.

**static**: Verzeichnis, für statische Dateien wie CSS, JavaScript und Bilder zur Gestaltung der Benutzeroberfläche.

**templates**: Definieren das HTML-Grundgerüst, das für die Darstellung der verschiedenen Seiten der Anwendung verwendet wird.

**migrations**: Verzeichnis für Alembic-Migrationen, das die Versionierung und Migration der Datenbankstruktur ermöglicht.

**requirements.txt**: Eine Datei, die die Abhängigkeiten auflistet, welche für das Ausführen der Anwendung benötigt werden

**README.md**: Eine Markdown-Datei, die eine Übersicht über das Projekt, Installationsanweisungen und andere nützliche Informationen bietet

**.git und .gitignore**: Verzeichnis und Datei für Git-Versionierung, um die Versionskontrolle der Anwendung zu verwalten und bestimmte Dateien oder Verzeichnisse von der Versionskontrolle auszuschließen.

**env**: Ein Verzeichnis, das für die Umgebungsvariablen verwendet wird, um Konfigurationen wie Datenbankverbindungen sicher zu speichern.

**instance**: Ein Ordner, der für Instanz-spezifische Konfigurationen genutzt werden kann, wie z.B. geheime Schlüssel.

**flask_session**: Ein Verzeichnis für die Speicherung von Flask-Sessiondaten.


{: .download }
> This is a download callout.
>



