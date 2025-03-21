import streamlit as st
import json

# Load and save the library data
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    """Save the updated library data to JSON file."""
    with open("library.json", "w") as file:
        json.dump(st.session_state.library, file, indent=4)

# Initialize library in session state
if "library" not in st.session_state:
    st.session_state.library = load_library()

st.title("📚 Personal Library Management System")
st.write("____________________________")



# Sidebar menu
menu = st.sidebar.radio("📌 Select an option", ["View Library", "Add Book", "Delete Book", "Search Book", "Save and Exit"])

# 📖 View Library
if menu == "View Library":
    st.markdown("### 📚 Your Library")
    if st.session_state.library:
        st.table(st.session_state.library)
    else:
        st.warning("⚠️ No books in the library. Add some books first.")



# ➕ Add a Book
elif menu == "Add Book":
    st.markdown("###  *Add a New Book*")
    title = st.text_input("📖 Enter the title of the book")
    author = st.text_input("✍️ Enter the author of the book")
    year = st.number_input("📅 Enter the year of the book", min_value=1000, max_value=2025, step=1)
    genre = st.text_input("🏷️ Enter the genre of the book")
    read_status = st.checkbox(" Mark as Read")

    if st.button(" Add Book"):
        if title and author and genre:
            st.session_state.library.append({
                "title": title, 
                "author": author, 
                "year": year, 
                "genre": genre, 
                "read_status": read_status
            })
            save_library()
            st.success(f"{title}' added successfully!")
            st.rerun()
        else:
            st.warning("⚠️ Please fill in all fields before adding.")


# ❌ Delete a Book
elif menu == "Delete Book":
    st.markdown("###  *Delete a Book*")
    
    if st.session_state.library:
        book_titles = [book["title"] for book in st.session_state.library]
        selected_book = st.selectbox("📖 Select a book to delete", book_titles)

        if st.button("🗑️ Delete Book"):
            st.session_state.library = [book for book in st.session_state.library if book["title"] != selected_book]
            save_library()
            st.success(f"🗑️ Book '{selected_book}' deleted successfully!")
            st.rerun()
    else:
        st.warning("⚠️ No books in the library. Add some books first.")


# 🔍 Search for a Book

elif menu == "Search Book":
    st.markdown("###  *Search for a Book*")
    search_term = st.text_input(" Enter the title or author of the book")

    if st.button("🔍 Search"):
        results = [
            book for book in st.session_state.library 
            if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()
        ]
        if results:
            st.table(results)
        else:
            st.warning("⚠️ No books found!")

# 💾 Save and Exit
elif menu == "Save and Exit":
    save_library()
    st.success("✅ Library saved successfully!")
    st.balloons()
    st.stop()
