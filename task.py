# ====== Chat Room Menu ======
# 1. Join Chat
# 2. Leave Chat
# 3. Show Active Users
# 4. Exit
# Enter your choice (1-4): 1
# Enter username to join: alice
# ✅ User 'alice' joined the chat.

# ====== Chat Room Menu ======
# 1. Join Chat
# 2. Leave Chat
# 3. Show Active Users
# 4. Exit
# Enter your choice (1-4): 1
# Enter username to join: alice
# ⚠️ User 'alice' is already in the chat!

x = int(input("Enter the number "))
set1 = set({})
while True:

    match x:
        case 1:name = input("Enter the name") ; set1.add(name); print(set1); break
        case 2:name = input("Enter the name to delete") ; set1.remove(name) ; print(set1); break
        case 3:print(set1); break
        case 4:exit

