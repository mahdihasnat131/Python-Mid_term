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

    
    def __book_seats(self,id,booked_seat):
        row_col=(row,col)
        self.booked_seat.append(row_col)
        if id not in self.seats:
            return "Show not available"
        else:
            self.seats[id][booked_seat]==1
            return "Booking successful"
    def _view_show_list():
        return self.show_list
    available_seats=[]
    def __view_available_seats(self,id,seats):
        if id not in self.seats:
            return "Show not available"
        else:
            for rows in range (self.seats[id]):
                for cols in range (self.seats[id]):
                    if seats[id][rows][cols]==0:
                        available_seats.append(seats[id][rows][cols])
                        return available_seats
                        
                






    
