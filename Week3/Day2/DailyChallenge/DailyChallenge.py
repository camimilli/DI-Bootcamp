# Daily Challenge: Pagination
import math 

# Step 1 

class Pagination:

# Step 2 

    def __init__(self, items = None, page_size = 10):
        self.items = items 
        if self.items == None:
            self.items = []
        
        if isinstance(page_size, int) and page_size > 0:
            self.page_size = page_size 
        else:
            raise ValueError('Page size must be a positive integer')
        self.current_idx = 0
        self.number_of_pages = math.ceil(len(self.items) / self.page_size)

# Step 3

    def get_visible_items(self)->list:
        '''
        Returns the list of items visible on the current page
        '''
        start_index = self.current_idx * self.page_size 
        end_index = start_index + self.page_size
        return self.items[start_index:end_index]
    
# Step 4

    def go_to_page(self, page_num):
        '''
        Goes to the specified page number 
        '''
        try:
            if isinstance(page_num, int) and page_num in range(1, self.number_of_pages):
                self.current_idx = page_num - 1 
            elif isinstance(page_num, str):
                raise TypeError('you can\'t add a string')
            else:
                raise IndexError(f'the page number is not in the range of valid pages the range is between 1 and {self.number_of_pages}')
        except Exception as e:
            print(f'{e}')

                

    def first_page(self):
        '''
        Navigates to the first page 
        '''
        self.current_idx = 0
        return self 
    
    def last_page(self):
        '''
        Navigates to the last page 
        '''
        self.current_idx = self.number_of_pages - 1
        return self 

    def next_page(self):
        '''
        Moves one page forward 
        (if not already on the last page)
        '''
        if self.current_idx != self.number_of_pages - 1:
            self.current_idx += 1 
        else:
            print('You are on the last page, can\'t move one page forward')

        return self 
    
    def previous_page(self):
        '''
        Moves one page backwards
        (if not already on the first)
        '''
        if self.current_idx != 0:
            self.current_idx -= 1 
        else:
            print("You're on the first page, can't move one page backwards")
        return self 

    def __str__(self): 
        return "\n".join(self.get_visible_items())
        

alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
print(str(p))

p.next_page()
print(p.get_visible_items())

p.last_page()
print(p.get_visible_items())

p.go_to_page(6)
print(p.current_idx + 1)

p.go_to_page('1')