import tkinter as tk


WINDOW_SIZE = 1500
POINT_RADIUS = 6


class DragPointApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("01 - TESTRUN")
        self.root.geometry(f"{WINDOW_SIZE}x{WINDOW_SIZE}")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=WINDOW_SIZE,
            height=WINDOW_SIZE,
            bg="white",
            highlightthickness=0,
        )
        self.canvas.pack()

        cx = WINDOW_SIZE // 2
        cy = WINDOW_SIZE // 2
        self.point_id = self.canvas.create_oval(
            cx - POINT_RADIUS,
            cy - POINT_RADIUS,
            cx + POINT_RADIUS,
            cy + POINT_RADIUS,
            fill="black",
            outline="",
        )

        self.dragging = False
        self.drag_offset = (0, 0)

        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

    def on_mouse_down(self, event: tk.Event) -> None:
        x1, y1, x2, y2 = self.canvas.coords(self.point_id)
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            self.dragging = True
            cx = (x1 + x2) / 2
            cy = (y1 + y2) / 2
            self.drag_offset = (event.x - cx, event.y - cy)

    def on_mouse_drag(self, event: tk.Event) -> None:
        if not self.dragging:
            return
        new_cx = event.x - self.drag_offset[0]
        new_cy = event.y - self.drag_offset[1]

        new_cx = max(POINT_RADIUS, min(WINDOW_SIZE - POINT_RADIUS, new_cx))
        new_cy = max(POINT_RADIUS, min(WINDOW_SIZE - POINT_RADIUS, new_cy))

        self.canvas.coords(
            self.point_id,
            new_cx - POINT_RADIUS,
            new_cy - POINT_RADIUS,
            new_cx + POINT_RADIUS,
            new_cy + POINT_RADIUS,
        )

    def on_mouse_up(self, event: tk.Event) -> None:
        self.dragging = False


def main() -> None:
    root = tk.Tk()
    DragPointApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
