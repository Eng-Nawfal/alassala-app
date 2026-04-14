import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "نظام مكتب الأصالة للهندسة"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.rtl = True
    page.padding = 15
    page.scroll = ft.ScrollMode.AUTO

    # --- مخزن البيانات ---
    sections = ["القدرة والآلات", "مكونات إلكترونية"]
    inventory = [
        {"item": "AVR SX460", "section": "القدرة والآلات", "qty": "10", "buy": "15000", "sell": "25000"},
    ]

    def handle_exception():
        err = traceback.format_exc()
        page.clean()
        page.add(ft.Text(f"خطأ تقني: {err}", color="red"))

    try:
        def update_all():
            render_inventory()
            render_sections()
            item_section.options = [ft.dropdown.Option(s) for s in sections]
            page.update()

        # --- 1. إدارة الأقسام ---
        new_sec_name = ft.TextField(label="اسم القسم الجديد", expand=True)
        sec_list_column = ft.Column()

        def add_sec(e):
            if new_sec_name.value:
                sections.append(new_sec_name.value)
                new_sec_name.value = ""
                update_all()

        def render_sections():
            sec_list_column.controls.clear()
            for s in sections:
                sec_list_column.controls.append(
                    ft.ListTile(
                        leading=ft.Icon(ft.Icons.FOLDER),
                        title=ft.Text(s),
                        trailing=ft.IconButton(ft.Icons.DELETE, icon_color="red", on_click=lambda e, n=s: [sections.remove(n), update_all()])
                    )
                )

        sections_view = ft.Column([
            ft.Text("إدارة الأقسام الهندسية", size=20, weight="bold"),
            ft.Row([new_sec_name, ft.ElevatedButton("إضافة قسم", on_click=add_sec)]),
            ft.Divider(),
            sec_list_column
        ], visible=False)

        # --- 2. إدارة الجرد والمواد ---
        item_name = ft.TextField(label="اسم المادة", expand=2)
        item_qty = ft.TextField(label="الكمية", expand=1)
        item_buy = ft.TextField(label="سعر الشراء", expand=1)
        item_sell = ft.TextField(label="سعر البيع", expand=1)
        item_section = ft.Dropdown(label="القسم", expand=2, options=[ft.dropdown.Option(s) for s in sections])
        
        editing_index = None

        def save_item(e):
            nonlocal editing_index
            if all([item_name.value, item_section.value]):
                data = {"item": item_name.value, "section": item_section.value, "qty": item_qty.value, "buy": item_buy.value, "sell": item_sell.value}
                if editing_index is None: inventory.append(data)
                else:
                    inventory[editing_index] = data
                    editing_index = None
                    btn_save.text = "إضافة للمخزن"
                item_name.value = item_qty.value = item_buy.value = item_sell.value = ""
                update_all()

        btn_save = ft.ElevatedButton("إضافة للمخزن", icon=ft.Icons.SAVE, on_click=save_item)
        inv_table = ft.DataTable(
            columns=[ft.DataColumn(ft.Text("المادة")), ft.DataColumn(ft.Text("الكمية")), ft.DataColumn(ft.Text("بيع")), ft.DataColumn(ft.Text("إجراء"))],
            rows=[]
        )

        def render_inventory():
            inv_table.rows.clear()
            for i, d in enumerate(inventory):
                inv_table.rows.append(ft.DataRow(cells=[
                    ft.DataCell(ft.Text(d["item"])), ft.DataCell(ft.Text(d["qty"])), ft.DataCell(ft.Text(d["sell"])),
                    ft.DataCell(ft.Row([
                        ft.IconButton(ft.Icons.EDIT, icon_color="blue", on_click=lambda e, idx=i: edit_item(idx)),
                        ft.IconButton(ft.Icons.DELETE, icon_color="red", on_click=lambda e, idx=i: [inventory.pop(idx), update_all()]),
                    ]))
                ]))

        def edit_item(idx):
            nonlocal editing_index
            editing_index = idx
            item = inventory[idx]
            item_name.value, item_section.value, item_qty.value, item_buy.value, item_sell.value = item["item"], item["section"], item["qty"], item["buy"], item["sell"]
            btn_save.text = "تحديث البيانات"
            page.update()

        # التعديل هنا: وضع الجدول في Row ثم Column لتجنب خطأ التمرير في الـ Container
        inventory_view = ft.Column([
            ft.Text("إدارة خزين المواد", size=20, weight="bold"),
            ft.Row([item_name, item_section]),
            ft.Row([item_qty, item_buy, item_sell]),
            btn_save,
            ft.Divider(),
            ft.Column([ft.Row([inv_table], scroll=ft.ScrollMode.ALWAYS)], scroll=ft.ScrollMode.ALWAYS)
        ], visible=True)

        # --- 3. الاستعلام ---
        search_field = ft.TextField(label="بحث...", prefix_icon=ft.Icons.SEARCH, on_change=lambda e: run_query(e.control.value))
        query_results = ft.Column()

        def run_query(val):
            query_results.controls.clear()
            for d in inventory:
                if val.lower() in d["item"].lower() or val in d["section"]:
                    query_results.controls.append(ft.Card(content=ft.ListTile(title=ft.Text(d['item']), subtitle=ft.Text(f"القسم: {d['section']} | الكمية: {d['qty']} | شراء: {d['buy']} | بيع: {d['sell']}"))))
            page.update()

        query_view = ft.Column([ft.Text("محرك الاستعلام", size=20, weight="bold"), search_field, query_results], visible=False)

        # --- التنقل ---
        def navigate(e):
            idx = e.control.selected_index
            inventory_view.visible = (idx == 0); query_view.visible = (idx == 1); sections_view.visible = (idx == 2)
            page.update()

        page.navigation_bar = ft.NavigationBar(
            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.INVENTORY, label="الجرد"),
                ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="استعلام"),
                ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="الأقسام"),
            ], on_change=navigate
        )

        page.add(ft.Row([ft.Text("مكتب الأصالة للهندسة", size=25, weight="bold", color="blue900")], alignment="center"), ft.Divider(), inventory_view, query_view, sections_view)
        update_all()

    except Exception: handle_exception()

if __name__ == "__main__":
    ft.app(target=main)
