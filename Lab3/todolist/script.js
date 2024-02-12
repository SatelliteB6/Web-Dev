// Sample initial todo list
let todos = [
    { text: 'Learn HTML', done: false },
    { text: 'Learn CSS', done: true },
    { text: 'Learn JavaScript', done: false }
];

// Function to render the todo list
function renderTodos() {
    const todoListContainer = document.getElementById('todo-list');
    todoListContainer.innerHTML = ''; // Clear existing list

    todos.forEach((todo, index) => {
        const todoItem = document.createElement('div');
        todoItem.classList.add('todo-item');

        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.checked = todo.done;
        checkbox.addEventListener('change', () => toggleTodo(index));

        const text = document.createElement('span');
        text.textContent = todo.text;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';
        deleteButton.addEventListener('click', () => deleteTodo(index));

        todoItem.appendChild(checkbox);
        todoItem.appendChild(text);
        todoItem.appendChild(deleteButton);

        todoListContainer.appendChild(todoItem);
    });
}

// Function to add a new todo
function addTodo() {
    const newTodoInput = document.getElementById('newTodo');
    const newTodoText = newTodoInput.value.trim();

    if (newTodoText !== '') {
        todos.push({ text: newTodoText, done: false });
        newTodoInput.value = '';
        renderTodos();
    }
}

// Function to toggle the status of a todo (mark as done/undone)
function toggleTodo(index) {
    todos[index].done = !todos[index].done;
    renderTodos();
}

// Function to delete a todo
function deleteTodo(index) {
    todos.splice(index, 1);
    renderTodos();
}

// Initial rendering
renderTodos();
