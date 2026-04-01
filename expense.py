class expense:
    def __init__(self, title, amount, category):
        self.__title = title
        self.__amount = amount
        self.__category =  category
    
    def get_title(self):
        return self.__title
    def get_amount(self):
        return self.__amount
    def get_category(self):
        return self.__category
    
    def to_dict(self):
        return {"title":self.__title, "amount":self.__amount, "category":self.__category}
    
# e = expense("icecream", 100, "Food")
# print(e.to_dict())
# print(e.get_amount())
# print(e.get_category())
# print(e.get_title())