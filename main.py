import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "نظام مكتب الأصالة للهندسة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True 
    page.scroll = ft.ScrollMode.AUTO
    
    def handle_exception():
        error_details = traceback.format_exc()
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.ERROR_OUTLINE, color=ft.Colors.RED, size=50),
                    ft.Text("حدث خطأ تقني:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.RED),
                    ft.Text(error_details, color=ft.Colors.ORANGE_900, selectable=True, size=12),
                ], scroll=ft.ScrollMode.ALWAYS),
                padding=20
            )
        )

    try:
        # --- واجهة المكتب المصححة ---
        header = ft.Container(
            content=ft.Column([
                ft.Text("مكتب الأصالة للهندسة", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("نظام إدارة المشاريع والمخازن", size=16, color=ft.Colors.BLUE_700),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(bottom=20),
            # التعديل هنا: استخدام أحرف كبيرة
            alignment=ft.alignment.CENTER 
        )

        menu_buttons = ft.Column([
            ft.ElevatedButton("إدارة المكونات الإلكترونية", icon=ft.Icons.ELECTRICAL_SERVICES, width=300),
            ft.ElevatedButton("مشاريع الطلاب والبحوث", icon=ft.Icons.SCHOOL, width=300),
            ft.ElevatedButton("قسم التصميم الهندسي", icon=ft.Icons.DESIGN_SERVICES, width=300),
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        page.add(
            ft.Column([
                header,
                ft.Divider(),
                menu_buttons,
                ft.Text("الموصل - نينوى | 2026", size=12, color=ft.Colors.GREY_600)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )

    except Exception:
        handle_exception()

if __name__ == "__main__":
    ft.app(target=main)
