import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "نظام مكتب الأصالة للهندسة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 20
    
    def handle_exception():
        error_details = traceback.format_exc()
        page.clean()
        page.add(ft.Text(f"خطأ تقني: {error_details}", color="red"))

    try:
        # --- الأقسام ---
        inventory_view = ft.Column([
            ft.Text("قائمة الجرد الهندسي", size=20, weight="bold"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("المادة")),
                    ft.DataColumn(ft.Text("الكمية")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("AVR Card")), ft.DataCell(ft.Text("5"))]),
                ],
            ),
            ft.FloatingActionButton(icon=ft.Icons.ADD) 
        ], visible=True)

        query_view = ft.Column([
            ft.Text("نظام الاستعلام", size=20, weight="bold"),
            ft.TextField(label="بحث...", prefix_icon=ft.Icons.SEARCH),
        ], visible=False)

        settings_view = ft.Column([
            ft.Text("الإعدادات", size=20, weight="bold"),
            ft.ListTile(title=ft.Text("بيانات المكتب")),
        ], visible=False)

        def navigate(e):
            inventory_view.visible = (e.control.selected_index == 0)
            query_view.visible = (e.control.selected_index == 1)
            settings_view.visible = (e.control.selected_index == 2)
            page.update()

        # التعديل هنا: استخدمنا المسمى الجديد NavigationBarDestination
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
                    ft.Icon(ft.Icons.PRECISION_MANUFACTURING, color="blue900"),
                    ft.Text("معرض ملاك ", size=25, weight="bold", color="blue900"),
                ], alignment="center"),
                ft.Divider(height=10),
                inventory_view,
                query_view,
                settings_view
            ])
        )

    except Exception:
        handle_exception()

if __name__ == "__main__":
    ft.app(target=main)
