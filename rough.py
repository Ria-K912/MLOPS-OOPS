# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 155

# print(type(my_str))
# lst.clear()
# print(lst)

from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

#using static method directly from class rather than object
chatbook.set_id(10)
user2 = chatbook()
print(user2.id)
# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)




#getter and setter
print(user1.get_name())
user1.set_name("John")
print(user1.get_name())
#print(user1.__name)
#print(user1._chatbook__name)

lst = [1,2,3]

#function
a1 = len(lst)
print(a1)

#method
user1.sendmsg()