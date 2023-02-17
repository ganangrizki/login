import streamlit as st


def main():
    """Simple Login App"""

    st.title("Simple Login App")

    menu = ["Home", "Login", "Signup"]
    choice = st.sidebar("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        st.subheader("Login Section")

    elif choice == "SignUp":
        st.subheader("Create New Account")

    if __name__ == '__main__':
        main()
