import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "نظام مكتب الأصالة للهندسة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 20
    
    # دالة معالجة الأخطاء (بقينا عليها للأمان)
    def handle_exception():
        error_details = traceback.format_exc()
        page.clean()
        page.add(ft.Text(f"خطأ: {error_details}", color="red"))

    try:
        # --- قسم الجرد (Inventory) ---
        inventory_view = ft.Column([
            ft.Text("قائمة الجرد الهندسي", size=20, weight="bold"),
            ft.DataTable(
                columns=[
                    ft.DataColumn(ft.Text("المادة")),
                    ft.DataColumn(ft.Text("الكمية")),
                    ft.DataColumn(ft.Text("الحالة")),
                ],
                rows=[
                    ft.DataRow(cells=[ft.DataCell(ft.Text("AVR Card")), ft.DataCell(ft.Text("5")), ft.DataCell(ft.Text("متوفر"))]),
                    ft.DataRow(cells=[ft.DataCell(ft.Text("ESP32")), ft.DataCell(ft.Text("12")), ft.DataCell(ft.Text("قيد الاستخدام"))]),
                ],
            ),
            ft.FloatingActionButton(icon=ft.Icons.ADD, text="إضافة مادة للجرد")
        ], visible=True)

        # --- قسم الاستعلام (Query) ---
        query_view = ft.Column([
            ft.Text("نظام الاستعلام عن المشاريع", size=20, weight="bold"),
            ft.TextField(label="أدخل رقم المشروع أو اسم الطالب", prefix_icon=ft.Icons.SEARCH),
            ft.ElevatedButton("بحث سريع", icon=ft.Icons.SEARCH_SHARP),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.ListTile(
                            leading=ft.Icon(ft.Icons.ENGINEERING),
                            title=ft.Text("آخر الاستعلامات"),
                            subtitle=ft.Text("لا يوجد بيانات لعرضها حالياً"),
                        ),
                    ]), padding=10
                )
            )
        ], visible=False)

        # --- قسم الإعدادات / الأقسام الأخرى ---
        settings_view = ft.Column([
            ft.Text("إدارة الأقسام", size=20, weight="bold"),
            ft.ListTile(leading=ft.Icon(ft.Icons.PERSON), title=ft.Text("بيانات المهندسين")),
            ft.ListTile(leading=ft.Icon(ft.Icons.FILE_COPY), title=ft.Text("تقارير البحوث")),
        ], visible=False)

        # دالة التنقل بين الأقسام
        def navigate(e):
            inventory_view.visible = (e.control.selected_index == 0)
            query_view.visible = (e.control.selected_index == 1)
            settings_view.visible = (e.control.selected_index == 2)
            page.update()

        # شريط التنقل السفلي
        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationDestination(icon=ft.Icons.INVENTORY_2, label="الجرد"),
                ft.NavigationDestination(icon=ft.Icons.QUERY_STATS, label="استعلام"),
                ft.NavigationDestination(icon=ft.Icons.SETTINGS, label="الأقسام"),
            ],
            on_change=navigate,
        )

        # إضافة جميع الواجهات للصفحة
        page.add(
            ft.Column([
                ft.Row([
                    ft.Icon(ft.Icons.PRECISION_MANUFACTURING, color="blue900"),
                    ft.Text("مكتب الأصالة للهندسة", size=25, weight="bold", color="blue900"),
                ], alignment="center"),
                ft.Divider(height=20, color="transparent"),
                inventory_view,
                query_view,
                settings_view
            ])
        )

    except Exception:
        handle_exception()

if __name__ == "__main__":
    ft.app(target=main)
