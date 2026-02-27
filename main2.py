from pyscript import window,document

def dologin(event):
  print("dologin clicked")
  nameob=document.querySelector("#name_field")
  passwordob=document.querySelector("#password_field")
  print("name : ",nameob.value)
  print("password : ",passwordob.value)
  resultob=document.querySelector(".result")
  resultob.innerHTML=f'<h1> your name is {nameob.value} and password is {passwordob.value}'