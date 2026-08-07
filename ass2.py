def border(func):
    def wrapper(*args):
        print("=" * 30)
        func(*args)
        print("=" * 30)
    return wrapper


class Report:

    template = "General Report"

    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def change_template(cls, name):
        cls.template = name

    def __str__(self):
        return f"{self.template}\nTitle: {self.title}\nContent: {self.content}"

    def __len__(self):
        return len(self.content)

    @border
    def display(self):
        print(self)

Report.change_template("Sales Report")

r1 = Report("January", "Sales = ₹50,000")

r1.display()

print("Content Length:", len(r1))