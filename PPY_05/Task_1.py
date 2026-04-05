bibliophiles = { "John": {1, 2, 7, 11, 29}, "Mary": {7, 9, 11, 5}, "Jane": {1, 4, 5}, "Bill": {7, 11, 1, 2, 9}, "Kate": {4, 5, 9, 11}}



def func1(dict, name):
    person_name = ""
    person_with_most_shared_books = {}
    highest_number = 0
    person_books = dict.get(name)
    for el in dict:
        if(el == name):
            continue
        temp = len(person_books.intersection(dict.get(el)))
        if (temp > highest_number):
            highest_number = temp
            person_name = el
            person_with_most_shared_books = dict.get(el)
    

    print(f"'{name}' -> ['{person_name}', {highest_number}, {person_with_most_shared_books.difference(person_books)}]")

func1(bibliophiles, "John")
func1(bibliophiles, "Mary")

print("-------------------------")

def func2(dict, name):
    person_books = dict.get(name)
    frequent_books = {book: 0 for book in person_books}
    
    for book_onwer, set in dict.items():
        
        if book_onwer == name:
            continue
        
        for i in set:
            if i in person_books:
                frequent_books.update({i: frequent_books[i] + 1})
   
    max_count = -1
    most_frequent_book = None
    for i in frequent_books:
        if frequent_books[i] > max_count:
            max_count = frequent_books[i]
            most_frequent_book = i

    
                
    
    print(f"'{name}' -> ({most_frequent_book}, {max_count})")

func2(bibliophiles, "John")
func2(bibliophiles, "Jane")

print("-------------------------")


def func3(dict, name):
    
    
    if name not in bibliophiles:
        return None
        
    target_books = bibliophiles[name]
    unowned_book_counts = {}
    
    for book_onwer, set in dict.items():
        
        if book_onwer == name:
            continue
        
      
        for i in set - target_books:
            unowned_book_counts[i] = unowned_book_counts.get(i, 0) + 1
                
    
   
    max_count = -1
    most_frequent_book = None
    for i in unowned_book_counts:
        if unowned_book_counts[i] > max_count:
            max_count = unowned_book_counts[i]
            most_frequent_book = i

    
                
    
    print(f"'{name}' -> ({most_frequent_book}, {max_count})")

func3(bibliophiles, "John")
func3(bibliophiles, "Kate")        