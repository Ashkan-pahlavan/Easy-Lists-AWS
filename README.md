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

## Installation und Verwendung

Um das Projekt lokal auszuführen, führen Sie die folgenden Schritte aus:

1. Klonen Sie das GitHub-Repository: `git clone <URL_des_Repositories>`
2. Navigieren Sie in das Verzeichnis des Projekts: `cd EasyLists`
3. Öffnen Sie die `index.html`-Datei im Browser, um die Anwendung auszuführen.

Für die lokale Entwicklung und Tests müssen Sie sicherstellen, dass Node.js und npm auf Ihrem System installiert sind. Installieren Sie dann die erforderlichen Abhängigkeiten mit dem Befehl `npm install`.

## Beitrag

Wenn Sie zur Verbesserung dieses Projekts beitragen möchten, können Sie gerne:

- Pull Requests einreichen, um Fehler zu beheben, neue Funktionen hinzuzufügen oder vorhandene Funktionen zu verbessern.
- Probleme melden, um auf Probleme hinzuweisen oder neue Funktionen vorzuschlagen.

## Autor

Das Projekt wurde von Ashkan Pahlavan (ich 😊 )  entwickelt .

