import flet as ft
import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Select at least one option"
    
    return ''.join(random.choice(characters) for _ in range(length))

def main(page: ft.Page):
    page.title = "Password Generator"
    page.theme_mode = ft.ThemeMode.DARK
    
    password_field = ft.TextField(label="Generated Password", read_only=True, width=300, text_align=ft.TextAlign.LEFT)
    status_text = ft.Text("", size=16, color=ft.colors.GREEN)
    
    length_label = ft.Text("Password Length", size=16, color=ft.colors.WHITE)
    length_slider = ft.Slider(min=4, max=32, value=12, label="{value}")
    use_letters = ft.Switch(label="Include Letters", value=True)
    use_digits = ft.Switch(label="Include Digits", value=True)
    use_symbols = ft.Switch(label="Include Symbols", value=True)
    
    def on_generate(e):
        password_field.value = generate_password(int(length_slider.value), use_letters.value, use_digits.value, use_symbols.value)
        status_text.value = "Generated!"
        page.update()
    
    def on_copy(e):
        page.set_clipboard(password_field.value)
        status_text.value = "Copied!"
        page.update()
    
    generate_button = ft.ElevatedButton(
        text="Generate Password", on_click=on_generate, opacity=0.8, style=ft.ButtonStyle(color=ft.colors.WHITE)
    )
    
    copy_button = ft.IconButton(ft.icons.COPY, on_click=on_copy)
    
    page.add(
        ft.Column([
            length_label,
            length_slider,
            use_letters,
            use_digits,
            use_symbols,
            password_field,
            ft.Row([generate_button, copy_button], alignment=ft.MainAxisAlignment.START),
            status_text
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    )

ft.app(target=main)