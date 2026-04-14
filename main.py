import flet as ft
import traceback
import os

def main(page: ft.Page):
    # إعدادات الصفحة الأساسية لتناسب شاشة الموبايل
    page.title = "نظام مكتب الأصالة للهندسة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True  # لدعم اللغة العربية من اليمين لليسار
    page.scroll = ft.ScrollMode.AUTO
    
    # دالة لعرض الأخطاء في حال حدوثها بدلاً من الشاشة البيضاء
    def handle_exception():
        error_details = traceback.format_exc()
        page.clean()
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Icon(ft.Icons.ERROR_OUTLINE, color=ft.Colors.RED, size=50),
                    ft.Text("حدث خطأ تقني في النظام:", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.RED),
                    ft.Text(error_details, color=ft.Colors.ORANGE_900, selectable=True, size=12),
                ], scroll=ft.ScrollMode.ALWAYS),
                padding=20
            )
        )

    try:
        # --- بداية واجهة المستخدم لمكتب الأصالة ---
        
        # 1. عنوان المكتب
        header = ft.Container(
            content=ft.Column([
                ft.Text("مكتب الأصالة للهندسة", size=30, weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_900),
                ft.Text("نظام إدارة المشاريع والمخازن", size=16, color=ft.Colors.BLUE_700),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(bottom=20),
            alignment=ft.alignment.center
        )

        # 2. أزرار التحكم الرئيسية (كمثال)
        menu_buttons = ft.Column([
            ft.ElevatedButton(
                "إدارة المكونات الإلكترونية", 
                icon=ft.Icons.ELECTRICAL_SERVICES, 
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
            ft.ElevatedButton(
                "مشاريع الطلاب والبحوث", 
                icon=ft.Icons.SCHOOL, 
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
            ft.ElevatedButton(
                "قسم التصميم الهندسي", 
                icon=ft.Icons.DESIGN_SERVICES, 
                width=300,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
            ),
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

        # 3. تذييل الصفحة
        footer = ft.Text(
            "الموصل - نينوى | 2026", 
            size=12, 
            color=ft.Colors.GREY_600, 
            text_align=ft.TextAlign.CENTER
        )

        # إضافة العناصر للصفحة
        page.add(
            ft.Column([
                header,
                ft.Divider(),
                menu_buttons,
                ft.VerticalDivider(height=40),
                footer
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
        
        # --- نهاية واجهة المستخدم ---

    except Exception:
        handle_exception()

# تشغيل التطبيق
if __name__ == "__main__":
    ft.app(target=main)
