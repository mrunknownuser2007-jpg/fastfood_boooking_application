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
  orderingob=document.querySelector(".ordering")
  orderingob.innerHTML=f'<s> your order is {orderob.value} and quantity selected {quantityob.value}'  