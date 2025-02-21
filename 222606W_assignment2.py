class Book:
    def __init__(self, title, year_published, isbn, category, publisher):
        self.title = title
        self.year_published = year_published
        self.isbn = isbn
        self.category = category
        self.publisher = publisher

    def update_details(self, title, year_published, isbn, category, publisher):
        self.title = title
        self.year_published = year_published
        self.isbn = isbn
        self.category = category
        self.publisher = publisher


class Customer:
    def __init__(self, customer_id, name, email, tier, points):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.tier = tier
        self.points = points


class CustomerRequest:
    def __init__(self, customer_id, request_details):
        self.customer_id = customer_id
        self.request_details = request_details


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


def bubble_sort_books_category(books):
    n = len(books)
    for i in range(n):
        for j in range(0, n-i-1):
            if books[j].category > books[j+1].category:
                books[j], books[j+1] = books[j+1], books[j]
    return books


def selection_sort_books_publisher_desc(books):
    n = len(books)
    for i in range(n-1):
        max_idx = i
        for j in range(i+1, n):
            if books[j].publisher > books[max_idx].publisher:
                max_idx = j
        books[i], books[max_idx] = books[max_idx], books[i]
    return books


def insertion_sort_books_title_asc(books):
    for i in range(1, len(books)):
        current_book = books[i]
        j = i - 1
        while j >= 0 and current_book.title < books[j].title:
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = current_book
    return books


def merge_sort_books_year_isbn_asc(books):
    if len(books) <= 1:
        return books

    mid = len(books) // 2
    left_half = books[:mid]
    right_half = books[mid:]

    left_half = merge_sort_books_year_isbn_asc(left_half)
    right_half = merge_sort_books_year_isbn_asc(right_half)

    return merge_year_isbn(left_half, right_half)


def merge_year_isbn(left, right):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index].year_published > right[right_index].year_published:
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index].year_published < right[right_index].year_published:
            merged.append(right[right_index])
            right_index += 1
        else:
            if left[left_index].isbn > right[right_index].isbn:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def add_new_customer(customer_dict):
    customer_id = input("Enter the Customer ID: ").upper()
    if customer_id in customer_dict:
        print("Customer ID already exists. Please enter a unique ID.")
        return

    name = input("Enter the customer's name: ")
    email = input("Enter the customer's email: ")

    # Validate and get the initial points for the customer
    while True:
        try:
            points = int(input("Enter the initial points for the customer: "))
            if points < 0:
                print("Points cannot be negative. Please enter a non-negative value.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer for points.")

    # Create a new customer object and add it to the customer_dict
    new_customer = Customer(customer_id, name, email, "C", points)
    customer_dict[customer_id] = new_customer
    print("New customer added successfully!")

def add_new_book(books):
    title = input("Enter the book title: ")
    while True:
        year_published = int(input("Enter the year of publication: "))
        if 1920 <= year_published <= 2023:
            break
        print('Invalid year. Please enter a valid year between 1920 and 2023.')
    isbn = input("Enter the ISBN number: ")
    category = input("Enter the book category: ")
    publisher = input("Enter the book publisher: ")
    new_book = Book(title, year_published, isbn, category, publisher)
    books.append(new_book)
    print("New book added successfully!")

def edit_book(books):
    search_query = input("Enter ISBN or title of the book to edit: ")
    found_books = []

    for book in books:
        if search_query.lower() in book.isbn.lower() or search_query.lower() in book.title.lower():
            found_books.append(book)

    if not found_books:
        print("No matching books found.")
        return

    print("Matching books:")
    for i, book in enumerate(found_books, start=1):
        print(f"{i}. ISBN: {book.isbn} - Title: {book.title}")

    choice = int(input("Select the book to edit (enter corresponding number): ")) - 1

    if 0 <= choice < len(found_books):
        book_to_edit = found_books[choice]

        new_title = input("Enter new book title : ")
        new_category = input("Enter new book category : ")
        new_publisher = input("Enter new book publisher : ")
        new_year_published = int(input("Enter new year published : "))

        book_to_edit.update_details(new_title, new_year_published, book_to_edit.isbn, new_category, new_publisher)

        print("Book record updated successfully!")
    else:
        print("Invalid choice.")

