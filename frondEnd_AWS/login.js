// Funktion zum Anzeigen oder Ausblenden des Passworts
function togglePasswordVisibility(inputId) {
  const input = document.getElementById(inputId);
  if (input.type === "password") {
      input.type = "text";
  } else {
      input.type = "password";
  }
}

// Ereignishandler für das Umschalten der Passwort-Sichtbarkeit beim Klicken auf die Schaltfläche "Show Password"
document.getElementById('showPassword').addEventListener('click', function() {
  togglePasswordVisibility('psw');
  this.classList.toggle('active');
});

// Ereignishandler für das Umschalten der Passwort-Sichtbarkeit beim Klicken auf die Schaltfläche "Show New Password"
document.getElementById('showNewPassword').addEventListener('click', function() {
  togglePasswordVisibility('newpsw');
  togglePasswordVisibility('newpsw_repeat');
  this.classList.toggle('active');
});

// Anmeldeformular
document.getElementById('loginForm').addEventListener('submit', async function(event) {
  event.preventDefault();

  const UserName = document.getElementById('uname').value;
  const Password = document.getElementById('psw').value;
  
  try {

    const response = await fetch('https://mvz54kpu1b.execute-api.eu-central-1.amazonaws.com/st/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ UserName, Password })
    });

    if (!response.ok) {
      throw new Error(`Anmeldefehler! Status: ${response.status}`);
    }

    const data = await response.json();

    if (data.message === "Registrierung erfolgreich!") {
      alert('Login Successful!');
      localStorage.setItem('UserName', UserName);
      window.location.href = 'app.html';
    } else {
      alert('Registration failed! Please check your details and try again.');
    }


  } catch (error) {
    console.error('Fehler bei der Anmeldung:', error.message);
    alert('Login failed! Please try again later.');
  }
});

// Registrierungsformular
document.getElementById('registerForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Verhindert das Standardverhalten des Formulars (Neuladen der Seite)

    const UserName = document.getElementById('newuname').value;
    const Password = document.getElementById('newpsw').value;
    const RepeatPassword = document.getElementById('newpsw_repeat').value;

    // Überprüfen, ob die Passwörter übereinstimmen
    if (Password !== RepeatPassword) {
        alert('Passwords do not match!');
        return;
    }

    try {
        const response = await fetch('https://mvz54kpu1b.execute-api.eu-central-1.amazonaws.com/st/update_item', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ UserName, Password })
        });

        if (!response.ok) {
            throw new Error(`Registrierungsfehler! Status: ${response.status}`);
        }

        const data = await response.json();

        if (data.message === "Benutzer erfolgreich hinzugef\u00fcgt") {
            alert('Registration successful!');
            localStorage.setItem('UserName', UserName);
            window.location.href = 'app.html';
        } else {
            alert('Registration failed! Please check your details and try again.');
        }
    } catch (error) {
        console.error('Fehler bei der Registrierung:', error.message);
        alert('Registration error! Please try with new username.');
    }
});


