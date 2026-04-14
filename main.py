import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "نظام مكتب الأصالة للهندسة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # بيانات تجريبية
    sections = ["القدرة والآلات", "المتحكمات الدقيقة", "البحوث الطلابية"]
    inventory = [
        {"item": "AVR Card SX460", "section": "القدرة والآلات", "qty": "5"},
        {"item": "ESP32 DevKit", "section": "المتحكمات الدقيقة", "qty": "10"}
    ]

    def handle_exception():
        error_details = traceback.format_exc()
        page.clean()
        page.add(ft.Text(f"خطأ في النظام: {error_details}", color="red"))

    try:
        def update_ui():
            render_inventory()
            render_sections()
            page.update()

        # --- 1. قسم الجرد ---
        item_name = ft.TextField(label="اسم المادة", expand=True)
        item_qty = ft.TextField(label="الكمية", width=100)
        item_section = ft.Dropdown(label="القسم", options=[ft.dropdown.Option(s) for s in sections], expand=True)

        inventory_table = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("المادة")),
                ft.DataColumn(ft.Text("القسم")),
                ft.DataColumn(ft.Text("الكمية")),
                ft.DataColumn(ft.Text("حذف")),
            ],
            rows=[]
        )

        def render_inventory():
            inventory_table.rows.clear()
            for i, data in enumerate(inventory):
                inventory_table.rows.append(
                    ft.DataRow(cells=[
                        ft.DataCell(ft.Text(data["item"])),
                        ft.DataCell(ft.Text(data["section"])),
                        ft.DataCell(ft.Text(data["qty"])),
                        ft.DataCell(ft.IconButton(ft.Icons.DELETE, icon_color="red", on_click=lambda e, idx=i: delete_item(idx))),
                    ])
                )

        def add_item_to_inv(e):
            if item_name.value and item_section.value:
                inventory.append({"item": item_name.value, "section": item_section.value, "qty": item_qty.value})
                item_name.value = ""
                item_qty.value = ""
                update_ui()

        def delete_item(idx):
            inventory.pop(idx)
            update_ui()

        inventory_view = ft.Column([
            ft.Text("إدارة جرد المواد", size=20, weight="bold"),
            ft.Row([item_name, item_qty]),
            ft.Row([item_section, ft.ElevatedButton("إضافة", icon=ft.Icons.ADD, on_click=add_item_to_inv)]),
            ft.Divider(),
            inventory_table
        ], visible=True)

        # --- 2. قسم الاستعلام ---
        search_query = ft.TextField(label="ابحث هنا...", prefix_icon=ft.Icons.SEARCH, on_change=lambda e: run_search(e.control.value))
        search_results = ft.Column()

        def run_search(val):
            search_results.controls.clear()
            if val:
                for res in inventory:
                    if val.lower() in res["item"].lower() or val in res["section"]:
                        search_results.controls.append(ft.ListTile(title=ft.Text(res["item"]), subtitle=ft.Text(f"القسم: {res['section']}")))
            page.update()

        query_view = ft.Column([
            ft.Text("محرك البحث", size=20, weight="bold"),
            search_query,
            search_results
        ], visible=False)

        # --- 3. قسم الأقسام ---
        new_section_name = ft.TextField(label="اسم القسم الجديد", expand=True)
        sections_list = ft.Column()

        def add_new_section(e):
            if new_section_name.value:
                sections.append(new_section_name.value)
                item_section.options.append(ft.dropdown.Option(new_section_name.value))
                new_section_name.value = ""
                update_ui()

        def render_sections():
            sections_list.controls.clear()
            for s in sections:
                # استبدلنا CHIP بـ SETTINGS لضمان العمل
                sections_list.controls.append(ft.ListTile(leading=ft.Icon(ft.Icons.SETTINGS), title=ft.Text(s)))

        render_sections()
        render_inventory()

        settings_view = ft.Column([
            ft.Text("إدارة الأقسام", size=20, weight="bold"),
            ft.Row([new_section_name, ft.ElevatedButton("إضافة", on_click=add_new_section)]),
            ft.Divider(),
            sections_list
        ], visible=False)

        def navigate(e):
            inventory_view.visible = (e.control.selected_index == 0)
            query_view.visible = (e.control.selected_index == 1)
            settings_view.visible = (e.control.selected_index == 2)
            page.update()

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.INVENTORY, label="الجرد"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="استعلام"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="الأقسام"),
            ],
            on_change=navigate,
        )

        page.add(
            ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.BUILD, color="blue900"), # أيقونة BUILD مضمونة
                    ft.Text("مكتب الأصالة للهندسة", size=25, weight="bold", color="blue900"),
                ], alignment="center"),
                ft.Divider(),
                inventory_view,
                query_view,
                settings_view
            ])
        )

    except Exception:
        handle_exception()

if __name__ == "__main__":
    ft.app(target=main)