def manage_customer_requests(customer_dict, queue):
    while True:
        print("\nCustomer Request Page:")
        print("1. Input customer request")
        print("2. View number of request")
        print("3. Service next request in Queue")
        print("4. Return to Main Menu")
        request_choice = int(input("Please select one: "))

        if request_choice == 1:
            customer_id = input("Enter Customer ID: ").upper()
            if customer_id not in customer_dict:
                print("Invalid Customer ID. Please try again!.")
                continue

            request_details = input("Enter Customer's request: ")

            request = CustomerRequest(customer_id, request_details)
            queue.enqueue(request)
            print("Customer's request added successfully!")

        elif request_choice == 2:
            print(f"Number of request: {queue.size()}")

        elif request_choice == 3:
            if not queue.is_empty():
                request = queue.dequeue()
                print("\nCustomer Request Details:")
                customer = customer_dict[request.customer_id]
                print("--------------------------------------------")
                print(f"Customer ID: {customer.customer_id}")
                print(f"Customer Name: {customer.name}")
                print(f"Customer Email: {customer.email}")
                print(f"Customer Tier: {customer.tier}")
                print(f"Customer Points: {customer.points}")
                print("--------------------------------------------")
                print(f"Request Details: {request.request_details}")
                print("--------------------------------------------")
                print(f"Remaining request: {queue.size()}")
            else:
                print("No customer requests in the queue.")

        elif request_choice == 4:
            break

        else:
            print("Invalid choice. Please try again.")


def populate_data(books):
    while True:
        print("\nEnter Book Details (or enter '0' to stop adding)")
        title = input("Enter the book title: ")
        if title == '0':
            break

        year_published = int(input("Enter the year of publication: "))
        if 1920 <= year_published <= 2023:
            break
        print('Invalid year. Please enter a valid year between 1920 and 2023.')
        isbn = input("Enter the ISBN number: ")
        category = input("Enter the book category: ")
        publisher = input("Enter the book publisher: ")
        new_book = Book(title, year_published, isbn, category, publisher)
        books.append(new_book)

    print("Data populated successfully!")


#def is_valid_year(year):
   # year = int(year)
    #return 1910 <= year <= 2023


def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input != '':
            return user_input
        print("Invalid input. Please try again.")


#def is_unique_isbn(isbn, books):
    #return all(isbn != book.isbn for book in books)


def update_customer_tier(customer):
    if customer.points >= 5000:
        customer.tier = "A"
    elif customer.points >= 3000:
        customer.tier = "B"
    else:
        customer.tier = "C"


def search_book_by_title(books):
    search_title = input("Enter the title to search for: ")
    found_books = [book for book in books if search_title.lower() in book.title.lower()]
    if not found_books:
        print("No books found with that title.")
    else:
        print("Found Books:")
        for book in found_books:
            print(f"{book.title}, {book.year_published}, {book.isbn}, {book.category}, {book.publisher}")


def display_customer_details(customer_dict):
    customer_id = input("Enter the Customer ID to display details: ").upper()
    if customer_id in customer_dict:
        customer = customer_dict[customer_id]
        print("\nCustomer Details:")
        print(f"Customer ID: {customer.customer_id}")
        print(f"Customer Name: {customer.name}")
        print(f"Customer Email: {customer.email}")
        print(f"Customer Tier: {customer.tier}")
        print(f"Customer Points: {customer.points}")
    else:
        print("Invalid Customer ID. Please try again!")

def print_colored(text, color_code):
    print("\033[" + str(color_code) + "m" + text + "\033[0m")

option_colors = {
    "1": 31,
    "2": 32,
    "3": 33,
    "4": 34,
    "5": 35,
    "6": 36,
    "7": 32,
    "8": 33,
    "0": 34,
}


