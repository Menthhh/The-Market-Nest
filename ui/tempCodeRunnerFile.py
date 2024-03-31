    def adjust_columns(self):
            window_width = self.ui.stackedWidget.width()

            # Define the number of columns based on window size
            if window_width > 1500:
                max_columns = 6
            elif 1000 < window_width <= 1500:
                max_columns = 5
            else:
                max_columns = 4

            # Calculate the number of rows needed based on the products and max columns
            num_rows = len(self.products) // max_columns + (len(self.products) % max_columns > 0)

            # Add or remove widgets as needed
            current_items = self.productlist_layout.count()
            needed_items = num_rows * max_columns

            if current_items < needed_items:
                for i in range(current_items, needed_items):
                    row = i // max_columns
                    col = i % max_columns
                    if i < len(self.products):
                        product_data = self.products[i]
                        product_widget = ProductWidget(product_data["name"], product_data["price"],
                                                    product_data["image_path"], index_to_show=1, main_window=self)
                        self.productlist_layout.addWidget(product_widget, row, col)
            elif current_items > needed_items:
                for i in range(current_items - 1, needed_items - 1, -1):
                    item = self.productlist_layout.takeAt(i)
                    widget = item.widget()
                    if widget:
                        widget.setParent(None)