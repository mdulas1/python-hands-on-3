"""
1. You are managing your shopping list: shopping = ['Milk', 'Bread', 'Eggs', 'Butter'].
Add 'Tomatoes' to the end of the list.


2. You have a list of movies: movies = ['Titanic', 'Avatar', 'Inception'].
Insert 'The Matrix' between 'Avatar' and 'Inception'.


3. Your task list: tasks = ['Email client', 'Write report', 'Submit invoice'].
Replace 'Write report' with 'Write blog post'.


4. Your daily routine: routine = ['Wake up', 'Exercise', 'Shower', 'Breakfast'].
Remove 'Exercise' from the list.


5. You’re packing your bag: items = ['Notebook', 'Pen', 'Charger', 'Water Bottle'].
Display only the first 2 items.


6. You’re ranking your favorite sports: sports = ['Football', 'Basketball', 'Tennis', 'Golf'].
Sort the list in alphabetical order.


7. A list of travel destinations: places = ['Lagos', 'Accra', 'Nairobi', 'Cairo'].
Find the index of 'Nairobi' in the list.


8. You’re updating your playlist: songs = ['Calm Down', 'Ojapiano', 'Unavailable'].
Add 'Feeling' to the beginning of the list.


9. You’re organizing your bookshelf: books = ['1984', 'Brave New World', 'Fahrenheit 451'].
Replace '1984' with 'Animal Farm'.


10. You’re keeping track of borrowed items: borrowed = ['Umbrella', 'Jacket', 'Book'].
Remove and print the last item returned using pop().


11. Your favorite fruits: fruits = ['Apple', 'Mango', 'Banana'].
Add two more fruits: 'Pineapple' and 'Orange'.


12. List of programming languages: languages = ['Python', 'Java', 'C++', 'Rust'].
Count how many items are in the list.


13. You’re managing your expenses: expenses = ['Food', 'Transport', 'Data', 'Rent'].
Delete 'Data' using del.


14. List of months: months = ['January', 'February', 'March', 'April'].
Print only the last 2 months.


15. Your class attendance list: students = ['James', 'Anna', 'Peter'].
Add 'Sarah' after 'Anna'.


16. You’re managing files: files = ['doc1.txt', 'doc2.txt', 'doc3.txt'].
Replace 'doc2.txt' with 'report.txt'.


17. Pet names: pets = ['Buddy', 'Max', 'Bella'].
Remove 'Max' and add 'Rocky' at the same position.


18. Your weekend activities: weekend = ['Sleep', 'Clean', 'Watch TV', 'Read'].
Show the second and third items only.


19. Bookmarks in your browser: bookmarks = ['google.com', 'stackoverflow.com', 'wikipedia.org'].
Add 'github.com' to the list and sort alphabetically.


20. A list of clothes to wash: laundry = ['Shirt', 'Trousers', 'Socks', 'Jacket'].
Remove the last item and insert 'Sweater' at the beginning.

"""
# question 1
shopping = ['Milk', 'Bread', 'Eggs', 'Butter']
shopping.append("Tomatos")
# question 2
movies = ['Titanic', 'Avatar', 'Inception']
movies.insert(2,"The Matrix")
print(movies)
# question 3
tasks = ['Email client', 'Write report', 'Submit invoice']
tasks[1] = "Write blog post"
print(tasks)

# quetion 4
routine = ['Wake up', 'Exercise', 'Shower', 'Breakfast']
routine.pop(1)
print(routine)

# quetion 5 
items = ['Notebook', 'Pen', 'Charger', 'Water Bottle']
display = items[:2]
print(display)

# question 6
sports = ['Football', 'Basketball', 'Tennis', 'Golf']
sports.sort()
print(sports)

# question 7
places = ['Lagos', 'Accra', 'Nairobi', 'Cairo']
length = places.index("Nairobi")
print(length)
# question 8
songs = ['Calm Down', 'Ojapiano', 'Unavailable']
songs.insert(0,"Feeling")
print(songs)
# question 9
books = ['1984', 'Brave New World', 'Fahrenheit 451']
books[0] = "Animal Farm"
print(books)
# question 10
borrowed = ['Umbrella', 'Jacket', 'Book']
borrowed.pop()
print(borrowed)
# question 11
fruits = ['Apple', 'Mango', 'Banana']
fruits.append("Pineapple") 
fruits.append("Orange")
print(fruits)
# question 12
languages = ['Python', 'Java', 'C++', 'Rust']
languages = len(languages)
print(languages)

# question 13
expenses = ['Food', 'Transport', 'Data', 'Rent'] 
del expenses[2]
print(expenses)

# question 14
months = ['January', 'February', 'March', 'April']
print(months[2:])

# question 15 
students = ['James', 'Anna', 'Peter']
students.insert(2,"Sarah")
print(students)

# queston 16
files = ['doc1.txt', 'doc2.txt', 'doc3.txt']
files[1] = "report.txt"
print(files)

# question 17
pets = ['Buddy', 'Max', 'Bella']
pets[1] = "Rocky"
print(pets)

# question 18
weekend = ['Sleep', 'Clean', 'Watch TV', 'Read']
print(weekend[1:3])

# question 19

bookmarks = ['google.com', 'stackoverflow.com', 'wikipedia.org']
bookmarks.append("github")
bookmarks.sort()
print(bookmarks)

# question 20
laundry = ['Shirt', 'Trousers', 'Socks', 'Jacket']
laundry.pop()
laundry.insert(0,"Sweater")
print(laundry)

markets = ["Terminus","Mangu market","Bokkos Market","Bukuru Market","B Ladi Market"]
kasuwa = ["halle daily market","dorowa tsoho market","gyambus market"]
markets.extend(kasuwa)
length = len(markets)
print(length)
markets.pop()
del markets[0]
print(markets)
print(markets)
can = markets[0], markets[2]
print(len(can))
