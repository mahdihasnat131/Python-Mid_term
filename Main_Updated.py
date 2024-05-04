class Hall:
    def __init__(self, rows, cols):
        self.seats={}
        self.show_list=[]
        self.rows=rows
        self.cols=cols
        self.booked_seat=[]
    def _entry_show(self, id, movie_name, time):
        info=(id, movie_name, time)
        self.show_list.append(info)
        self.seats[id]=[[0]*self.cols for _ in range(self.rows)]

    
    def _book_seats(self,id,row,col):
        if id not in self.seats:
            return "Show not available"
        elif self.seats[id][row][col]==1:
            return "Seat already booked"
        else:
            self.seats[id][row][col]=1
            self.booked_seat.append((row,col))
            return "Booking successful"
    def _view_show_list(self):
        return self.show_list
    
    def _view_available_seats(self,id):
        available_seats=[]
        if id not in self.seats:
            return "Show not available"
        else:
            for row in range (self.rows):
                for col in range (self.cols):
                    if self.seats[id][row][col]==0:
                        available_seats.append((row,col))
            return available_seats
                    
class Star_Cinema(Hall):
	hall_list=[]
	def entry_hall(self, Hall):
		self.hall_list.append(Hall)


class counter(Hall):
    def __init__(self, Hall):
        self.Hall=Hall
    def view_all_shows(self):
        return self.Hall.show_list()
    def available_seats(self,id):
        return self.Hall.view_available_seats(id)
    def book_seats_for_show(self,id,row,col):
        return self.Hall.book_seats(id,row,col)

 
class main():
    def __init__(self):
        self.counter=counter(Hall(30,30))
        
    
    while True:
        print("1.View movie list")
        print("2.View available seats")
        print("3.Book Tickets")
        print("4.Exit")
                
                
        selection=int(input("Enter your choice: "))
        if selection == 1:
            print(counter.view_all_shows())
        elif selection == 2:
            id=int(input("Enter show id: "))
            print(counter.available_seats(id))
        elif selection == 3:
            id=int(input("Enter show ID: "))
            row=int(input("Enter row: "))
            col=int(input("Enter column: "))
            print(counter.book_seats_for_show(id, row, col))
        elif selection == 4:
            break


      
     



           