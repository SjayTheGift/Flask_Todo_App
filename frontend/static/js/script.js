window.addEventListener("DOMContentLoaded", (event) => {

    const url = "http://localhost:5000/todos"

    function fetchTodos() {
        fetch(url)
        .then(function(response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to get todo items.');
            }
        })
        .then(data => {
            // Process the data and update the UI
            console.log(data);
            var todoList = document.getElementById('todoList');
            if (todoList){
                todoList.innerHTML = '';
                for (var i = 0; i < data.length; i++) {
                    var todo = data[i];
                    var li = document.createElement('li');
                    li.appendChild(document.createTextNode(todo.title));
                    todoList.appendChild(li);
                }
            }
            
        })
        .catch(error => console.error(error));
    }

    fetchTodos();


    const todoForm = document.getElementById('addTodoForm');
    const successMessage = document.getElementById('successMessage');

    let title = document.getElementById('title')
    
    if (todoForm) {
        todoForm.addEventListener('submit', function (event) {
            event.preventDefault();

            fetch(`${url}/create`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                
                body: JSON.stringify({ 'title': title.value.trim(), 'is_complete': false})
            })
            .then(function(response) {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Failed to add todo item.');
                }
            })
            .then(data => {

                console.log(data)

                successMessage.textContent = data.message;
                successMessage.style.display = 'block';

                // Set timeout to hide message after displaying it
                setTimeout(function() {
                    successMessage.style.display = 'none';
                }, 2000);

                title.value = "";
            })
            .catch(function(error) {
                console.log(error);
            });
        });
    }

});