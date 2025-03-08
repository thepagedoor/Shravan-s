import webbrowser
import os
import requests
import tkinter as tk
from tkinter import messagebox

# Function to save image from URL
def save_image(image_url, save_path):
    try:
        response = requests.get(image_url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            return os.path.basename(save_path)
        else:
            return None
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download image: {e}")
        return None

# Function to format full location (line break after every 6-7 words)
def format_full_location(text):
    words = text.split()
    formatted_location = ""
    for i in range(0, len(words), 6):  # Insert <br> after every 6-7 words
        formatted_location += " ".join(words[i:i+6]) + "<br>"
    return formatted_location.strip("<br>")

# Function to clean phone number (remove leading zero if present)
def clean_number(number):
    return number.lstrip("0")  # Removes only the leading zero


# Function to generate GitHub-friendly name
def generate_github_name(name):
    return name.strip().replace(" ", "-")

# Function to update copyable text
def update_copy_text():
    generated_name = generate_github_name(name_entry.get())
    copy_text_var.set(generated_name)

# Function to copy text to clipboard
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(copy_text_var.get())
    root.update()

# Function to open GitHub new repo page
def open_new_repo():
    webbrowser.open("https://github.com/new")

# Function to open GitHub repo settings
def open_repo_settings():
    generated_name = generate_github_name(name_entry.get())
    if generated_name:
        url = f"https://github.com/thepagedoor/{generated_name}/settings/pages"
        webbrowser.open(url)
    else:
        messagebox.showwarning("Warning", "Please enter a name first.")







# Function to generate the new index file
def generate_index():
    name = name_entry.get()
    image_url = image_url_entry.get()
    short_location = short_location_entry.get()
    timings = timings_entry.get().strip() or "All Days: 8:00 AM - 10:00 PM"  # Keep input if provided
    location_url = location_url_entry.get()
    full_location = format_full_location(full_location_text.get("1.0", tk.END).strip())
    number = clean_number(number_entry.get())  # Process phone number

    if not name or not image_url or not short_location or not location_url or not full_location or not number:
        messagebox.showwarning("Warning", "Please fill all required fields!")
        return

    # File paths
    output_filename = f"index.html"
    image_filename = f"{name.replace(' ', '_')}.jpg"
    image_save_path = os.path.join(os.getcwd(), image_filename)

    # Save the image
    downloaded_image = save_image(image_url, image_save_path)
    if downloaded_image:
        saved_image_path = downloaded_image
    else:
        saved_image_path = image_url  # Fallback to URL if download fails

    # Read template and replace placeholders
    template_file = "main.html"
    if not os.path.exists(template_file):
        messagebox.showerror("Error", "Template file (index_template.htm) not found!")
        return

    with open(template_file, "r", encoding="utf-8") as file:
        template = file.read()

    output_content = template.replace("{NAME}", name)
    output_content = output_content.replace("{IMAGE_URL}", saved_image_path)
    output_content = output_content.replace("{SHORT_LOCATION}", short_location)
    output_content = output_content.replace("{TIMINGS}", timings)
    output_content = output_content.replace("{LOCATION_URL}", location_url)
    output_content = output_content.replace("{FULL_LOCATION}", full_location)
    output_content = output_content.replace("{NUMBER}", number)

    # Save the modified file
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(output_content)

    messagebox.showinfo("Success", f"Generated: {output_filename}")

# Create GUI Window
root = tk.Tk()
root.title("Index.htm Generator")
root.geometry("500x600")

# Labels and Entry Fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root, width=50)
name_entry.pack()
name_entry.bind("<KeyRelease>", lambda event: update_copy_text())  # Update copy text dynamically





tk.Label(root, text="Image URL:").pack()
image_url_entry = tk.Entry(root, width=50)
image_url_entry.pack()

tk.Label(root, text="Short Location (Delhi, India):").pack()
short_location_entry = tk.Entry(root, width=50)
short_location_entry.pack()

tk.Label(root, text="Timings (Leave Empty for Default 8am to 10pm ):").pack()
timings_entry = tk.Entry(root, width=50)
timings_entry.pack()


tk.Label(root, text="Location URL:").pack()
location_url_entry = tk.Entry(root, width=50)
location_url_entry.pack()

tk.Label(root, text="Full Location (Auto Line Breaks After 6-7 Words):").pack()
full_location_text = tk.Text(root, width=50, height=5)
full_location_text.pack()

tk.Label(root, text="Contact Number:").pack()
number_entry = tk.Entry(root, width=50)
number_entry.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Index.htm", command=generate_index)
generate_button.pack(pady=10)

# Copyable Text Section
tk.Label(root, text="Generated Copyable Name:").pack()
copy_text_var = tk.StringVar()
copy_text_entry = tk.Entry(root, width=30, textvariable=copy_text_var, state="readonly")
copy_text_entry.pack()
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=5)

# Buttons for GitHub Pages
github_new_button = tk.Button(root, text="Go to GitHub New Repo", command=open_new_repo, bg="blue", fg="white")
github_new_button.pack(pady=5)

github_settings_button = tk.Button(root, text="Go to Repo Settings", command=open_repo_settings, bg="green", fg="white")
github_settings_button.pack(pady=5)

# Run Tkinter loop
root.mainloop()