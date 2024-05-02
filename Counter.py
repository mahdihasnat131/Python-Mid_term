from Hall_class import Hall
class counter(Hall):
    def __init__(self, Hall):
        self.Hall=Hall
    def view_all_shows(self):
        return self.Hall.show_list
    def available_seats(self,id):
        return self.Hall.view_available_seats(id)
    def book_seats_for_show(self,id,seats):
        return self.Hall.book_seats(id,seats)