def main_menu():
    books = []
    queue = Queue()
    customer_dict = {
        "S222": Customer("S222", "John Tan", "jtan@yahoo.com", "C", 2000),
        "S333": Customer("S333", "Rae Choo", "Raechoo@hotmail.com", "B", 3500),
        "S444": Customer("S444", "Jia Yi", "Jiayi@gmail.com", "A", 5000)
    }

    while True:
        print_colored("\nMain Menu Page", option_colors["0"])
        print_colored("1. Display all the books record", option_colors["1"])
        print_colored("2. Add a new book record", option_colors["2"])
        print_colored("3. Sort books by Category in ascending order using Bubble sort and display", option_colors["3"])
        print_colored("4. Sort books by Publisher in descending order using Selection sort and display", option_colors["4"])
        print_colored("5. Sort books by Title in ascending order using Insertion sort and display", option_colors["5"])
        print_colored("6. Sort books by Year published and then ISBN in ascending order using Merge sort and display", option_colors["6"])
        print_colored("7. Manage customer request", option_colors["7"])
        print_colored("8. Populate data", option_colors["8"])
        #print("9. Unique ISBN Validation (Additional Feature)")
        print_colored("9. Update Customer Tier (Additional Feature)", option_colors["1"])
        print_colored("10. Search Book by Title (Additional Feature)", option_colors["2"])
        print_colored("11. Display Customer Details (Additional Feature)", option_colors["3"])
        print_colored("12. Add new users (Additional Feature)", option_colors["4"])
        print_colored("13. Edit book details (Additional Feature)", option_colors["5"])
        print_colored("0. Exit", option_colors["6"])
        choice = int(input("Please select one: "))
        #add new customer
        
        if choice == 1:
            if not books:
                print("No books in the list.")
            else:
                print("\nAll Books:")
                for book in books:
                    print(f"{book.title}, {book.year_published}, {book.isbn}, {book.category}, {book.publisher}")

        elif choice == 2:
            add_new_book(books)

        elif choice == 3:
            sorted_books = bubble_sort_books_category(books.copy())
            print("\nBooks sorted by Category (Bubble Sort):")
            for book in sorted_books:
                print(f"{book.title}, {book.year_published}, {book.isbn}, {book.category}, {book.publisher}")

        elif choice == 4:
            sorted_books = selection_sort_books_publisher_desc(books.copy())
            print("\nBooks sorted by Publisher (Selection Sort - Descending Order):")
            for book in sorted_books:
                print(f"{book.title}, {book.year_published}, {book.isbn}, {book.category}, {book.publisher}")

        elif choice == 5:
            sorted_books = insertion_sort_books_title_asc(books.copy())
            print("\nBooks sorted by Title (Insertion Sort):")
            for book in sorted_books:
                print(f"{book.title}, {book.year_published}, {book.isbn}, {book.category}, {book.publisher}")

        elif choice == 6:
            sorted_books = merge_sort_books_year_isbn_asc(books.copy())
            print("\nBooks sorted by Year Published and ISBN (Merge Sort):")
            for book in sorted_books:
                print(f"{book.title}, {book.year_published}, {book.isbn}, {book.category}, {book.publisher}")

        elif choice == 7:
            manage_customer_requests(customer_dict, queue)

        elif choice == 8:
            populate_data(books)

        #elif choice == 9:
            # Additional Feature 1: Unique ISBN Validation
            #isbn = get_valid_input("Enter the ISBN number: ")
            #while not is_unique_isbn(isbn, books):
                #print("ISBN number already exists. Please enter a unique ISBN.")
                #isbn = get_valid_input("Enter the ISBN number: ")

        elif choice == 9:
            # Additional Feature 2: Customer Tier Update
            customer_id = input("Enter Customer ID to update tier: ").upper()
            if customer_id in customer_dict:
                customer = customer_dict[customer_id]
                points = int(input("Enter the points for the customer: "))
                customer.points = points
                update_customer_tier(customer)
                print("Customer tier updated successfully.")
            else:
                print("Invalid Customer ID. Please try again!.")

        elif choice == 10:
            # Additional Feature 3: Book Search by Title
            search_book_by_title(books)

        elif choice == 11:
            # Additional Feature 4: Display Customer Details
            display_customer_details(customer_dict)

        elif choice == 12:
            add_new_customer(customer_dict)

        elif choice == 13:
            edit_book(books)

        elif choice == 0:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()

