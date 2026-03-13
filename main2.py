from pyscript import window,document

def dologin(event):
  print("dologin clicked")
  nameob=document.querySelector("#name_field")
  passwordob=document.querySelector("#password_field")
  print("name : ",nameob.value) 
  print("password : ",passwordob.value)
#  resultob=document.querySelector(".result")
 # resultob.innerHTML=f'<h1> your name is {nameob.value} and password is {passwordob.value}'

def do_login(event):
  print("do_login clicked")
  orderob=document.querySelector("#order_field")
  quantityob=document.querySelector("#quantity_field")
  print("order : ",orderob.value)
  print("quantity : ",quantityob.value)
#  orderingob=document.querySelector(".ordering")
 # orderingob.innerHTML=f'<s> your order is {orderob.value} and quantity selected {quantityob.value}'  



#from pyscript import Element

# def do_login(event):
    # 1. Logic to save your data (e.g., to a database or local storage)
    # save_data_function() 

    # 2. Select the container and hide it
#  login_box = Element("login-container")
#  login_box.add_class("hidden") 
    
    # Or change style directly:
    # login_box.element.style.display = "none"
    
#  print("Data saved and container removed!")


def do_loginin(event):
  print("do_loginin clicked")
  problemsob=document.querySelector("#problems_field")
  opinionsob=document.querySelector("#opininons_field")
  print("problems : ",problemsob.value)
  print("opininons : ",opinionsob.value)