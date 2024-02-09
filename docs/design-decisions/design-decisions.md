---
title: Design Decisions
nav_order: 3
---

{: .label }
Rayan

{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## 01: Auswahl der Datenbank - SQLAlchemy

Status
: Work in progress - **Decided**  - Obsolete

Updated
: 01-Feb-2024

### Problem statement

Wir brauchen für unsere Flask-App eine einfache, flexible Art, mit der Datenbank zu arbeiten. Diese Lösung sollte schnell gehen, leicht zu warten sein und einfach sein, bei Bedarf die Datenbank zu wechseln.

### Decision

Wir haben SQLAlchemy als unser Werkzeug gewählt, weil es eine objektorientierte Datenbankinteraktion ermöglicht und  eine Vielzahl von Datenbankbackends unterstützt. Diese Entscheidung steigert unsere Entwicklungsproduktivität, indem wir komplexe SQL-Abfragen durch Python-Code ersetzen. Das lässt uns leicht Anpassungen vornehmen und bietet Flexibilität, unsere Datenbankinfrastruktur ohne erheblichen Aufwand zu ändern oder zu zu erweitern.

### Regarded options

+ Plain SQL
+ SQLAlchemy

| Kriterien | Plain SQL | SQLAlchemy |
| --- | --- | --- |
| **Fachkenntnisse** | ✔️ Direktes Wissen über SQL wird angewandt. Keine zusätzliche Abstraktionsebene, die gelernt werden muss.| ❌ Lernaufwand, um ORM-Konzepten und SQLAlchemy zu verstehen |
| **DB Schema-Änderungen** | ❌ müssen manuell durchgeführt und im gesamten Code reflektiert werden. | ✔️ Ermöglicht einfache Schema-Migrationen durch Alembic und objektorientierte Modellierung, was die Wartung und Evolution des Schemas vereinfacht |
| **Datenbank-Engine-Wechsel** | ❌ Erheblicher Anpassungsaufwand, da unterschiedliche SQL-Dialekte beachtet werden müssen | ✔️ Einfacher Wechsel durch Abstraktion |
| **Komplexität der Anwendungslogik** | ❌ erhöht die Komplexität der Anwendungslogik, da Geschäftslogik und Datenbankinteraktionen eng miteinander verknüpft sind.| ✔️ trennt Anwendungslogik und Datenbank, was zu einer saubereren und modulareren Codebasis führt. | 

Entscheidung getroffen von: https://github.com/birtyq256

## 02: WTForms für Frontend-Formulare

Status
:  Work in progress - **Decided**  - Obsolete

Updated
: 28-JAN-2024

### Problem statement
Für die Einreichung von Buchungsanfragen benötigen wir eine effiziente, sichere und benutzerfreundliche Methode zur Gestaltung von Frontend-Formularen.

### Decision
Wir haben uns für die Verwendung von WTForms entschieden, um die Frontend-Formulare für unsere Buchungsanfragen zu gestalten. Dadurch können wir Formulare mit vielfältigen Feldtypen einfach implementieren, die Validierungslogik direkt in unserem Flask-Backend integrieren.

## Regarded Options

HTML-Formulare: 
Pro: Volle Kontrolle über das Markup; keine zusätzlichen Abhängigkeiten
Con: Manuelle Implementierung von Validierungen; erhöhter Aufwand bei der Sicherheitsabsicherung

Entscheidung getroffen von: https://github.com/birtyq256

## 03: Implementierung eines Login-Systems

Status
: Work in progress - **Decided**  - Obsolete

Updated
: 05-FEB-2024

### Problem statement

Wir benötigen ein einfaches Login-System, um eine schnelle und unkomplizierte Lösung für Demonstrationszwecke zu schaffen.

### Decision

Wir haben uns für das einfache Login-System entschieden, bei dem ein Admin sich mit vorgegebenen Zugangsdaten anmelden kann, ohne eine Datenbank zu verwenden. Die Zugangsdaten sind direkt im Code hinterlegt. Wir haben ADMIN_USERNAME und ADMIN_PASSWORD als feste Variablen in unserer Flask-Anwendung gesetzt. Diese Methode ermöglicht eine schnelle Implementierung für einen einzigen Administratorzugang.
Diese Entscheidung erfüllt die Anforderungen für unseren spezifischen Anwendungsfall.

### Regarded Options

#### Flask-Login: 

+ Pro: Vereinfacht die Implementierung sicherer Authentifizierungssysteme mit Unterstützung für Benutzersitzungen. 
+ Con: Erfordert eine Datenbank zur Speicherung von Benutzerinformationen

#### Eigene Benutzerverwaltung mit Datenbank: 

Entwicklung eines benutzerdefinierten Authentifizierungssystems, das Benutzernamen und Passwörter in einer Datenbank speichert.

+ Pro: Vollständige Kontrolle über die Authentifizierung und Benutzerverwaltung
+ Con: Erhöhter Entwicklungs- und Wartungsaufwand, erfordert sorgfältige Implementierung von Sicherheitsmaßnahmen

Entscheidung getroffen von: https://github.com/rayanbeydoun12


## 04: Service Screen

Status
:  Work in progress - **Decided**  - Obsolete

Updated
: 04-JAN-2024

### Problem statement

Benutzer, die eine individuelle Buchungsanfrage stellen möchten, benötigen einen klaren und ansprechenden Weg, um ihre Präferenzen und Anforderungen zu kommunizieren. Der Prozess sollte nicht nur funktional sein, sondern auch das hohe Niveau an Exklusivität und Personalisierung widerspiegeln, das VIP Voyage seinen Kunden bieten möchte.

### Decision

Implementierung eines Inquiry Screens mit vier ansprechenden Bildern, die unterschiedliche  Servicekategorien darstellen. Der Benutzer kann eine Kategorie auswählen. Diese visuelle Methode bietet eine benutzerfreundliche Oberfläche, die den Auswahlprozess vereinfacht und gleichzeitig visuell ansprechend ist.

### Regarded options

Dropdown-Menüs:
Pro: Ermöglicht eine einfache und klare Auswahl von Optionen.
Con: Bietet nicht die gleiche visuelle Anziehungskraft und kann weniger einladend wirken.

Entscheidung getroffen von: https://github.com/LanaKrt

## 05: Inquiry Form Screen

Status
: Work in progress - **Decided**  - Obsolete

Updated
: 04-JAN-2024

### Problem statement

Benutzer, benötigen eine klare und einfache Möglichkeit, ihre Präferenzen und Anforderungen zu kommunizieren. Die Erfahrung sollte das exklusive und personalisierte Niveau an Service vermitteln, das VIP Voyage bietet.

### Decision

Einführung eines Inquiry Form Screens, der einen klaren und direkten Weg bietet, persönliche Daten und Reisepräferenzen einzugeben. Der Hintergrund des Bildschirms zeigt eine atemberaubende Aussicht auf Mykonos, was die Exklusivität und Attraktivität des Ziels unterstreicht.

## 06: Service Selection Screen

Status
: Work in progress - **Decided**  - Obsolete

Updated
: 04-JAN-2024

### Problem statement

Kunden benötigen ein breites Angebot an spezifische Dienstleistungen, die ihren Bedürfnissen entsprechen. Die Darstellung dieser Optionen sollte das hochwertige Angebot und die Vielfalt der Dienstleistungen von VIP Voyage widerspiegeln.

### Decision

Implementierung eines Service Selection Screens mit großen, ansprechenden Bildern für jede Servicekategorie (Unterkunft, Transportmittel, etc.). Dies ermöglicht es den Benutzern, mit einem Blick die verfügbaren Dienstleistungen zu verstehen und ihre Auswahl auf eine ansprechende und interaktive Weise zu treffen.

Entscheidung getroffen von: https://github.com/LanaKrt

---

