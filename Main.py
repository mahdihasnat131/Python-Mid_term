from Counter import counter
class main():
    while True:
        print("1.View movie list")
        print("2.View available seats")
        print("3.Book Tickets")
        print("4.Exit")
    
    
        selection=input()
        if selection == '1':
            counter.view_all_shows()
        elif selection == '2':
            id=input()
            counter.available_seats
        elif selection == '3':
            id=input()
            seats=int(input())
            counter.book_seats_for_show()
        elif selection == '4':
            break
