import streamlit as st
import functions

if 'todos' not in st.session_state:
    st.session_state.todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    st.session_state.todos.append(todo)
    functions.write_todos(st.session_state.todos)
    st.session_state["new_todo"] = ""  # Clear the input after adding


st.title("My Todo App")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(st.session_state.todos):
    checkbox = st.checkbox(todo, key=f"todo_{index}")
    if checkbox:
        st.session_state.todos.pop(index)
        functions.write_todos(st.session_state.todos)
        st.rerun()

st.text_input(label="Add a new todo", placeholder="Enter a todo", on_change=add_todo, key='new_todo')
