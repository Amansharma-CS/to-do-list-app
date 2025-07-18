import streamlit as st
import functions

st.title("MY TO DO APP")
st.subheader("This is my to do app")
st.write("This is app is used  to increase your productivity")


todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')