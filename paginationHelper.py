class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        length = len(self.collection) / self.items_per_page
        return length if int(length) == length else int(length) + 1 
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if len(self.collection) - page_index * self.items_per_page <= 0 or len(self.collection) == 0 or page_index < 0:
            return -1
        elif len(self.collection) - page_index * self.items_per_page > self.items_per_page:
            return self.items_per_page
        else:
            return len(self.collection) - page_index * self.items_per_page 
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if len(self.collection) <= item_index or item_index < 0 or len(self.collection) == 0:
            return -1
        else:
            return int(item_index / self.items_per_page)


collection = ['a','b','c','d','e','f']
helper = PaginationHelper(collection, 4)

print(helper.page_index(2))