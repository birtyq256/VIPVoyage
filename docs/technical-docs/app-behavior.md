---
title: App Behavior
parent: Technical Docs
nav_order: 2
---

{: .label }
Rayan

# App behavior
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Main Features

1. **Buchungsanfragen:** Ein Button "Send Inquiry" auf der Homesseite lädt den Nutzer ein, eine Buchungsanfrage zu stellen. Sie werden dann auf eine Seite geleitet, auf der sie den gewünschten Service auswählen können, darunter luxuriöse Villen, Yachten, Premium-Autos und weitere Luxuserlebnisse. Nach der Auswahl füllen die Nutzer ein Formular aus, das in forms.py definiert ist. Nach dem Absenden des Formulars erhalten sie eine Bestätigung. 

2. **Login-Funktion für Administratoren/Agenten:** Ein Login-Bereich, der es Administratoren oder Agenten ermöglicht, sich mit festgelegten Zugangsdaten anzumelden. Es besteht auch die Möglichkeit, sich über eine Logout-Funktion wieder abzumelden.

3. **Buchungsübersicht (Inquiries Overview):** Eine Übersichtsseite, auf der Administratoren (Agenten) alle gestellten Buchungsanfragen einsehen können. Die Übersicht zeigt detaillierte Informationen zu jeder Anfrage, wie Name, Telefonnummer, Ankunfts- und Abreisedaten, Anzahl der Gäste, Budget und den aktuellen Status. Admins können den Status der Anfrage aktualisieren und Anfragen bei Bedarf löschen.
