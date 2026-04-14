import flet as ft
import traceback

def main(page: ft.Page):
    # إعدادات الصفحة
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
                    ft.Text("خطأ في الواجهة:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.RED),
                    ft.Text(error_details, color=ft.Colors.ORANGE_900, selectable=True, size=12),
                ], scroll=ft.ScrollMode.ALWAYS),
                padding=20
            )
        )

    try:
        # --- واجهة المكتب باستخدام التنسيق المبسط ---
        
        # استبدلنا ft.alignment.CENTER بـ "center" مباشرة كـ String
        header = ft.Container(
            content=ft.Column([
                ft.Text("مكتب الأصالة للهندسة", size=30, weight="bold", color="blue900"),
                ft.Text("نظام إدارة المشاريع والمخازن", size=16, color="blue700"),
            ], horizontal_alignment="center"),
            margin=ft.margin.only(bottom=20),
            alignment=ft.Alignment(0, 0) # هذه هي الطريقة الرياضية للمركز (0,0) وهي مضمونة 100%
        )

        menu_buttons = ft.Column([
            ft.ElevatedButton("إدارة المكونات الإلكترونية", icon=ft.Icons.ELECTRICAL_SERVICES, width=300),
            ft.ElevatedButton("مشاريع الطلاب والبحوث", icon=ft.Icons.SCHOOL, width=300),
            ft.ElevatedButton("قسم التصميم الهندسي", icon=ft.Icons.DESIGN_SERVICES, width=300),
        ], spacing=15, horizontal_alignment="center")

        page.add(
            ft.Column([
                header,
                ft.Divider(),
                menu_buttons,
                ft.Container(height=40),
                ft.Text("الموصل - نينوى | 2026", size=12, color="grey600")
            ], horizontal_alignment="center")
        )

    except Exception:
        handle_exception()

if __name__ == "__main__":
    ft.app(target=main)
