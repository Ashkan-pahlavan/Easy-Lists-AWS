# Easy Lists

Easy Lists ist eine Webanwendung, die es Benutzern ermöglicht, Listen von Aufgaben zu erstellen und zu verwalten. Die Anwendung bietet eine einfache Benutzeroberfläche zum Hinzufügen, Löschen und Überprüfen von Aufgaben in verschiedenen Listen.

## Nutzung

Die Anwendung kann unter der folgenden Adresse direkt genutzt werden: [Easy Lists App](http://my-lits-app.s3-website.eu-central-1.amazonaws.com/)

## Features

- **Benutzeranmeldung**: Benutzer können sich mit einem Benutzernamen und einem Passwort anmelden, um ihre persönlichen Listen zu verwalten.
- **Listenverwaltung**: Benutzer können neue Listen erstellen, vorhandene Listen anzeigen und löschen.
- **Aufgabenverwaltung**: Benutzer können Aufgaben zu ihren Listen hinzufügen, sie abhaken, bearbeiten und löschen.

## Technologien

Das Projekt verwendet folgende Technologien:

- **Frontend**: HTML, CSS und JavaScript wurden verwendet, um die Benutzeroberfläche zu erstellen. Die Gestaltung ist responsiv und bietet eine benutzerfreundliche Erfahrung auf verschiedenen Geräten.
- **Backend**: Die Anwendung kommuniziert mit einer serverlosen Backend-Infrastruktur über RESTful-APIs, die auf AWS Lambda und Amazon API Gateway gehostet werden. Die Backend-Logik wird in AWS Lambda-Funktionen implementiert und mithilfe von AWS DynamoDB gespeichert.
- **Authentifizierung und Autorisierung**: Die Benutzeranmeldung wird über benutzerdefinierte Authorizer in AWS API Gateway implementiert, wobei die Benutzerinformationen in einer sicheren Datenbank gespeichert werden.
- **Deployment**: Das Frontend und die Backend-Infrastruktur werden über AWS CloudFront und S3 für das Hosting bereitgestellt. Die Anwendung ist über eine HTTPS-geschützte URL zugänglich.


## Beitrag

Wenn Sie zur Verbesserung dieses Projekts beitragen möchten, können Sie gerne:

- Pull Requests einreichen, um Fehler zu beheben, neue Funktionen hinzuzufügen oder vorhandene Funktionen zu verbessern.
- Probleme melden, um auf Probleme hinzuweisen oder neue Funktionen vorzuschlagen.

# Lambda-Back-End-Funktionen für Easy Lists

Dieses Repository enthält die Lambda-Back-End-Funktionen, die für das Easy Lists-Projekt verwendet werden. Diese Funktionen sind für die Kommunikation mit der Datenbank verantwortlich und führen verschiedene Operationen wie das Hinzufügen, Löschen und Aktualisieren von Listen und Aufgaben durch.

## Funktionen

### delete_listname.py

Diese Funktion löscht eine Listenbezeichnung und alle damit verbundenen Aufgaben aus der Datenbank.

### delete_taskdescription.py

Diese Funktion löscht eine bestimmte Aufgabenbeschreibung aus der Datenbank.

### login.py

Diese Funktion ermöglicht die Benutzeranmeldung durch Überprüfung des Benutzernamens und des Passworts.

### my_lists.py

Diese Funktion fügt eine neue Liste und die zugehörigen Aufgaben in die Datenbank ein.

### mylists_checked.py

Diese Funktion aktualisiert den Status einer Aufgabe (checked/unchecked) in der Datenbank.

### register.py

Diese Funktion ermöglicht die Registrierung neuer Benutzer und speichert ihre Anmeldeinformationen in der Datenbank.

### show_lists.py

Diese Funktion ruft alle Listen eines bestimmten Benutzers aus der Datenbank ab.

### show_task_description.py

Diese Funktion ruft alle Aufgaben für eine bestimmte Liste eines Benutzers aus der Datenbank ab.

## Einrichtung

Um diese Funktionen zu verwenden, müssen Sie:
- Die Funktionen in Ihrem AWS Lambda-Konto erstellen.
- Die erforderlichen AWS-Ressourcen wie DynamoDB-Tabellen erstellen.
- Die Lambda-Funktionen mit den entsprechenden Datenbanktabellen und Berechtigungen verknüpfen.
- Die Funktionen in der Serverless-Architektur Ihrer Anwendung aufrufen.

Weitere Informationen zur Einrichtung und Verwendung finden Sie in den Kommentaren innerhalb der Funktionen und in der offiziellen AWS-Dokumentation.

## Autor

Das Projekt wurde von Ashkan Pahlavan (ich 😊 )  entwickelt .

