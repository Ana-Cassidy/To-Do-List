from to_do_website import create_app

# Create app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port = 8000)