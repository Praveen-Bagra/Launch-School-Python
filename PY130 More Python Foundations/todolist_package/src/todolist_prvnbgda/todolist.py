from todo import Todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title

    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError('Can only add Todo objects')

        self._todos.append(todo)

    def __str__(self):
        todos_string = '\n'.join([str(todo) for todo in self._todos])

        return (f'---- {self._title} -----\n{todos_string}') 

    def __len__(self):
        return len(self._todos)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]

    def to_list(self):
        return self._todos.copy()

    def todo_at(self, index):
        return self._todos[index]

    def mark_done_at(self, index):
        self.todo_at(index).done = True

    def mark_undone_at(self, index):
        self.todo_at(index).done = False

    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = True

        self.each(mark_undone)

    def all_done(self):
        return all([todo.done for todo in self._todos])

    def remove_at(self, index):
        self._todos.pop(index)

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_todolist = TodoList(self.title)
        for todo in filter(callback, self._todos):
                new_todolist.add(todo)

        return new_todolist

    def find_by_title(self, title):
        # for todo in self._todos:
            # if todo.title == title:
                # return todo
        
        # raise IndexError
        return self.select(lambda todo: todo.title == title).first()

    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)

    def mark_done(self, todo_title):
        self.find_by_title(todo_title).done = True
