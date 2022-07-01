import pywhatkit as pw
import flask

txt="""In this Farhan Shaikh Ansari Python project for beginners in Hindi, you will learn critical skills that will make you sharp in Python. 
Python is one of the most used languages currently, and the demand for programmers in the market is not slowing down.""" 

pw.text_to_handwriting(txt,"demo1.png",[0,0,138])
print(" END ")