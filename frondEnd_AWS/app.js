document.addEventListener('DOMContentLoaded', async function() {
  const userName = localStorage.getItem('UserName');
  const userIdInput = document.getElementById('userIdInput');
  userIdInput.value = userName;
  userIdInput.disabled = true;

  document.getElementById('taskInput').addEventListener('keydown', function(event) {
      if (event.keyCode === 13) {
          aufgabeHinzufuegen();
      }
  });

});




async function aufgabenLaden() {
  try {
      const listName = document.getElementById('listNameInput').value;
      const userName = document.getElementById('userIdInput').value;
      
      const response = await fetch(`https://nd5tbhnyvl.execute-api.eu-central-1.amazonaws.com/stage/all_task?listName=${listName}&UserName=${userName}`);
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const sortedTasks = sortTasks(data);
      renderTasks(sortedTasks);
  } catch (error) {
      console.error('Fehler beim Laden der Aufgaben:', error);
  }
}
function sortTasks(tasks) {
  // Sortiere die Aufgaben so, dass zuerst die ungeprüften und dann die geprüften Aufgaben angezeigt werden
  const uncheckedTasks = tasks.filter(task => !task.checked);
  const checkedTasks = tasks.filter(task => task.checked);
  return uncheckedTasks.concat(checkedTasks);
}

function renderTasks(tasks) {
  const aufgabenListe = document.getElementById('todoListe');
  aufgabenListe.innerHTML = ''; 

  if (tasks.length > 0) {
      tasks.forEach(task => {
          const li = document.createElement('li');
          li.id = `task_${task.id}`;

          const checkbox = document.createElement('input');
          checkbox.type = 'checkbox';
          checkbox.classList.add('checkbox-custom');
          checkbox.id = `checkbox_${task.id}`;
          checkbox.checked = task.checked;

          const label = document.createElement('label');
          label.htmlFor = checkbox.id;
          label.textContent = `✔️ ${task.task}`;
          label.classList.add('checkbox-label');
          if (task.checked) {
              label.classList.add('task-checked');
          }

          checkbox.addEventListener('change', async function() {
              try {
                  await updateTaskStatus(task.task, this.checked);
                  label.classList.toggle('task-checked', this.checked);
              } catch (error) {
                  console.error('Fehler beim Aktualisieren der Aufgabe:', error);
              }
          });

          label.addEventListener('click', function() {
            event.preventDefault(); 
            checkbox.checked = !checkbox.checked;
            label.classList.toggle('task-checked', checkbox.checked);
            updateTaskStatus(task.task, checkbox.checked);
        });

          li.appendChild(checkbox);
          li.appendChild(label);

          const deleteButton = document.createElement('button');
          deleteButton.textContent = 'Delete';
          deleteButton.onclick = function () {
            const taskDescription = task.task; 
            aufgabeLoeschen(document.getElementById('listNameInput').value, taskDescription);
          };
          li.appendChild(deleteButton);

          aufgabenListe.appendChild(li);
      });
      showTableNames();
  } else {
      alert('No tasks were found.');
  }
}

async function aufgabeLoeschen(listName, taskDescription) {
  try {
      const confirmed = confirm('Are you sure you want to delete this task?');
      if (!confirmed) {
        return;
      }
      const response = await fetch(`https://nd5tbhnyvl.execute-api.eu-central-1.amazonaws.com/stage/delete_task`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ listName, taskDescription })
      });
      
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }

      await aufgabenLaden();
  } catch (error) {
      console.error("Fehler beim Löschen des Tasks:", error);
  }
}

async function showTableNames() {
  try {
      const userName = document.getElementById('userIdInput').value;
      const apiUrl = 'https://nd5tbhnyvl.execute-api.eu-central-1.amazonaws.com/st/listName_post';
      const response = await fetch(apiUrl, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ UserName: userName })
      });
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }

      const tableNames = await response.json();
      renderTableNames(tableNames);
  } catch (error) {
      console.error('Fehler beim Laden der Tabellennamen:', error);
      alert('Error loading table names. Please try again later.');
  }
}

function renderTableNames(tableNames) {
  const tableList = document.getElementById('tableList');
  tableList.innerHTML = ''; 

  tableNames.forEach(tableName => {
      const li = document.createElement('li');
      li.textContent = tableName;
      li.appendChild(createDeleteButton(tableName));
      li.addEventListener('click', function () {
          document.getElementById('listNameInput').value = tableName;
          aufgabenLaden();
      });
      tableList.appendChild(li);
  });
}

function createDeleteButton(tableName) {
  const deleteButton = document.createElement('button');
  deleteButton.textContent = '❌';
  deleteButton.onclick = function () {
      deleteTable(tableName);
  };
  return deleteButton;
}

async function deleteTable(listName) {
    try {
        const userName = localStorage.getItem('UserName');
        const confirmed = confirm('Are you sure you want to delete this list with all its tasks?');
        if (!confirmed) return;
  
        const requestBody = {
            UserName: userName,
            listName: listName
        };
  
        const response = await fetch('https://nd5tbhnyvl.execute-api.eu-central-1.amazonaws.com/stage/delete_listname', {
            method: "POST", 
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(requestBody)
        });
  
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
  
        await showTableNames(); // Aktualisieren der Tabellennamen nach dem Löschen
    } catch (error) {
        console.error("Fehler beim Löschen der Tabelle:", error);
    }
  }
  
async function aufgabeHinzufuegen() {
  try {
      const userId = document.getElementById('userIdInput').value;
      const listName = document.getElementById('listNameInput').value;
      const taskDescription = document.getElementById('taskInput').value;

      if (!listName || !taskDescription) {
          alert('Please enter list name and a task!');
          return;
      }

      const requestBody = { listName, task: taskDescription, UserName: userId };

      const response = await fetch('https://nd5tbhnyvl.execute-api.eu-central-1.amazonaws.com/st/post_item', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(requestBody)
      });

      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }

      document.getElementById('taskInput').value = '';
      await aufgabenLaden();
  } catch (error) {
      console.error('Error adding record:', error.message);
  }
}

async function updateTaskStatus(taskDescription, checked) {
  const listName = document.getElementById('listNameInput').value;
  const response = await fetch(`https://nd5tbhnyvl.execute-api.eu-central-1.amazonaws.com/stage/checked`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ listName, taskDescription, Checked: checked })
  });

  if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
  }
}
