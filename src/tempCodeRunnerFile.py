import flet as ft
import sys
from short_url import shorten_url, get_long_url, display_url_count

def main(page: ft.Page):
    page.title = "URL Shortener"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#f5f5f7"
    page.padding = 30

    PRIMARY_COLOR = "#4a6bff"
    SECONDARY_COLOR = "#38b6ff"
    BG_COLOR = "#f5f5f7"
    CARD_COLOR = "#ffffff"
    TEXT_COLOR = "#333333"

    long_url_input = ft.TextField(label="Enter long URL",
                                  width=500, border_color=PRIMARY_COLOR,
                                  focused_border_color=SECONDARY_COLOR,
                                  color=TEXT_COLOR,
                                  bgcolor=CARD_COLOR,
                                  icon=ft.Icons.LINK)
    short_id_output = ft.Text("",
                              size=16,
                              weight="bold",
                              color=PRIMARY_COLOR)
    short_id_input = ft.TextField(label="Enter short ID",
                                  width=500, border_color=PRIMARY_COLOR,
                                  focused_border_color=SECONDARY_COLOR,
                                  color=TEXT_COLOR,
                                  bgcolor=CARD_COLOR,
                                  icon=ft.Icons.TAG)
    long_url_output = ft.Text("",
                              size=16,
                              weight="bold",
                              color=PRIMARY_COLOR)
    url_count_output = ft.Text(f"Number of shortened URLs: {display_url_count()}",
                               size=16,
                              weight="bold",
                              color=TEXT_COLOR)
    
    shorten_button = ft.ElevatedButton("Shorten URL", on_click=lambda e: on_shorten_click(e),
                                      bgcolor=PRIMARY_COLOR, color="white",
                                      icon=ft.Icons.SHORT_TEXT,
                                      width=200, height=45)
    
    retrieve_button = ft.ElevatedButton("Retrieve Original URL", on_click=lambda e: on_retrieve_click(e),
                                       bgcolor=SECONDARY_COLOR, color="white", icon=ft.Icons.SEARCH,
                                        width=200, height=45)




    def on_shorten_click(e):
        short_id = shorten_url(long_url_input.value)
        short_id_output.value = f"Shortened URL ID: {short_id}"
        url_count_output.value = f"Number of shortened URLs: {display_url_count()}"
        short_id_output.update()
        url_count_output.update()

    def on_retrieve_click(e):
        long_url = get_long_url(short_id_input.value)
        long_url_output.value = f"Original URL: {long_url}"
        long_url_output.update()

    page.add(
        ft.Column([
            ft.Text("URL Shortener", size=30, weight="bold"),
            long_url_input,
            ft.ElevatedButton("Shorten URL", on_click=on_shorten_click),
            short_id_output,
            ft.Divider(),
            short_id_input,
            ft.ElevatedButton("Retrieve Original URL", on_click=on_retrieve_click),
            long_url_output,
            ft.Divider(),
            url_count_output,
        ], alignment="center", horizontal_alignment="center")
    )

ft.app(main)
